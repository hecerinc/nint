# nintCompiler.py

import os
import sys
import pickle

# Hide traceback from exceptions:
# sys.tracebacklimit = None

from utils.Stack import Stack
from icg.Temp import Temp
from symbols.Operators import Operator, RELOPS
from symbols.Types import DType
from semantics.Cube import SemanticCube
from symbols.Env import Env # Symbol Table
from symbols.Function import Function
from symbols.Variable import Variable
from icg.CompMem import CompMem as Memory, MemType
import utils.utils as utils


# TODO: probs should remove this from here
GOTO = 'goto'
GOTOF = 'gotoF'
GOTOV = 'gotoV'
ENDPROC = 'ENDPROC'
PARAM = 'PARAM'
ERA = 'ERA'
GOSUB = 'GOSUB'
RETURN = 'RETURN'
GLOBAL = '__global'

debug_mode = os.getenv('NINT_ENV', 'debug')

def debug(*args):
	if debug_mode == 'debug':
		for arg in args:
			print("[nint]: {}".format(arg), end = '')
		print()

def printable(item):
	return ' ' if item is None else str(item)


no_check = ['serialize', 'functionDirectory', 'intercode', '__check_main']

class nintCompiler:
	"""docstring for nintCompiler"""
	def __init__(self):
		super().__init__()
		self.OperatorStack = Stack()
		self.OperandStack = Stack()
		self.TypeStack = Stack()
		self.JumpStack = Stack()
		self.GScope = Env(None, MemType.GLOBAL) # Global env?

		# Function helpers
		self._found_main = False
		self._print = False
		self._current_func = None
		self._call_proc = None
		self._func_returned = None # Check if the current function has returned something
		self._param_k = None
		# Generate the global scope and insert it into the functions directory
		# gscope = Function(GLOBAL, None, VOID)
		# self.FunDir.insert(gscope) # TODO: are objects passed by reference here?
		self.ScopeStack = Stack() # Keep track of the current Scope
		self.ScopeStack.push(self.GScope)

		# Temporal memory
		self._Temporal = Temp()

		self.quads = []

		# Add GOTO main
		self.quads.append([GOTO, None, None, None])


	def __getattribute__(self, attr):
		method = object.__getattribute__(self, attr)
		# if not method:
		# 	raise Exception("Method %s not implemented" % attr)
		if callable(method):
			name = method.__code__.co_name
			if name not in no_check and not name.startswith('procedure'):
				self.__check_main()
		return method

	def __check_main(self):
		if not self._found_main and self._current_func is None:
			self._found_main = True
			self.quads[0][3] = len(self.quads)

	def serialize(self, filename = "out.nint.bytecode"):
		'''Serialize the quads and the quads into an intermediate
		obj file to be read by the VM.'''
		const_map = dict()
		for const_dict in Memory.CONST_TABLE.values():
			for const, var in const_dict.items():
				const_map[var.address] = utils.parseVar(var)
		temp_counters = self._Temporal._counters
		data = [self.quads, const_map, temp_counters]
		with open(filename, 'wb') as f:
			pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


	def intercode(self):
		'''Print the quadruples'''
		for i, quad in enumerate(self.quads):
			if debug_mode == 'debug':
				print("{}) ".format(i), end='')
			print('\t'.join(map(printable, quad)))

	def add_var_declaration(self, type_str: str, identifier: str):
		'''Add variable to the varsTable of the current context'''
		debug("add_var_declaration")
		current_scope = self.ScopeStack.peek()
		# Check if it's not already been defined
		if current_scope.exists(identifier):
			raise Exception('Double declaration. {} has already been declared in this context.'.format(identifier))

		dtype = DType(type_str)
		address = current_scope.memory.next_address(dtype)

		var = Variable(identifier, dtype, address)
		current_scope.insert(var)


	def add_var(self, token: str):
		'''Add variable to the operand stack'''
		debug("add_var")

		current_scope = self.ScopeStack.peek()
		variable = current_scope.get(token)
		# Check that the variable has already been declared _somewhere_ (could be current, could be upper scopes)
		assert variable is not None, "Name {} has not been declared.".format(token)

		debug("add_var: OperandStack.push({})".format(variable.name))
		debug("add_var: TypeStack.push({})".format(variable.dtype))
		self.OperandStack.push(variable)
		self.TypeStack.push(variable.dtype)

		debug()

	def add_constant(self, token, dtype: DType):
		'''Adds a constant to the operand stack'''
		debug("add_constant")
		debug("Operand.push({})".format(token))
		debug("TypeStack.push({})".format(dtype))
		debug()
		self.OperandStack.push(Memory.constant(dtype, token)) # TODO: should we parse?
		self.TypeStack.push(dtype)
		debug()

	def add_operator(self, op: str):
		''' Adds operator op to the OperatorStack'''
		debug("add_operator")
		debug("Operator.push({})".format(op))
		operator = Operator(op)
		self.OperatorStack.push(operator) # TODO: change this to an enum
		debug()

	# TODO: refactor the check_* functions
	def check_relop(self):
		debug("check_relop")
		top = self.OperatorStack.peek()
		debug('top: {}'.format(top))
		if top not in RELOPS:
			return
		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug((operator, left_type, right_type))
		result = self._Temporal.next(DType.BOOL)
		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))
		self.OperandStack.push(result)
		# Relational operators *always* return a boolean
		self.TypeStack.push(DType.BOOL)
		debug()


	def check_addsub(self):
		debug('check_addsub')
		top = self.OperatorStack.peek()

		if not (top == Operator.ADD or top == Operator.SUB):
			return

		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug((operator, left_type, right_type))

		result_type = SemanticCube.check(operator, left_type, right_type)
		result = self._Temporal.next(result_type)
		self.OperandStack.push(result)
		self.TypeStack.push(result_type)

		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))

		debug()

	def check_multdiv(self):
		debug('check_multdiv')
		top = self.OperatorStack.peek()

		if not (top == Operator.MULT or top == Operator.DIV):
			return

		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug((operator, left_type, right_type))

		result_type = SemanticCube.check(operator, left_type, right_type)
		result = self._Temporal.next(result_type)
		self.OperandStack.push(result)
		self.TypeStack.push(result_type)

		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))

		debug()

	# If-Else
	# --------------------------------------------
	def ifelse_start_jump(self):
		debug("ifelse_start_jump")
		expression_type = self.TypeStack.pop()
		debug(expression_type)
		if expression_type != DType.BOOL:
			raise Exception("Type mismatch on line {}".format('SOMELINE TODO FIX THIS')); # TODO: maybe make a static function for this?
		result = self.OperandStack.pop()
		debug("ADD START QUAD FOR IFELSE")
		self.quads.append([GOTOF, result, None, None])
		self.JumpStack.push(len(self.quads)-1) # TODO: definitely change this. There has to be a better way to do this

	def ifelse_end_jump(self):
		debug("ifelse_end_jump")
		counter = len(self.quads) # TODO: change this
		debug('counter: {}'.format(counter))
		self.fill(self.JumpStack.pop(), counter)
		debug()

	def fill(self, pending_jump_pos, jump_location):
		debug("fill")
		self.quads[pending_jump_pos][3] = jump_location # TODO: definitely make a class for this

	def ifelse_start_else(self):
		debug("ifelse_start_else")
		debug("ADD ELSE QUAD GOTO")
		self.quads.append([GOTO, None, None, None])

		# Fill the false condition jump of the `if`
		if_false_jump = self.JumpStack.pop()
		counter = len(self.quads) # TODO: counter
		self.JumpStack.push(counter-1)
		self.fill(if_false_jump, counter)


	def assignment_quad(self):
		debug("assignment_quad")
		operator = self.OperatorStack.pop()

		assert operator == Operator.ASSIGN

		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()

		debug("<{}> = <{}>".format(left_type, right_type))

		# TODO: probably change this
		# TODO: these don't need to be *exactly* the same, they just need to be compatible
		# example: float a = 10
		assert right_type == left_type, "Type mismatch: assignment does not match"

		self.quads.append((operator.value, right_operand.address, None, left_operand.address))

		debug()


	# While
	# --------------------------------------------
	def while_condition_start(self):
		debug("while_condition_start")
		counter = len(self.quads) # TODO: counter
		self.JumpStack.push(counter)


	def while_block_start(self):
		debug("while_block_start")
		expression_type = self.TypeStack.pop()
		if expression_type != DType.BOOL:
			raise Exception("Type mismatch on line {}".format("SOMELINE FIX THIS TODO"))
		result = self.OperandStack.pop()
		debug("ADD QUAD: while block_start GOTOF")
		self.quads.append([GOTOF, result, None, None])
		counter = len(self.quads)
		self.JumpStack.push(counter - 1) # TODO: counter


	def while_end(self):
		debug("while_end")

		pending_while_end_jump = self.JumpStack.pop()
		return_pos = self.JumpStack.pop()

		debug("ADD QUAD: while_end GOTO return")
		self.quads.append([GOTO, None, None, return_pos])

		counter = len(self.quads) # TODO: change this
		self.fill(pending_while_end_jump, counter)


	# Function definitions
	# --------------------------------------------
	def procedure_start(self, name: str):
		'''Insert procedure name into dirfunc table, verify semantics'''
		debug('procedure_start')
		current_scope = self.ScopeStack.peek()
		# Check that it's not already defined in the **current** scope
		if current_scope.exists(name):
			raise Exception('The name {} is already defined'.format(name))
		func = Function(name, current_scope)
		current_scope.insert(func)
		self._current_func = func
		self._func_returned = False
		self.ScopeStack.push(func.varsTable)

	def procedure_add_params(self, params):
		'''Add the total params to the current function'''
		debug('procedure_add_params')
		for param in params:
			self.procedure_add_param(param['type'], param['id'])

	def procedure_add_param(self, dtype: str, pname: str):
		'''Call function.add_param()'''
		debug('procedure_add_param')

		assert self._current_func is not None

		current_scope = self.ScopeStack.peek()

		if current_scope.exists(pname):
			raise Exception('Redefinition of parameter {} in function signature'.format(pname))

		data_type = DType(dtype)
		address = current_scope.memory.next_address(data_type)
		var = Variable(pname, data_type, address)
		self._current_func.add_param(var)


	def procedure_mark_start(self):
		'''Mark the current quadruple counter as the start of this function'''
		debug('procedure_mark_start')
		self._current_func.start_pos = len(self.quads)

	def procedure_set_type(self, dtype):
		'''Set the return type of this function'''
		self._current_func.update_type(DType(dtype))

	def procedure_update_size(self):
		'''Once we know the number of temps, and local variables defined, we can update the size'''
		# TODO: define this
		debug('procedure_update_size')

	def procedure_return(self, returns_expresion = False):
		'''Generate a RETURN command'''
		debug('procedure_return')
		retval = None
		if returns_expresion:
			retval = self.OperandStack.pop()
			retval_type = self.TypeStack.pop()
			assert self._current_func.dtype == retval_type, 'Type mismatch: value returned does not match function signature.'
			self._func_returned = True
		else:
			assert self._current_func.is_void, 'Type mismatch: no value returned in non-void function.'
		self.quads.append((RETURN, retval.address, None, None))
		debug()

	def procedure_end(self):
		'''Generate an ENDPROC'''
		debug('procedure_end')
		# TODO: release the current vartable?
		# TODO: resolve any ERAs here
		# self.procedure_update_size()

		# if function is non-void, it returned something
		if not self._current_func.is_void and not self._func_returned:
			raise Exception("Non-void function must return a valid value.")

		self.quads.append((ENDPROC, None, None, None))
		debug(('FUNCTION TYPE:', self._current_func.dtype))

		self._current_func = None
		self.ScopeStack.pop()
		debug()

	# Function calls
	# --------------------------------------------
	def method_call_start(self, method_name):
		'''Verify that the procedure exists in DirFunc'''
		debug('method_call_start')

		if not self.GScope.exists(method_name):
			raise Exception('Method {} has not been defined'.format(method_name))
		call_proc = self.GScope.find(method_name) # Assumes all functions are defined in the global scope
		assert call_proc is not None
		self._call_proc = call_proc
		debug()


	def method_call_param_start(self):
		'''Start reading parameters for function call'''
		debug('method_call_param_start')
		debug("Start param k counter at 0")
		self._param_k = 0
		# TODO: add stack/list to keep track of these
		self.quads.append([ERA, 'SIZE', None, None]) # ActivationRecord expansion
		debug()

	def method_call_param(self):
		'''Get the kth parameter for the function call and perform semantic validations'''
		param = self.OperandStack.pop()
		param_type = self.TypeStack.pop()

		assert self._param_k is not None

		assert self._param_k < len(self._call_proc.param_list)

		kth_param_type = self._call_proc.param_list[self._param_k]

		# Check param_type
		# TODO: estos no **tienen** que ser iguales, solo compatibles
		assert param_type == kth_param_type # TODO: Aqui es donde entra el cubo semantico

		self.quads.append((PARAM, param.address, None, 'param{}'.format(self._param_k+1)))


	def method_call_param_end(self):
		'''Verify the last parameter points to null'''
		# i.e. we consumed all of the parameters
		# i.e. the parameter call matches the function definition
		# NOTE: when the argument list ends, the k pointer should be pointing at the last elem (len-1)
		assert self._param_k == len(self._call_proc.param_list)-1, "Parameter count mismatch."


	def method_call_end(self):
		'''Generate a GOSUB to take control flow the procedure'''
		debug('method_call_end')
		func = self._call_proc
		name = func.name
		init_address = func.start_pos
		is_void = func.is_void
		return_type = func.dtype

		self._call_proc = None
		self._param_k = None
		self.quads.append((GOSUB, name, None, init_address)) # TODO: migaja de pan pa saber donde voy a regresar

		# If the function returned something, we should assign it to a local temporary var
		if not is_void:
			result = self._Temporal.next(return_type)
			self.OperandStack.push(result)
			self.TypeStack.push(return_type)
			self.quads.append(('=', name, None, result.address))
		else: # TODO: test this thoroughly, not sure if this is going to work
			assert self.OperatorStack.peek() is not Operator.ASSIGN, 'Void function does not return anything. Cannot assign void value.'

		debug()

	def print_start(self):
		self._print = True
	def print_end(self):
		self._print = False
	def print_expression(self):
		debug("print_expression")
		assert self._print
		op = self.OperandStack.pop()
		self.TypeStack.pop()
		self.quads.append((Operator.PRINT.value, None, None, op.address))
		debug()

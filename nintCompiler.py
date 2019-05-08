# nintCompiler.py

import os
import sys
import pickle

# Hide traceback from exceptions:
# sys.tracebacklimit = None

from utils.Stack import Stack, OperandStack as OStack
from icg.Temp import Temp
from symbols.Operators import Operator, RELOPS
from symbols.Types import DType, mapType
from semantics.Cube import SemanticCube
from symbols.Env import Env # Symbol Table
from symbols.Function import Function
from symbols.Variable import Variable
from icg.CompMem import CompMem as Memory, MemType
import utils.utils as utils


GLOBAL = '__global'
# CALL   	t4 <- result
debug_mode = os.getenv('NINT_ENV', 'debug')

def debug(*args):
	if debug_mode == 'debug':
		print("[nint]:", end= ' ')
		for arg in args:
			print(arg, end = ' ')
		print()

def printable(item):
	'''Print blank instead of None'''
	return ' ' if item is None else str(item)


no_check = ['serialize', 'functionDirectory', '__check_main', '_init_special_functions']
special_functions = ['print']

class nintCompiler:
	"""Main class for the compiler"""
	def __init__(self):
		'''Set bookkeeping variables, initialize stacks and compiler memory'''
		super().__init__()
		self.OperatorStack = Stack()
		self.OperandStack = OStack()
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

		# Array helpers
		self._is_array = False
		self._array_access = None
		self._array_access_dim = 0

		# Generate the global scope and insert it into the functions directory
		# gscope = Function(GLOBAL, None, VOID)
		# self.FunDir.insert(gscope) # TODO: are objects passed by reference here?
		self.ScopeStack = Stack() # Keep track of the current Scope
		self.ScopeStack.push(self.GScope)

		# Temporal memory
		self._Temporal = Temp()
		self._TempStack = Stack()
		self._TempStack.push(self._Temporal)

		self._init_special_functions()

		self.quads = []

		# Add GOTO main
		self.quads.append([Operator.GOTO.value, None, None, None])


	def __getattribute__(self, attr):
		method = object.__getattribute__(self, attr)
		# if not method:
		if callable(method):
			name = method.__code__.co_name
			if name not in no_check and not name.startswith('procedure'):
				self.__check_main()
		return method

	def __check_main(self):
		'''Check statements to find the "main" program (the first non-scoped) statement'''
		if not self._found_main and self._current_func is None:
			self._found_main = True
			self.quads[0][3] = len(self.quads)

	def _init_special_functions(self):
		'''Add special functions to function directory'''
		scope = self.GScope
		funcs = [
			Function.make('len', DType.INT, [DType.VECTOR]),
			Function.make('ls', DType.VOID, []),
			Function.make('sum', DType.INT, [DType.VECTOR]),
			Function.make('table', DType.VOID, [DType.VECTOR]),
		]
		for func in funcs:
			scope.insert(func)

	def serialize(self, filename = "out.nint.bytecode"):
		'''Serialize the quads and the quads into an intermediate
		obj file to be read by the VM.'''
		const_map = dict()
		for const_dict in Memory.CONST_TABLE.values():
			for const, var in const_dict.items():
				const_map[var.address] = utils.parseVar(var)

		temp_counters = self._Temporal._counters
		global_counters = self.GScope.memory._counters
		fun_dir = self.functionDirectory()

		data = [self.quads, const_map, fun_dir, global_counters, temp_counters]

		with open(filename, 'wb') as f:
			pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

	def functionDirectory(self):
		'''Map the functions directory to only the stuff the VM needs'''
		result = dict()
		for func in self.GScope.functions:
			result.update({func.name: func.size_map})
		return result

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

		dtype = mapType(type_str)

		if self._is_array:
			scalar_type = dtype
			dtype = DType.VECTOR

		address = current_scope.memory.next_address(dtype)

		var = Variable(identifier, dtype, address)

		if self._is_array:
			var.scalar_type = scalar_type
			self._is_array = False # Reset this value

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
		'''Check relational operators'''
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
		result_type = SemanticCube.check(operator, left_type, right_type)
		# Relational operators *always* return a boolean
		assert result_type is DType.BOOL
		result = self._TempStack.peek().next(result_type)
		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))
		self.OperandStack.push(result)
		self.TypeStack.push(result_type)
		debug()

	def check_and(self):
		'''Checks if the next operator in the stack is an and'''
		debug("check_and")
		top = self.OperatorStack.peek()
		debug('top: {}'.format(top))
		if top is not Operator.AND:
			return
		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug((operator, left_type, right_type))
		result_type = SemanticCube.check(operator, left_type, right_type)
		# Relational operators *always* return a boolean
		assert result_type is DType.BOOL
		result = self._TempStack.peek().next(result_type)
		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))
		self.OperandStack.push(result)
		self.TypeStack.push(result_type)
		debug()

	def check_or(self):
		'''Checks if the next operator in the stack is an or'''
		debug("check_or")
		top = self.OperatorStack.peek()
		debug('top: {}'.format(top))
		if top is not Operator.OR:
			return
		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug((operator, left_type, right_type))
		result_type = SemanticCube.check(operator, left_type, right_type)
		# Relational operators *always* return a boolean
		assert result_type is DType.BOOL
		result = self._TempStack.peek().next(result_type)
		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))
		self.OperandStack.push(result)
		self.TypeStack.push(result_type)
		debug()

	def check_eqop(self):
		'''Checks if the next operator in the stack is an equality (==) or (!=)'''
		debug("check_eqop")
		# TODO: implement this
		top = self.OperatorStack.peek()
		if top is not Operator.EQUAL and top is not Operator.NEQ:
			return
		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug((operator, left_type, right_type))
		result_type = DType.BOOL
		# result_type = SemanticCube.check(operator, left_type, right_type)
		# TODO: rn we allow comparison of everything vs everything, is this correct?
		# TODO: what if we compare a function name to a variable? (e.g. uno == 2)
		result = self._TempStack.peek().next(result_type)
		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))
		self.OperandStack.push(result)
		self.TypeStack.push(result_type)

		debug()

	def check_addsub(self):
		'''Check if the next operator is a + or -'''
		debug('check_addsub')
		top = self.OperatorStack.peek()

		if not (top == Operator.ADD or top == Operator.SUB):
			return

		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug((operator, left_operand.name, right_operand.name))

		result_type = SemanticCube.check(operator, left_type, right_type)
		result = self._TempStack.peek().next(result_type)
		self.OperandStack.push(result)
		self.TypeStack.push(result_type)

		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))

		debug()

	def check_multdiv(self):
		'''Check if the next operator is a * or /'''
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
		result = self._TempStack.peek().next(result_type)
		self.OperandStack.push(result)
		self.TypeStack.push(result_type)

		debug("Adds quad")
		self.quads.append((operator.value, left_operand.address, right_operand.address, result.address))

		debug()

	# If-Else
	# --------------------------------------------
	def ifelse_start_jump(self):
		'''Denote where the if block starts to generate the jumping GOTOF'''
		debug("ifelse_start_jump")
		expression_type = self.TypeStack.pop()
		if expression_type != DType.BOOL:
			raise Exception("Type mismatch on line {}".format('SOMELINE TODO FIX THIS')); # TODO: maybe make a static function for this?
		result = self.OperandStack.pop()
		self.quads.append([Operator.GOTOF.value, result.address, None, None])
		self.JumpStack.push(len(self.quads)-1) # TODO: definitely change this. There has to be a better way to do this
		debug()

	def ifelse_end_jump(self):
		'''Fill in the pending condition jump for the IF statement
		once we know where to jump'''
		debug("ifelse_end_jump")
		counter = len(self.quads) # TODO: change this
		debug('counter: {}'.format(counter))
		self.fill(self.JumpStack.pop(), counter)
		debug()

	def fill(self, pending_jump_pos, jump_location):
		'''Fill a pending jump quad'''
		debug("fill")
		self.quads[pending_jump_pos][3] = jump_location # TODO: definitely make a class for this

	def ifelse_start_else(self):
		'''Store jumps for else statement in jump stack. Add GOTO quad'''
		debug("ifelse_start_else")
		debug("ADD ELSE QUAD GOTO")
		self.quads.append([Operator.GOTO.value, None, None, None])

		# Fill the false condition jump of the `if`
		if_false_jump = self.JumpStack.pop()
		counter = len(self.quads) # TODO: counter
		self.JumpStack.push(counter-1)
		self.fill(if_false_jump, counter)


	def assignment_quad(self):
		'''Generate the assignment quadruple making appropriate semantic checks'''
		debug("assignment_quad")
		operator = self.OperatorStack.pop()

		assert operator is Operator.ASSIGN

		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop(True)
		left_type = self.TypeStack.pop()

		debug("<{}> = <{}>".format(left_type, right_type))

		# TODO: probably change this
		# TODO: these don't need to be *exactly* the same, they just need to be compatible
		# example: float a = 10
		# assert right_type == left_type, "Type mismatch: assignment does not match"
		SemanticCube.check(operator, left_type, right_type)

		if left_type is DType.VECTOR:
			assert left_operand.scalar_type == right_operand.scalar_type, "Vector types do not match"
			# Also check the length if we have it
			if left_operand.dim1 is not None and right_operand.dim1 is not None:
				assert left_operand.dim1 == right_operand.dim1, "Subset vectors must be of same size"
		# else:


		left_operand.has_value = True
		self.quads.append((operator.value, right_operand.address, None, left_operand.address))
		self._is_array = False

		debug()


	# While
	# --------------------------------------------
	def while_condition_start(self):
		'''Store where the while condition starts to jump for reevaluation'''
		debug("while_condition_start")
		counter = len(self.quads) # TODO: counter
		self.JumpStack.push(counter)


	def while_block_start(self):
		'''Store where the while block starts and generate the GOTOF for the condition'''
		debug("while_block_start")
		expression_type = self.TypeStack.pop()
		if expression_type != DType.BOOL:
			raise Exception("Type mismatch on line {}".format("SOMELINE FIX THIS TODO"))
		result = self.OperandStack.pop()
		debug("ADD QUAD: while block_start GOTOF")
		self.quads.append([Operator.GOTOF.value, result.address, None, None])
		counter = len(self.quads)
		self.JumpStack.push(counter - 1) # TODO: counter


	def while_end(self):
		'''Once we know where the while ends, GOTO the start of condition'''
		debug("while_end")

		pending_while_end_jump = self.JumpStack.pop()
		return_pos = self.JumpStack.pop()

		debug("ADD QUAD: while_end GOTO return")
		self.quads.append([Operator.GOTO.value, None, None, return_pos])

		counter = len(self.quads) # TODO: change this
		self.fill(pending_while_end_jump, counter)


	# Function definitions
	# --------------------------------------------
	def procedure_start(self, name: str):
		'''Insert procedure name into dirfunc table, verify semantics'''
		debug('procedure_start')
		current_scope = self.ScopeStack.peek()
		# Check that it's not already defined in the **current** scope
		if current_scope.exists(name) or name in special_functions:
			raise Exception('The name {} is already defined'.format(name))
		func = Function(name, current_scope)
		current_scope.insert(func)
		self._current_func = func
		self._func_returned = False
		self.ScopeStack.push(func.varsTable)
		self._TempStack.push(func.varsTable.memory)

	def procedure_add_params(self, params):
		'''Add the total params to the current function'''
		debug('procedure_add_params')
		for param in params:
			self.procedure_add_param(param['type'], param['id'])

	def procedure_add_param(self, type_str: str, pname: str):
		'''Call function.add_param() to add the appropriate params to the function'''
		debug('procedure_add_param')

		assert self._current_func is not None

		current_scope = self.ScopeStack.peek()

		if current_scope.exists(pname):
			raise Exception('Redefinition of parameter {} in function signature'.format(pname))

		data_type = mapType(type_str)
		is_vector = type_str.endswith('[]')
		if is_vector:
			scalar_type = data_type
			data_type = DType.VECTOR
		address = current_scope.memory.next_address(data_type)
		var = Variable(pname, data_type, address)
		if is_vector:
			var.scalar_type = scalar_type
		var.has_value = True
		self._current_func.add_param(var)


	def procedure_mark_start(self):
		'''Mark the current quadruple counter as the start of this function'''
		debug('procedure_mark_start')
		self._current_func.start_pos = len(self.quads)

	def procedure_set_type(self, type_str: str):
		'''Set the return type of this function'''
		self._current_func.update_type(mapType(type_str))

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
			retval = retval.address
		else:
			assert self._current_func.is_void, 'Type mismatch: no value returned in non-void function.'
		self.quads.append((Operator.RETURN.value, retval, None, None))
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

		self.quads.append((Operator.ENDPROC.value, None, None, None))
		debug(('FUNCTION TYPE:', self._current_func.dtype))

		self._current_func = None
		self.ScopeStack.pop()
		self._TempStack.pop()
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
		fname = self._call_proc.name
		# TODO: add stack/list to keep track of these
		self.quads.append([Operator.ERA.value, fname, None, None]) # ActivationRecord expansion
		debug()

	def method_call_param(self):
		'''Get the kth parameter for the function call and perform semantic validations'''
		param = self.OperandStack.pop()
		param_type = self.TypeStack.pop()

		assert self._param_k is not None

		assert self._param_k < len(self._call_proc.param_list)

		kth_param = self._call_proc.param_list[self._param_k]
		kth_param_type = kth_param.dtype


		# Check param_type
		# TODO: estos no **tienen** que ser iguales, solo compatibles
		assert param_type == kth_param_type # TODO: Aqui es donde entra el cubo semantico

		self.quads.append((Operator.PARAM.value, param.address, None, kth_param.address))


	def method_call_param_end(self):
		'''Verify the last parameter points to null'''
		# i.e. we consumed all of the parameters
		# i.e. the parameter call matches the function definition
		# NOTE: when the argument list ends, the k pointer should be pointing at the last elem (len-1)
		arglength = len(self._call_proc.param_list)
		if arglength == 0:
			assert self._param_k == 0, "Parameter count mismatch."
		else:
			assert self._param_k == arglength-1, "Parameter count mismatch."


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
		self.quads.append((Operator.GOSUB.value, name, None, init_address)) # TODO: migaja de pan pa saber donde voy a regresar

		# If the function returned something, we should assign it to a local temporary var
		if not is_void:
			result = self._TempStack.peek().next(return_type)
			self.OperandStack.push(result)
			self.TypeStack.push(return_type)
			self.quads.append(('=', name, None, result.address))
		else: # TODO: test this thoroughly, not sure if this is going to work
			assert self.OperatorStack.peek() is not Operator.ASSIGN, 'Void function does not return anything. Cannot assign void value.'

		debug()


	# Vectors
	# --------------------------------------------
	def array_declaration(self):
		'''Helper method for generating array related quads'''
		self._is_array = True

	def array_decl_end(self):
		self._is_array = False

	def array_start(self):
		'''Mark the beginning of an array definition. Add it to varstable and set appropriate types.
		Generate a VECTOR quad. Add this quad to the jumpstack to fill the size of the vector'''
		self.JumpStack.push(len(self.quads)) # Return here to store the length
		var = self._TempStack.peek().next(DType.VECTOR)
		var.dim1 = 0
		self.OperandStack.push(var)
		self.TypeStack.push(DType.VECTOR)
		self.quads.append([Operator.VECTOR.value, None, None, None])

	def array_elem(self):
		'''Add an array element to the current array. Check for consistent types.
		Generate a PUSH quad'''
		elem_type = self.TypeStack.pop()
		elem = self.OperandStack.pop()
		array = self.OperandStack.peek()
		if array.dim1 == 0:
			# Set the type for this array if this is the first element
			array.scalar_type = elem_type
		else:
			assert array.scalar_type == elem_type, "Type mismatch: Each element in the array must be of same type."
		array.dim1 += 1
		self.quads.append((Operator.PUSH.value, None, None, elem.address))

	def array_end(self):
		'''Get the full size of the array definition and generate an ENDVECTOR.
		Fill the corresponding VECTOR quad with the full size'''
		# Resolve size
		vec_pos = self.JumpStack.pop()
		array = self.OperandStack.peek()
		self.quads[vec_pos][3] = array.dim1
		self.quads.append((Operator.ENDVECTOR.value, None, None, array.address))

	# Array access
	def check_array(self, array_name: str):
		'''Start an array subsetting or access. Checks that the name exists and it is an array'''
		current_scope = self.ScopeStack.peek()
		array = current_scope.get(array_name)
		assert array is not None, "Array {} has not been declared."
		assert array.dtype is DType.VECTOR, "Object {} is not a vector.".format(array_name)
		self._array_access = array

	def array_access_start(self):
		'''Generate a SUBSET quad to start subsetting the array.'''
		array = self._array_access
		self.quads.append((Operator.SUBSET.value, None, None, array.address))

	def array_access_expression(self):
		'''Add the current expression as an element of the list subsetting the current array.
		Check that the expression is of type INT. Generates a DIM quad'''
		pos = self.OperandStack.pop()
		pos_type = self.TypeStack.pop()
		assert pos_type is DType.INT, "Vector subset expression must be an integer."
		self._array_access_dim += 1
		# TODO: check that all expressions are different (we don't want [1,1])
		self.quads.append((Operator.DIM.value, None, None, pos.address))

	def array_access_end(self):
		'''End the array subsetting. Check whether subsetting multiple or 1 item and set the
		return type accordingly. Generate a pointer address to use when accesing the subsetted elements.
		Store this pointer address in an ENDSUBSET quad.'''
		array = self._array_access
		result_is_scalar = self._array_access_dim == 1

		result = self._TempStack.peek().next(DType.POINTER)

		dtype = array.scalar_type if result_is_scalar else DType.VECTOR
		result.pointer_type = dtype

		if not result_is_scalar:
			result.scalar_type = array.scalar_type
			result.dim1 = self._array_access_dim

		self.OperandStack.push(result)
		self.TypeStack.push(dtype)

		self.quads.append((Operator.ENDSUBSET.value, None, None, result.address))
		self._array_access_dim = 0
		self._array_access = None




	# Special functions
	# --------------------------------------------
	def print_start(self):
		self._print = True
	def print_end(self):
		self._print = False
	def print_expression(self):
		'''Generate a print quad'''
		debug("print_expression")
		assert self._print # TODO: remove this
		op = self.OperandStack.pop()
		self.TypeStack.pop()
		self.quads.append((Operator.PRINT.value, None, None, op.address))
		debug()


	def paren_open(self):
		'''Add a fake bottom the operator stack'''
		self.OperatorStack.push(Operator.FAKE)

	def paren_close(self):
		'''Pop the fake bottom from the operator stack'''
		self.OperatorStack.pop()




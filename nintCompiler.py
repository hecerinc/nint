# nintCompiler.py

import os

from utils.Stack import Stack
from icg.Temp import Temp
from symbols.Operators import RELOPS
from symbols.Operators import Operator
from symbols.Types import DType
from semantics.Cube import SemanticCube
from icg.Env import Env # Symbol Table

# TODO: probs should remove this from here
GOTO = 'goto'
GOTOF = 'gotoF'
GOTOV = 'gotoV'
ENDPROC = 'ENDPROC'

debug_mode = os.getenv('NINT_ENV', 'debug')

def debug(*args):
	if debug_mode == 'debug':
		for arg in args:
			print("D: {}".format(arg))
		if len(args) == 0:
			print()

def printable(item):
	return ' ' if item is None else str(item)

class nintCompiler:
	"""docstring for nintCompiler"""
	def __init__(self):
		super().__init__()
		self.OperatorStack = Stack()
		self.OperandStack = Stack()
		self.TypeStack = Stack()
		self.JumpStack = Stack()
		self.FunDir = Env()
		self.quads = []

	def intercode(self):
		'''Print the quadruples'''
		for i, quad in enumerate(self.quads):
			print("{})".format(i), '\t'.join(map(printable, quad)))

	def add_var(self, token):
		debug("add_var")
		self.OperandStack.push(token)
		self.TypeStack.push('var') # TODO: get actual dtype
		debug()

	def add_constant(self, token, dtype: DType):
		debug("Operand.push({})".format(token))
		debug("TypeStack.push({})".format(dtype))
		debug()
		self.OperandStack.push(token)
		self.TypeStack.push(dtype)

	def add_operator(self, op):
		''' Adds operator op to the OperatorStack'''
		debug("add_operator")
		debug("Operator.push({})".format(op))
		operator = Operator(op)
		self.OperatorStack.push(operator) # TODO: change this to an enum

	# TODO: refactor the check_* functions
	def check_relop(self):
		debug("check_relop")
		top = self.OperatorStack.peek()
		if top not in Operators.RELOPS:
			return
		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug(operator, left_type, right_type) # TODO: remove
		result = Temp.getTmp().toString()
		debug("Adds quad")
		self.quads.append((operator.value, left_operand, right_operand, result))
		self.OperandStack.push(result)
		# Relational operators *always* return a boolean
		self.TypeStack.push(DType.BOOL)
		debug()


	def check_addsub(self):
		debug('check_addsub')
		top = self.OperatorStack.peek()
		debug(top)

		if not (top == Operator.ADD or top == Operator.SUB):
			return

		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug(operator, left_type, right_type) # TODO: remove

		result = Temp.getTmp().toString()
		self.OperandStack.push(result)
		self.TypeStack.push(SemanticCube.check(operator, left_type, right_type))

		debug("Adds quad")
		self.quads.append((operator.value, left_operand, right_operand, result))

		debug()

	def check_multdiv(self):
		debug('check_multdiv')
		top = self.OperatorStack.peek()
		debug(top)

		if not (top == Operator.MULT or top == Operator.DIV):
			return

		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug(operator, left_type, right_type) # TODO: remove

		result = Temp.getTmp().toString()
		self.OperandStack.push(result)
		self.TypeStack.push(SemanticCube.check(operator, left_type, right_type))

		debug("Adds quad")
		self.quads.append((operator.value, left_operand, right_operand, result))

		debug()

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
		debug(counter)
		self.fill(self.JumpStack.pop(), counter)

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

		assert operator == '='

		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()

		debug("<{}> = <{}>".format(left_type, right_type))

		# TODO: probably change this
		# TODO: what if left type is a new decl/assignment?
		assert right_type == left_type, "Type mismatch: assignment does not match"

		self.quads.append((operator.value, right_operand, None, left_operand))

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
	def procedure_begin(self):
		'''Insert procedure name into dirfunc table, verify semantics'''
		pass
	def procedure_add_param(self):
		'''Call function.add_param()'''
		pass
	def procedure_mark_start(self):
		'''Mark the current quadruple counter as the start of this function'''
		pass
	def procedure_update_size(self):
		'''Once we know the number of temps, and local variables defined, we can update the size and resolve any ERAs'''
		pass
	def procedure_returns(self):
		'''Generate a RETURN command'''
		pass
	def procedure_end(self):
		'''Generate an ENDPROC'''
		# TODO: release the current vartable?
		self.quads.append((ENDPROC, None, None, None))


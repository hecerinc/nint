# nintCompiler.py

import os

from utils.Stack import Stack
from icg.Temp import Temp
import symbols.Operators as Operators
import symbols.Types as Types

GOTO = 'goto'
GOTOF = 'gotoF'

debug_mode = os.getenv('NINT_ENV', 'debug')

def debug(*args):
	if debug_mode == 'debug':
		for arg in args:
			print("D: {}".format(arg))
		if len(args) == 0:
			print()

def printable(item):
	if item is None:
		return ' '
	return str(item)

class nintCompiler:
	"""docstring for nintCompiler"""
	def __init__(self):
		super().__init__()
		self.OperatorStack = Stack()
		self.OperandStack = Stack()
		self.TypeStack = Stack()
		self.JumpStack = Stack()
		self.quads = []

	def intercode(self):
		for i, quad in enumerate(self.quads):
			print("{})".format(i), '\t'.join(map(printable, quad)))

	def add_constant(self, token, dtype):
		debug("Operand.push({})".format(token))
		debug("TypeStack.push({})".format(dtype))
		debug()
		self.OperandStack.push(token)
		self.TypeStack.push(dtype)

	def add_operator(self, op):
		debug("Operator.push({})".format(op))
		self.OperatorStack.push(op)

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
		self.quads.append((operator, left_operand, right_operand, result))
		self.OperandStack.push(result)
		self.TypeStack.push(Types.BOOL)
		debug()


	def check_addsub(self):
		debug('check_addsub')
		top = self.OperatorStack.peek()
		debug(top)
		if not (top == '+' or top == '-'):
			return
		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug(operator, left_type, right_type) # TODO: remove
		result = Temp.getTmp().toString()
		debug("Adds quad")
		self.quads.append((operator, left_operand, right_operand, result))
		self.OperandStack.push(result)
		self.TypeStack.push('temporal')
		debug()

	def check_multdiv(self):
		debug('check_multdiv')
		top = self.OperatorStack.peek()
		debug(top)
		if not (top == '*' or top == '/'):
			return
		right_operand = self.OperandStack.pop()
		right_type = self.TypeStack.pop()
		left_operand = self.OperandStack.pop()
		left_type = self.TypeStack.pop()
		operator = self.OperatorStack.pop()
		debug(operator, left_type, right_type) # TODO: remove
		result = Temp.getTmp().toString()
		debug("Adds quad")
		self.quads.append((operator, left_operand, right_operand, result))
		self.OperandStack.push(result)
		self.TypeStack.push('temporal') # TODO: change this
		debug()

	def ifelse_start_jump(self):
		debug("ifelse_start_jump")
		expression_type = self.TypeStack.pop()
		debug(expression_type)
		if expression_type != Types.BOOL:
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
		counter = len(self.quads)
		self.JumpStack.push(counter-1)
		self.fill(if_false_jump, counter)



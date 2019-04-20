# nintCompiler.py

import os

from utils.Stack import Stack
from icg.Temp import Temp
import symbols.Operators as Operators


debug_mode = os.getenv('NINT_ENV', 'debug')

def debug(*args):
	if debug_mode == 'debug':
		for arg in args:
			print("D: {}".format(arg))
		if len(args) == 0:
			print()

class nintCompiler:
	"""docstring for nintCompiler"""
	def __init__(self):
		super().__init__()
		self.OperatorStack = Stack()
		self.OperandStack = Stack()
		self.TypeStack = Stack()
		self.quads = []

	def intercode(self):
		for quad in self.quads:
			print(' '.join(map(str, quad)))

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
		self.TypeStack.push('temporal')
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
		self.TypeStack.push('temporal')
		debug()

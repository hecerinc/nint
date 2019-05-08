# Stack.py
# Taken from http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaStackinPython.html

import sys
sys.path.append("C:/dev/compiler")

from symbols.Variable import Variable

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		if self.isEmpty():
			return None
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


class OperandStack(Stack):
	def __init__(self):
		super().__init__()
	def pop(self, is_assignment: bool = False):
		if is_assignment:
			return super().pop()
		var = self.peek()
		if isinstance(var, Variable) and not var.has_value:
			raise Exception("Attempt to use uninitialized variable.")
		return super().pop()

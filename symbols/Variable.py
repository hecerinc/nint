# Variable.py

from .Symbol import Symbol

class Variable(Symbol):
	"""docstring for Variable"""
	def __init__(self, name, dtype):
		super().__init__(name, dtype)


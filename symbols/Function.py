# Function.py

from .Symbol import Symbol
from .Env import Env


class Function(Symbol):
	"""docstring for Function"""
	def __init__(self, name, dtype, varsTable: Env):
		super().__init__(name, dtype)
		self._varsTable = varsTable
		# TODO: initialize everything


	@property
	def varsTable(self) -> Env:
		return self._varsTable

	@property
	def size(self):
		return self._size

	@property
	def start_pos(self):
		return self._start_pos

	@property
	def param_list(self):
		''''A list of parameter types in the order in which they were defined'''
		# TODO: do we need the names? we can use tuples
		return self._param_list


	def update_type(self, dtype):
		'''Update the type of the function'''
		self._dtype = dtype

	def add_param(self, variable: Variable):
		''' Add a parameter to the function directory'''
		# This implies:
		#   1. Adding it to the varTable
		#   2. Adding its type to the params list
		#   3. Adjust the function size
		raise Exception('Not implemented')



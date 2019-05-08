# Function.py

from .Symbol import Symbol
from .Variable import Variable
from .Env import Env
from .Types import DType



class Function(Symbol):
	"""docstring for Function"""
	def __init__(self, name, scope: Env = None, dtype = None):
		super().__init__(name, dtype)
		self._varsTable = Env(scope)
		self._temp_counter = 0
		self._start_pos = 0
		self._param_list = []

	@property
	def varsTable(self) -> Env:
		return self._varsTable

	@property
	def size_map(self):
		return self._varsTable.memory._counters

	@property
	def start_pos(self):
		return self._start_pos

	@start_pos.setter
	def start_pos(self, pos):
		self._start_pos = pos

	@property
	def param_list(self):
		''''A list of parameter types in the order in which they were defined'''
		# TODO: do we need the names? we can use tuples
		return self._param_list

	@property
	def is_void(self):
		return self.dtype == DType.VOID


	def update_type(self, dtype):
		'''Update the type of the function'''
		self._dtype = dtype

	def add_param(self, variable: Variable):
		''' Add a parameter to the function directory'''
		# This implies:
		#   1. Adding it to the varTable
		#   2. Adding its type to the params list
		#   3. Adjust the function size
		self._varsTable.insert(variable)
		self._param_list.append(variable)
		self._temp_counter += 1


	@staticmethod
	def make(name, return_type, param_list):
		func = Function(name, None, return_type)
		for param in param_list:
			var = func.varsTable.memory.next(param)
			func.add_param(var)
		return func





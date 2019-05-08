# Stackframe.py
from .Memory import Memory

class StackFrame(Memory):
	"""Subset of memory to represent additional info for stack frame"""
	def __init__(self, function_name, var_counts):
		super().__init__(var_counts)
		self._function_name = function_name
		self._param_list = []

	@property
	def return_addr(self):
		return self._return_addr

	@property
	def function_name(self):
		return self._function_name

	@property
	def param_list(self):
		return self._param_list


	def push_param(self, addr):
		self._param_list.append(addr)

	def set_return_addr(self, addr):
		self._return_addr = addr


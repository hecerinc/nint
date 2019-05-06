# Variable.py

from .Symbol import Symbol
from .Types import DType

import os
name_mode = os.getenv('NINT_ADDRESS', 'true')


class Variable(Symbol):
	"""docstring for Variable"""
	def __init__(self, name: str, dtype, address, value = None):
		super().__init__(name, dtype)
		# This address will be a function of the type and which memory
		self._address = address
		self._value = value
		self._scalar_type = None
		self._dim1 = None

	@property
	def address(self):
		if name_mode == 'true':
			return self._address
		else:
			return self.name # For debugging purposes

	@property
	def value(self):
		'''Used for consts'''
		return self._value

	@property
	def scalar_type(self):
		return self._scalar_type

	@property
	def dim1(self):
		return self._dim1

	@dim1.setter
	def dim1(self, size):
		self._dim1 = size

	@scalar_type.setter
	def scalar_type(self, st: DType):
		self._scalar_type = st


	def __str__(self):
		return "{{name: {}, type: {}, address: {}, scalar_type: {}}}".format(self.name, self.dtype, self.address, self.scalar_type)


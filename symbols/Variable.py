# Variable.py

from .Symbol import Symbol
from .Types import DType

import os
name_mode = os.getenv('NINT_ADDRESS', 'true')


class Variable(Symbol):
	"""docstring for Variable"""
	def __init__(self, name: str, dtype, address, value = None, st = None):
		super().__init__(name, dtype)
		# This address will be a function of the type and which memory
		self._address = address
		self._value = value
		self._scalar_type = st
		self._dim1 = None
		self._dim2 = None
		self._pointer_type = None
		self._has_value = False

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

	@property
	def dim2(self):
		return self._dim2

	@dim2.setter
	def dim2(self, size):
		self._dim2 = size

	@scalar_type.setter
	def scalar_type(self, st: DType):
		self._scalar_type = st


	@property
	def pointer_type(self):
		return self._pointer_type

	@property
	def has_value(self):
		return self._has_value

	@has_value.setter
	def has_value(self, hasvalue):
		self._has_value = hasvalue

	@pointer_type.setter
	def pointer_type(self, pt):
		self._pointer_type = pt

	def __str__(self):
		return "{{name: {}, type: {}, address: {}, scalar_type: {}}}".format(self.name, self.dtype, self.address, self.scalar_type)


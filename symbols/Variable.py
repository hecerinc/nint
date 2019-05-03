# Variable.py

from .Symbol import Symbol

import os
name_mode = os.getenv('NINT_ADDRESS', 'true')


class Variable(Symbol):
	"""docstring for Variable"""
	def __init__(self, name: str, dtype, address, value = None):
		super().__init__(name, dtype)
		# This address will be a function of the type and which memory
		self._address = address
		self._value = value

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




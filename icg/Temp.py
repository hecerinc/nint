# Temp.py

import sys
sys.path.append("C:/dev/compiler")

from .CompMem import CompMem as Memory
from .CompMem import MemType
from symbols.Types import DType
from symbols.Variable import Variable

class Temp(Memory):
	""" AVAIL to get the next temporary """

	def __init__(self, mem_type = MemType.TEMP):
		super().__init__(mem_type)

		# Only for debugging purposes (to set a readable var name)
		self._tmp_counter = 0

	# @staticmethod
	def next(self, dtype: DType) -> Variable:
		'''Generate a new temp variable of type dtype'''
		self._tmp_counter += 1
		address = self.next_address(dtype)
		var =  Variable('t{}'.format(self._tmp_counter), dtype, address)
		var.has_value = True
		return var

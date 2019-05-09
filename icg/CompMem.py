# CompMem.py

import sys
sys.path.append("C:/dev/compiler")

from enum import Enum
from symbols.Types import DType
from symbols.Variable import Variable

MemType = Enum('MEMTYPE', 'GLOBAL LOCAL CONST TEMP')

class CompMem:
	"""Memory management for compilation"""

	# TODO: maybe we don't need this anymore now that the DType enum is int-valued
	VAR_TYPE_IDS = {
		DType.INT: 1,
		DType.BOOL: 2,
		DType.STRING: 3,
		DType.FLOAT: 4,
		DType.VECTOR: 5,
		DType.POINTER: 6,
		DType.DF: 7,
	}

	CONST_TABLE = {
		DType.INT: dict(),
		DType.BOOL: dict(),
		DType.STRING: dict(),
		DType.FLOAT: dict(),
	}


	def __init__(self, memType = MemType.LOCAL):
		super().__init__()
		self._memtype = memType
		self._tmpcount = 0

		'''Counters for each data type. Used in VM'''
		self._counters = {
			DType.INT: 0,
			DType.BOOL: 0,
			DType.STRING: 0,
			DType.FLOAT: 0,
			DType.VECTOR: 0,
			DType.POINTER: 0,
			DType.DF: 0,
		}

	def next_address(self, dtype: DType) -> str:
		'''Get the next available address for the data type'''
		# Check what type of memory this is (global, temporal, constant, local)
		memtype_id = self._memtype.value


		assert dtype in self._counters

		# Check the data type
		datatype_id = CompMem.VAR_TYPE_IDS[dtype]

		self._counters[dtype] += 1
		address = self._counters[dtype]

		full_address = "{}{}{}".format(memtype_id, datatype_id, address)

		return full_address

	def next(self, dtype: DType) -> Variable:
		# TODO: if we arleady have this here, what is 'Temp.py' used for?
		self._tmpcount += 1
		addr = self.next_address(dtype)
		var =  Variable('t{}'.format(self._tmpcount), dtype, addr)
		var.has_value = True
		return var


	@staticmethod
	def constant(dtype: DType, value) -> Variable:
		''' Inserts a constant into the const table and returns the variable.
		If the constant already exists, it will return the stored variable'''
		const_bucket = CompMem.CONST_TABLE.get(dtype)
		var = const_bucket.get(value, None)
		if var is None:
			# insert it into the table

			address = len(const_bucket) + 1
			datatype_id = CompMem.VAR_TYPE_IDS[dtype]
			memtype_id = MemType.CONST.value
			full_address = "{}{}{}".format(memtype_id, datatype_id, address)
			var = Variable(value, dtype, full_address, value)
			var.has_value = True
			const_bucket.update({value: var})

		return var

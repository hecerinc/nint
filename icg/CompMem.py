# CompMem.py

import sys
sys.path.append("C:/dev/compiler")

from enum import Enum
from symbols.Types import DType
from symbols.Variable import Variable

MemType = Enum('MEMTYPE', 'GLOBAL LOCAL CONST TEMP')

class CompMem:
	"""docstring for CompMem"""

	VAR_TYPE_IDS = {
		DType.INT: 1,
		DType.BOOL: 2,
		DType.STRING: 3,
		DType.FLOAT: 4,
		'Other': 5
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

		self._counters = {
			DType.INT: 0,
			DType.BOOL: 0,
			DType.STRING: 0,
			DType.FLOAT: 0,
			'Other': 0
		}


	def next_address(self, dtype: DType) -> str:
		# Check what type of memory this is (global, temporal, constant, local)
		memtype_id = self._memtype.value

		# Check the data type
		datatype_id = CompMem.VAR_TYPE_IDS.get(dtype, CompMem.VAR_TYPE_IDS['Other'])

		assert dtype in self._counters

		self._counters[dtype] += 1
		address = self._counters[dtype]

		full_address = "{}{}{}".format(memtype_id, datatype_id, address)

		return full_address

	@staticmethod
	def constant(dtype: DType, value) -> Variable:
		''' Inserts a constant into the const table and returns the variable.
		If the constant already exists, it will return the stored variable'''
		const_bucket = CompMem.CONST_TABLE.get(dtype)
		var = const_bucket.get(value, None)
		if var is None:
			# insert it into the table

			address = len(const_bucket) + 1
			datatype_id = CompMem.VAR_TYPE_IDS.get(dtype, CompMem.VAR_TYPE_IDS['Other'])
			memtype_id = MemType.CONST.value
			full_address = "{}{}{}".format(memtype_id, datatype_id, address)
			var = Variable(value, dtype, full_address, value)
			const_bucket.update({value: var})

		return var




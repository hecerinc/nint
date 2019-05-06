# Memory.py

# Four types of memory

# - Global
# - Local
# - Temporal
# - Constants

import sys
sys.path.append("C:/dev/compiler")

from icg.CompMem import MemType
from symbols.Types import DType

# GLOBAL LOCAL CONST TEMP
# TODO: clean these functions
def is_constant(addr: str) -> bool:
	type_indicator = int(addr[0])
	memtype = MemType(type_indicator)
	return memtype is MemType.CONST

def is_temp(addr: str) -> bool:
	type_indicator = int(addr[0])
	memtype = MemType(type_indicator)
	return memtype is MemType.TEMP

def is_local(addr: str) -> bool:
	type_indicator = int(addr[0])
	memtype = MemType(type_indicator)
	return memtype is MemType.LOCAL

def is_global(addr: str) -> bool:
	type_indicator = int(addr[0])
	memtype = MemType(type_indicator)
	return memtype is MemType.GLOBAL



class Memory:
	"""The representation for the virtual memory for the virtual machine"""
	def __init__(self, var_count: dict):
		super().__init__()

		# TODO: get size of each bucket as parameter
		self._mem = {
			DType.INT: [None]*var_count[DType.INT],
			DType.BOOL: [None]*var_count[DType.BOOL],
			DType.STRING: [None]*var_count[DType.STRING],
			DType.FLOAT: [None]*var_count[DType.FLOAT],
			DType.VECTOR: [None]*var_count[DType.VECTOR]
		}

	def _parse_address(self, address):
		dtype_indicator = int(address[1])
		mapped_dtype = DType(dtype_indicator)
		mem_bucket = self._mem[mapped_dtype]
		real_address = int(address[2:])-1
		return (mem_bucket, real_address)

	def set_value(self, address, value):
		mem_bucket, real_address = self._parse_address(address)
		assert real_address < len(mem_bucket), ("Out of bounds address", address, "\n", self._mem)
		mem_bucket[real_address] = value

	def get_val(self, address):
		'''Get value from address'''
		bucket, real_address = self._parse_address(address)
		return bucket[real_address]


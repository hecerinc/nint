# Types.py

from enum import Enum, auto


class DType(Enum):
	"""Enum for data types"""
	INT = auto()
	BOOL = auto()
	STRING = auto()
	FLOAT = auto()
	VECTOR = auto()
	POINTER = auto()
	ERROR = auto()
	VOID = auto()


_typemap = {
	'int': DType.INT,
	'bool': DType.BOOL,
	'string': DType.STRING,
	'float': DType.FLOAT,
	'void': DType.VOID
}
def mapType(type_str: str):
	if type_str.endswith('[]'):
		type_str = type_str[:-2]
	return _typemap.get(type_str, DType.ERROR)

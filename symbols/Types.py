# Types.py

from enum import Enum, auto


class DType(Enum):
	"""Enum for data types"""
	INT = auto()
	BOOL = auto()
	STRING = auto()
	FLOAT = auto()
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
	return _typemap.get(type_str, DType.ERROR)

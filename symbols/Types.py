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
	DF = auto()
	ERROR = auto()
	VOID = auto()


_typemap = {
	'int': DType.INT,
	'bool': DType.BOOL,
	'string': DType.STRING,
	'float': DType.FLOAT,
	'data.frame': DType.DF,
	'void': DType.VOID,
}
def mapType(type_str: str):
	is_vector = False
	if type_str.endswith('[]'):
		is_vector = True
		type_str = type_str[:-2]
	mapped_type = _typemap.get(type_str, DType.ERROR)
	if is_vector:
		return DType.VECTOR, mapped_type
	else:
		return mapped_type, None

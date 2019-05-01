# Types.py

from enum import Enum, auto


class DType(Enum):
	"""Enum for data types"""
	BOOL = 'bool'
	ERROR = auto()
	FLOAT = 'float'
	INT = 'int'
	STRING = 'string'
	VOID = 'void'



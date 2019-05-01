# Types.py

from enum import Enum, auto


class DType(Enum):
	"""Enum for data types"""
	BOOL = auto()
	ERROR = auto()
	FLOAT = auto()
	INT = auto()
	STRING = auto()
	VOID = auto()

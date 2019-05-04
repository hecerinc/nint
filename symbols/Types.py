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

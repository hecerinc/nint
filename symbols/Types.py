# Types.py

from enum import Enum, auto


class DType(Enum):
	"""Enum for data types"""
	ERROR = auto()
	INT = auto()
	FLOAT = auto()
	BOOL = auto()
	STRING = auto()

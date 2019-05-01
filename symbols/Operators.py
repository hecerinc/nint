# Operators.py

from enum import Enum

RELOPS = ['<', '>', '<=', '>=']


class Operator(Enum):
	"""Enum for operator"""
	ASSIGN = '='
	ADD = '+'
	SUB = '-'
	MULT = '*'
	DIV = '/'


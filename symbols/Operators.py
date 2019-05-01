# Operators.py

from enum import Enum



class Operator(Enum):
	"""Enum for operator"""
	ASSIGN = '='
	ADD = '+'
	SUB = '-'
	MULT = '*'
	DIV = '/'
	LT = '<'
	LTE = '<='
	GT = '>'
	GTE = '>='

RELOPS = [Operator.GT, Operator.LT, Operator.LTE, Operator.GTE]

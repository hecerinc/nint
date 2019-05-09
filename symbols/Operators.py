# Operators.py

from enum import Enum



class Operator(Enum):
	"""Enum for operator"""
	FAKE = '('

	ASSIGN = '='
	ADD = '+'
	SUB = '-'
	MULT = '*'
	DIV = '/'
	LT = '<'
	LTE = '<='
	GT = '>'
	GTE = '>='
	EQUAL = '=='
	NEQ = '!='

	AND = '&&'
	OR = '||'


	GOTO = 'goto'
	GOTOF = 'gotoF'
	GOTOV = 'gotoV'

	# Functions:
	ENDPROC = 'ENDPROC'
	PARAM = 'PARAM'
	ERA = 'ERA'
	GOSUB = 'GOSUB'
	RETURN = 'RETURN'

	# Vectors
	VECTOR = 'VECTOR'
	PUSH = 'PUSH'
	ENDVECTOR = 'ENDVECTOR'
	DIM = 'DIM'
	SUBSET = 'SUBSET'
	ENDSUBSET = 'ENDSUBSET'

	DF = 'DATAFRAME'
	ENDF = 'ENDF'

	PRINT = 'print'


RELOPS = [Operator.GT, Operator.LT, Operator.LTE, Operator.GTE]

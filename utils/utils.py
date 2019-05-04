# utils.py

import sys
sys.path.append("C:/dev/compiler")

from symbols.Types import DType
from symbols.Variable import Variable

def parseVar(var: Variable):
	val = var.value
	if var.dtype == DType.STRING:
		val = val.strip("'").strip('"')
	elif var.dtype == DType.INT:
		val = int(val)
	else:
		val = None
	return val

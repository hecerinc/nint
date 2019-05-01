# semantics/Cube.py

import sys
sys.path.append("C:/dev/compiler")
from symbols.Types import DType
from symbols.Operators import Operator
import nintCompiler

class SemanticCube:
	"""Map of operators and operands to result type"""

	@staticmethod
	def check(operator, left_operand: DType, right_operand: DType) -> DType:
		result = SemanticCube._check(operator, left_operand, right_operand)
		nintCompiler.debug(operator, left_operand, right_operand)
		if result == DType.ERROR:
			raise Exception('Type mismatch: No baila mija con el señor', left_operand, right_operand)
		return result

	@staticmethod
	def _check(operator, left_operand: DType, right_operand: DType) -> DType:

		cube = {

			# INT
			# ---------------------------------------------------------------

			# Addition
			(Operator.ADD, DType.INT, DType.INT): DType.INT,
			(Operator.ADD, DType.INT, DType.FLOAT): DType.FLOAT,

			# Substraction
			(Operator.SUB, DType.INT, DType.INT): DType.INT,
			(Operator.SUB, DType.INT, DType.FLOAT): DType.FLOAT,

			# Multiplication
			(Operator.MULT, DType.INT, DType.INT): DType.INT,
			(Operator.MULT, DType.INT, DType.FLOAT): DType.FLOAT,

			# Division
			(Operator.DIV, DType.INT, DType.INT): DType.FLOAT,
			(Operator.DIV, DType.INT, DType.FLOAT): DType.FLOAT,


			# FLOAT
			# ---------------------------------------------------------------

			# Addition
			(Operator.ADD, DType.FLOAT, DType.FLOAT): DType.FLOAT,
			(Operator.ADD, DType.FLOAT, DType.INT): DType.FLOAT,

			# Substraction
			(Operator.SUB, DType.FLOAT, DType.FLOAT): DType.FLOAT,
			(Operator.SUB, DType.FLOAT, DType.INT): DType.FLOAT,

			# Multiplication
			(Operator.MULT, DType.FLOAT, DType.FLOAT): DType.FLOAT,
			(Operator.MULT, DType.FLOAT, DType.INT): DType.FLOAT,

			# Division
			(Operator.DIV, DType.FLOAT, DType.FLOAT): DType.FLOAT,
			(Operator.DIV, DType.FLOAT, DType.INT): DType.FLOAT,
		}

		return cube.get((operator, left_operand, right_operand), DType.ERROR)


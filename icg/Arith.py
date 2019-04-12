# Arith.py

from .Op import Op

class Arith(Op):
	"""docstring for Arith"""
	def __init__(self, token, x1: 'Expr', x2: 'Expr'):
		super().__init__(token, None)
		self._expr1 = x1
		self._expr2 = x2
		# TODO: Change this to a setter
		# TODO: enable types
		# dtype = Type.max(x1.type, x2.type)
		# if dtype is None:
		# 	raise Exception("Type mismatch on line {}".format(self.line))

	@property
	def expr1(self) -> 'Expr':
		return self._expr1

	@property
	def expr2(self) -> 'Expr':
		return self._expr2

	# @override
	def gen(self) -> 'Expr':
		return Arith(self.token, self.expr1.reduce(), self.expr2.reduce())

	def toString(self) -> str:
		return "{} {} {}".format(self.expr1.toString(), self.token, self.expr2.toString())

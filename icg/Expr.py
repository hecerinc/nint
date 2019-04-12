# Expr.py

class Expr(Node):
	"""docstring for Expr"""
	def __init__(self, token, dtype):
		super(Expr, self).__init__()
		self._token = token
		self._dtype = dtype

	@property
	def token(self):
		return self._token

	@property
	def dtype(self):
		return self._dtype

	# @overload
	def gen(self) -> Expr: # gen # Generate the three-address code for this expression
		""" TODO: Docstring for gen """
		return self

	# @overload
	def reduce(self) -> Expr:
		""" Returns a temporary variable (t#) or ID holding the value of the expression """
		return self

	def toString(self) -> str:
		return self.token.text # antlr4 way of getting the matched text for the string




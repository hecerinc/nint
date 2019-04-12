# Op.py

class Op(Expr):
	"""docstring for Op"""
	def __init__(self, token, dtype):
		super(Op, self).__init__(token, dtype)

	def reduce(self) -> Expr:
		x = self.gen()
		t = Temp(self.dtype)
		self.emit(t.toString() + " = " + x.toString())
		return t

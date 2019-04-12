# Op.py
from .Expr import Expr

class Temp():
	counter = 0
	@staticmethod
	def getTmp():
		Temp.counter = Temp.counter + 1
		return Temp("t{}".format(Temp.counter))
	"""docstring for Temp"""
	def __init__(self, token):
		super(Temp, self).__init__()
		self.token = token
	def toString(self):
		return self.token
class Op(Expr):
	"""docstring for Op"""
	def __init__(self, token, dtype):
		super().__init__(token, dtype)

	def reduce(self) -> Temp:
		x = self.gen()
		t = Temp.getTmp()
		# print('got here')
		self.emit(t.toString() + " = " + x.toString())
		return t

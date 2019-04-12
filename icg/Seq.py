# Seq.py
from .Stmt import Stmt

class Seq(Stmt):
	"""docstring for Seq"""
	def __init__(self, seq):
		super().__init__()
		if len(seq) == 0:
			self._s1 = None
			self._s2 = None
		else:
			self._s1 = seq[0]
			self._s2 = None if len(seq[1:]) == 0 else Seq(seq[1:])
	@property
	def s1(self) -> Stmt:
		return self._s1

	@property
	def s2(self) -> Stmt:
		return self._s2

	def gen(self):
		if self.s1 is None and self.s2 is None:
			return
		if self.s1 is None:
			# print("Only do the second one")
			self.emit(self.s2.gen().toString())
		elif self.s2 is None:
			# print("Only do the first one")
			# print(type(self.s1))
			self.emit(self.s1.gen().toString())
		else:
			# print("Do both")
			# print(type(self.s1))
			# print(type(self.s2))
			self.s1.gen()
			# self.emit(self.s1.gen().toString())
			# self.emit(self.s2.gen().toString())
			self.s2.gen()

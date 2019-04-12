# Node.py

class Node():
	"""docstring for Node"""
	def __init__(self, line: int = 1):
		self._line = line

	@property
	def line(self):
		return self._line

	def emit(self, s: str):
		""" Emits a quad for a node """
		print(s)

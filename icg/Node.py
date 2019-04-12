# Node.py

class Node():
	"""docstring for Node"""
	def __init__(self, line: int):
		super(Node, self).__init__()
		self._line = line

	@property
	def line(self):
		return self._line

	def emit(s: str):
		""" Emits a quad for a node """
		print(s)

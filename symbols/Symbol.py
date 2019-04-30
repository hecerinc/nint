# Symbol.py

class Symbol:
	"""Symbol is a conceptual structure to handle names (variables and functions) in the program"""
	def __init__(self, name: str, dtype):
		super().__init__()
		self._name = name
		self._dtype = dtype

	@property
	def dtype(self):
		return self._dtype

	@property
	def name(self):
		return self._name



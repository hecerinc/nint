# Variable.py

class Variable(Symbol):
	"""docstring for Variable"""
	def __init__(self, type, name):
		super().__init__(type)
		self._name = name

	@property
	def name(self):
		return self._name


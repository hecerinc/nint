# Function.py

class Function(Symbol):
	"""docstring for Function"""
	def __init__(self, type, varsTable : "Env"):
		super().__init__(type)
		self._varsTable = varsTable


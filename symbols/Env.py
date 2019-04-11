# Env.py

class Env():
	"""docstring for Env"""
	def __init__(self, previous: "Env"):
		self._previous = previous
		self._table = dict() # Symbol table

	def put(s, sym: "Symbol"):
		"""Insert a symbol into the symbol table"""
		# TODO: Check if already exists
		self._table[s] = sym
	def get(s):
		"""Gets a symbol from the symbol table

		@property s: String
		"""
		t = self
		while t is not None:
			found = t.get(s)
			if found is not None:
				return found
			t = t._previous
		else:
			return None

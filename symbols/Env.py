# Env.py

# Represents the symbol tables (Function Dir and Variables Table)
from .Symbol import Symbol

class Env:
	'''Represents a scope (an environment) in which variables and methods can be defined'''
	def __init__(self, previous: "Env" = None):
		self._previous = previous
		self._table = dict() # Symbol table

	def get(self, s: str) -> Symbol:
		'''Gets a symbol from the symbol table by recursively checking the previous tables'''
		t = self
		while t is not None:
			found = t.find(s)
			if found is not None:
				return found
			t = t._previous
		return None


	def exists(self, symbol_name: str) -> bool:
		''' Check if the symbol with symbol_name exists in this directory '''
		return symbol_name in self._table

	def find(self, symbol_name: str):
		'''Get the symbol with name symbol_name or None if not found'''
		return self._table.get(symbol_name, None)

	def insert(self, sym: Symbol):
		'''Inserts a symbol into the symbol directory'''
		# TODO: where do we check that it doesn't already exist?
		assert(sym.name not in self._table) # TODO: remove?
		self._table.update({sym.name: sym})


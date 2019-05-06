# Env.py

# Represents the symbol tables (Function Dir and Variables Table)
import sys
sys.path.append("C:/dev/compiler")

from .Symbol import Symbol
from icg.CompMem import CompMem, MemType


class Env:
	'''Represents a scope (an environment) in which variables and methods can be defined'''
	def __init__(self, previous: "Env" = None, memType = MemType.LOCAL):
		self._previous = previous
		self._table = dict() # Symbol table
		self._memory = CompMem(memType)
		self._funcdir = []

	@property
	def memory(self):
		return self._memory

	@property
	def functions(self):
		return self._funcdir


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
		from .Function import Function

		assert sym.name not in self._table
		if isinstance(sym, Function):
			self._funcdir.append(sym)
		self._table.update({sym.name: sym})

	def print(self):
		print()
		print('VARS TABLE')
		for item in self._table.items():
			print(item[0], item[1].dtype)
		print()

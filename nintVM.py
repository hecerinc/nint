# nintVM.py

import sys
import os
import pickle

from utils.Stack import Stack
from symbols.Operators import Operator
from vm.Memory import Memory, is_constant, is_temp
from nintCompiler import debug


debug_mode = os.getenv('NINT_ENV', 'debug')


class nintVM:
	"""docstring for nintVM"""
	def __init__(self, filename: str):
		super().__init__()
		self.ip = 0 # Instruction pointer
		self.quads = []
		self.ConstTable = dict()

		# Memcounts
		self._memcount_temp = 0
		self._memcount_global = 0


		self.load_data(filename)
		self._total_quads = len(self.quads)

		if debug_mode == 'debug':
			for quad in self.quads:
				debug(quad)

		# TODO: Create memory sections here
		self.Temp = Memory(self._memcount_temp)
		self._GlobalMemory = Memory(self._memcount_global)
		self.CallStack = Stack() # Local memory

		# Instruction set
		self.nintIS = {
			Operator.ASSIGN: self.assign,
			Operator.ADD: self.add,
			Operator.SUB: self.sub,
			Operator.MULT: self.mult,
			Operator.DIV: self.div,
			Operator.PRINT: self._print
		}

	def load_data(self, filename: str):
		'''Read the data into memory'''
		with open(filename, 'rb') as f:
			data = pickle.load(f)
		self.quads = data[0] # quads
		# TODO: I need to parse this table and get the actual values with their real types
		self.ConstTable = data[1] # consttable
		self._memcount_temp = data[2]

	def run(self):
		'''Run the actual code'''
		quad = self.quads[self.ip]
		while quad is not None:
			instruction = Operator(quad[0])
			method = self.nintIS[instruction]
			method(quad)
			quad = self.next()

	def next(self):
		self.ip += 1
		if self.ip < self._total_quads:
			return self.quads[self.ip]
		return None

	def get_value(self, address):
		if is_constant(address):
			return self.ConstTable[address]
		elif is_temp(address):
			return self.Temp.get_val(address)
		return self.mem.get_val(address)

	# Operation functions
	# ---------------------------------------------------------------
	def assign(self, quad):
		pass

	def add(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand + right_operand
		self.Temp.set_value(quad[3], result)

	def sub(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand - right_operand
		self.Temp.set_value(quad[3], result)

	def mult(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand * right_operand
		self.Temp.set_value(quad[3], result)

	def div(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		if right_operand == 0:
			raise Exception("Runtime Exception: Division by 0.")
		result = left_operand / right_operand
		self.Temp.set_value(quad[3], result)

	def _print(self, quad):
		arg = self.get_value(quad[3])
		print(arg)




def main(argv):
	'''Load the bytecode and initialise the VM'''
	if len(argv) < 2:
		print("Usage: python nintVM.py <file>.nint.bytecode")
		sys.exit()

	vm = nintVM(argv[1])
	vm.run()



if __name__ == '__main__':
	main(sys.argv)

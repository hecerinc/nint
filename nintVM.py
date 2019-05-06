# nintVM.py

import sys
import os
import pickle

from utils.Stack import Stack
from symbols.Operators import Operator
from vm.Memory import Memory, is_constant, is_temp, is_local, is_global
from vm.StackFrame import StackFrame
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

		self._returns_value = False
		self._newstack = None
		self._current_array = None
		self._subset_result = None


		self.load_data(filename)
		self._total_quads = len(self.quads)

		assert self._memcount_global != 0 and self._memcount_temp != 0, "No data read for global or temp counts from bytecode"

		if debug_mode == 'debug':
			debug("========== QUADS ===========")
			for quad in self.quads:
				debug(quad)
			debug()
			debug()

		self.Temp = Memory(self._memcount_temp)
		self._GlobalMemory = Memory(self._memcount_global)
		self.CallStack = Stack() # Local memory
		self.CallStack.push(self._GlobalMemory)

		# Instruction set
		self.nintIS = {

			# Arithmetic
			Operator.ASSIGN: self.assign,
			Operator.ADD: self.add,
			Operator.SUB: self.sub,
			Operator.MULT: self.mult,
			Operator.DIV: self.div,

			# Relops
			Operator.GT: self.gt,
			Operator.GTE: self.gte,
			Operator.LT: self.lt,
			Operator.LTE: self.lte,
			Operator.EQUAL: self.equals,
			Operator.NEQ: self.neq,

			# Boolean comparisons
			Operator.AND: self.bool_and,
			Operator.OR: self.bool_or,

			# GOTOs
			Operator.GOTO: self.goto,
			Operator.GOTOF: self.gotoF,
			Operator.GOTOV: self.gotoV,

			# Functions
			Operator.GOSUB: self.gosub,
			Operator.PARAM: self.param,
			Operator.ERA: self.expand_active_record,
			Operator.ENDPROC: self.endproc,
			Operator.RETURN: self.return_proc,

			# Vectors
			Operator.VECTOR: self.vector,
			Operator.PUSH: self.push_elem,
			Operator.ENDVECTOR: self.endvector,

			Operator.DIM: self.dim,
			Operator.SUBSET: self.subset,
			Operator.ENDSUBSET: self.endsubset,



			Operator.PRINT: self._print
		}

	def load_data(self, filename: str):
		'''Read the data into memory'''
		with open(filename, 'rb') as f:
			data = pickle.load(f)
		self.quads = data[0] # quads
		# TODO: I need to parse this table and get the actual values with their real types
		self.ConstTable = data[1] # consttable
		self.FunDir = data[2]
		self._memcount_global = data[3]
		self._memcount_temp = data[4]

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



	def set_value(self, address: str, value):
		if is_local(address):
			self.CallStack.peek().set_value(address, value)
		elif is_temp(address):
			self.Temp.set_value(address, value)
		else:
			self.CallStack.peek().set_value(address, value)

	def get_value(self, address):
		if is_constant(address):
			debug(address, "is_constant")
			return self.ConstTable[address]
		elif is_temp(address):
			return self.Temp.get_val(address)
		elif is_global(address): # TODO: we could probably remove this now
			return self._GlobalMemory.get_val(address)
		return self.CallStack.peek().get_val(address)
		# return self.mem.get_val(address)

	# Operation functions
	# ---------------------------------------------------------------
	def assign(self, quad):
		debug("assign")
		debug(quad)
		if self._returns_value:
			# Second param is function
			self._returns_value = False
			func = self.FunDir[quad[1]]
			assert 'value' in func, "Function should have a value because it is non-void"
			value = func['value']
		else:
			value = self.get_value(quad[1])
		assert value is not None
		target_address = quad[3]
		self.set_value(target_address, value)
		debug()


	# Relational operators
	# -------------------------------------------------
	def equals(self, quad):
		debug("equals")
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand == right_operand
		self.set_value(quad[3], result)
		debug()
	def neq(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand != right_operand
		self.set_value(quad[3], result)
	def gt(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand > right_operand
		self.set_value(quad[3], result)
	def gte(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand >= right_operand
		self.set_value(quad[3], result)
	def lt(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand < right_operand
		self.set_value(quad[3], result)
	def lte(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand <= right_operand
		self.set_value(quad[3], result)


	# Boolean operators
	# -------------------------------------------------
	def bool_and(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand and right_operand
		self.set_value(quad[3], result)

	def bool_or(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand or right_operand
		self.set_value(quad[3], result)

	# Arithmetic
	# -------------------------------------------------

	def add(self, quad):
		debug("add")
		debug(quad)
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand + right_operand
		self.set_value(quad[3], result)
		debug()

	def sub(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand - right_operand
		self.set_value(quad[3], result)

	def mult(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand * right_operand
		self.set_value(quad[3], result)

	def div(self, quad):
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		if right_operand == 0:
			raise Exception("Runtime Exception: Division by 0.")
		result = left_operand / right_operand
		self.set_value(quad[3], result)


	# GOTOs
	# -------------------------------------------------

	def goto(self, quad):
		quad_addr = int(quad[3])
		self.ip = quad_addr - 1

	def gotoF(self, quad):
		expr_result = self.get_value(quad[1])
		if not expr_result:
			self.ip = int(quad[3]) -1

	def gotoV(self, quad):
		raise Exception('Not implemented')

	# Functions
	# ---------------------------------------------------------------

	def expand_active_record(self, quad):
		debug("ERA")
		func_name = quad[1]

		assert func_name in self.FunDir, "No function"

		size_map = self.FunDir[func_name]

		# Create the AR
		sf = StackFrame(func_name, size_map)

		# Add it to the callstack
		# self.CallStack.push(sf)
		self._newstack = sf
		debug()

	def param(self, quad):
		debug('param')
		current_scope = self.CallStack.peek()
		assert current_scope is not None, "No callstack"
		param = self.get_value(quad[1])
		address = quad[3]
		assert self._newstack is not None
		self._newstack.set_value(address, param)
		debug()

	def gosub(self, quad):
		debug('gosub')
		sf = self._newstack
		self.CallStack.push(sf)
		sf.set_return_addr(self.ip)
		self.ip = int(quad[3])-1  # minus 1 because next() adds one
		debug()

	def endproc(self, quad):
		debug('endproc')
		current_scope = self.CallStack.pop()
		self.ip = current_scope.return_addr
		self._newstack = None
		del current_scope # vacuous statement but makes me feel good
		debug()

	def return_proc(self, quad):
		is_empty_return = quad[1] is None
		if is_empty_return:
			return self.endproc(quad)
		current_scope = self.CallStack.peek()
		fname = current_scope.function_name
		retval = self.get_value(quad[1])
		self.FunDir[fname]['value'] = retval
		self._returns_value = True
		return self.endproc(None)


	# Vectors
	# ---------------------------------------------------------------
	def vector(self, quad):
		size = int(quad[3])
		self._current_array = [None]*size
		self._current_array_length = 0

	def push_elem(self, quad):
		value = self.get_value(quad[3])
		self._current_array[self._current_array_length] = value
		self._current_array_length += 1

	def endvector(self, quad):
		array = self._current_array
		self.set_value(quad[3], array)
		self._current_array = None

	def subset(self, quad):
		self._current_array = self.get_value(quad[3])

	def dim(self, quad):
		array = self._current_array
		subset_value = self.get_value(quad[3])
		# Validate it's within bounds
		assert subset_value >= 0 and subset_value < len(array), "Out of bounds exception: index is out of bounds."
		if self._subset_result is None:
			self._subset_result = []
		self._subset_result.append(array[subset_value])

	def endsubset(self, quad):
		result = self._subset_result
		if len(result) == 1:
			result = result[0]
		self.set_value(quad[3], result)
		self._current_array = None
		self._subset_result = None

	# Special functions
	# ---------------------------------------------------------------
	def _print(self, quad):
		arg = self.get_value(quad[3])
		if isinstance(arg, bool):
			arg = str(arg).lower()
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

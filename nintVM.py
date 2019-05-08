# nintVM.py

import sys
import os
import pickle

from utils.Stack import Stack
from symbols.Operators import Operator
from vm.Memory import Memory, is_constant, is_temp, is_local, is_global, is_pointer
from vm.StackFrame import StackFrame
from nintCompiler import debug


debug_mode = os.getenv('NINT_ENV', 'debug')


class nintVM:
	"""Main class for the nint virtual machine"""
	def __init__(self, filename: str):
		'''Init all the bookkeeping necessary and store the instruction set'''
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
		self._current_array_address = None
		self._subset = []


		self.load_data(filename)
		self._total_quads = len(self.quads)

		# Check that the bytecode has the info we need
		assert self._memcount_global != 0 and self._memcount_temp != 0, "No data read for global or temp counts from bytecode"

		if debug_mode == 'debug':
			debug("========== QUADS ===========")
			for quad in self.quads:
				debug(quad)
			debug()
			debug()

		# Intialize memory
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
		'''Get the next quadruple'''
		self.ip += 1
		if self.ip < self._total_quads:
			return self.quads[self.ip]
		return None




	def set_value(self, address: str, value, check_pointer = True):
		'''Set the value of an address. Checks scope and calls set_value on the appropriate
		Memory instance.'''
		pointer = None
		if check_pointer and is_pointer(address):
			pointer = self.get_value(address, False)
		if is_local(address):
			self.CallStack.peek().set_value(address, value, pointer)
		elif is_temp(address):
			self.Temp.set_value(address, value, pointer)
		else:
			self.CallStack.peek().set_value(address, value, pointer)

	def get_value(self, address, check_pointer = True):
		'''Get value of an address. Check first if this is a pointer
		and whether we should dereference it'''
		value = self._get_value(address)
		if check_pointer and is_pointer(address):
			value = self.dereference_pointer(value)
		return value

	def _get_value(self, address):
		'''The actual function that checks which instance of memory to
		retrieve the value from'''
		if is_constant(address):
			debug(address, "is_constant")
			return self.ConstTable[address]
		elif is_temp(address):
			return self.Temp.get_val(address)
		elif is_global(address): # TODO: we could probably remove this now
			return self._GlobalMemory.get_val(address)
		return self.CallStack.peek().get_val(address)
		# return self.mem.get_val(address)

	def dereference_pointer(self, pointer):
		'''Dereferences an address of type pointer. Used for array subsetting.'''
		array_addr = pointer[0]
		subset = pointer[1]
		array = self._get_value(array_addr)
		result = []
		for index in subset:
			result.append(array[index])
		assert len(result) > 0, "No elements indexed"
		return result[0] if len(result) == 1 else result

	# Operation functions
	# ---------------------------------------------------------------
	def assign(self, quad):
		'''Assign a value to an address'''
		debug("assign")
		debug(quad)
		if self._returns_value:
			# If this is a function that returned, store the return value in the function directory
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
		'''Check equality.'''
		debug("equals")
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand == right_operand
		self.set_value(quad[3], result)
		debug()
	def neq(self, quad):
		'''Check that a value not equals'''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand != right_operand
		self.set_value(quad[3], result)
	def gt(self, quad):
		'''Check greater than >'''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand > right_operand
		self.set_value(quad[3], result)
	def gte(self, quad):
		'''Check greater than or equal to >='''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand >= right_operand
		self.set_value(quad[3], result)
	def lt(self, quad):
		'''Check less than >'''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand < right_operand
		self.set_value(quad[3], result)
	def lte(self, quad):
		'''Check less than or equal to >='''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand <= right_operand
		self.set_value(quad[3], result)


	# Boolean operators
	# -------------------------------------------------
	def bool_and(self, quad):
		'''Perform a boolean &&'''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand and right_operand
		self.set_value(quad[3], result)

	def bool_or(self, quad):
		'''Perform a boolean ||'''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand or right_operand
		self.set_value(quad[3], result)

	# Arithmetic
	# -------------------------------------------------

	def add(self, quad):
		'''Add two operands'''
		debug("add")
		debug(quad)
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand + right_operand
		self.set_value(quad[3], result)
		debug()

	def sub(self, quad):
		'''Subtract two operands'''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand - right_operand
		self.set_value(quad[3], result)


	def mult(self, quad):
		'''Multiply two operands'''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		result = left_operand * right_operand
		self.set_value(quad[3], result)

	def div(self, quad):
		'''Divide two operands. Check division by 0.'''
		left_operand = self.get_value(quad[1])
		right_operand = self.get_value(quad[2])
		if right_operand == 0:
			raise Exception("Runtime Exception: Division by 0.")
		result = left_operand / right_operand
		self.set_value(quad[3], result)


	# GOTOs
	# -------------------------------------------------

	def goto(self, quad):
		'''Jump to quad index in GOTO expression'''
		quad_addr = int(quad[3])
		self.ip = quad_addr - 1

	def gotoF(self, quad):
		'''Jump to quad index if expression is false'''
		expr_result = self.get_value(quad[1])
		if not expr_result:
			self.ip = int(quad[3]) -1

	def gotoV(self, quad):
		'''Jump to quad index if expression is true'''
		raise Exception('Not implemented')

	# Functions
	# ---------------------------------------------------------------

	def expand_active_record(self, quad):
		'''Expand the active record. Create the memory required for this
		function in its own StackFrame. Add it to the callstack.'''
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
		'''Copy a value from a memory address to the current
		stack frame as a local variable (param)'''
		debug('param')
		current_scope = self.CallStack.peek()
		assert current_scope is not None, "No callstack"
		param = self.get_value(quad[1])
		address = quad[3]
		assert self._newstack is not None
		self._newstack.set_value(address, param)
		debug()

	def gosub(self, quad):
		'''Move instruction pointer to wherever the function starts.
		Store the return address.'''
		debug('gosub')
		sf = self._newstack
		self.CallStack.push(sf)
		sf.set_return_addr(self.ip)
		self.ip = int(quad[3])-1  # minus 1 because next() adds one
		debug()

	def endproc(self, quad):
		'''Pop the current stack frame from the call stack and
		release the memory. Point instruction pointer to wherever it was
		before the function call'''
		debug('endproc')
		current_scope = self.CallStack.pop()
		self.ip = current_scope.return_addr
		self._newstack = None
		del current_scope # vacuous statement but makes me feel good
		debug()

	def return_proc(self, quad):
		'''If funciton returned, store the value in the function directory. Call endproc.'''
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
		'''Allocate memory for a new vector of a specified size'''
		size = int(quad[3])
		self._current_array = [None]*size
		self._current_array_length = 0

	def push_elem(self, quad):
		'''Push an element to the current vector'''
		value = self.get_value(quad[3])
		self._current_array[self._current_array_length] = value
		self._current_array_length += 1

	def endvector(self, quad):
		'''Copy the currently building vector into its corresponding memory address'''
		array = self._current_array
		self.set_value(quad[3], array)
		self._current_array = None

	def subset(self, quad):
		'''Start an array subsetting. Get the array from memory.'''
		self._current_array = self.get_value(quad[3])
		self._current_array_address = quad[3]

	def dim(self, quad):
		'''Add an subsetter index in dimension i (read from quad). Check that
		each subset index is within the range of the current address length'''
		# TODO: actually read the dimension to support data frames
		array = self._current_array
		subset_value = self.get_value(quad[3])
		# Validate it's within bounds
		assert subset_value >= 0 and subset_value < len(array), "Out of bounds exception: index is out of bounds."
		# 	self._subset_result = []
		if self._subset is None: # TODO: what is this?
			self._subset = []
		self._subset.append(subset_value)
		# self._subset_result.append(array[subset_value])

	def endsubset(self, quad):
		'''End the subset and store the subset result as a pointer in the designated memory'''
		result = (self._current_array_address, self._subset)
		# if len(result) == 1:
		# 	result = result[0]
		self.set_value(quad[3], result, False)
		self._current_array_address = None
		self._current_array = None
		self._subset = None

	# Special functions
	# ---------------------------------------------------------------
	def _print(self, quad):
		'''Print expression'''
		arg = self.get_value(quad[3])
		if isinstance(arg, bool):
			arg = str(arg).lower()
		print(arg)




def main(argv):
	'''Load the bytecode and initialise the VM'''
	if len(argv) < 2:
		print("Usage: nintVM <file>.nint.bytecode")
		sys.exit()

	vm = nintVM(argv[1])
	vm.run()



if __name__ == '__main__':
	main(sys.argv)

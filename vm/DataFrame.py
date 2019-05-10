# DataFrame.py
import pandas as pd

class DataFrame:
	"""docstring for DataFrame"""
	def __init__(self, columns, vm = None, df = None):
		super().__init__()
		if df is not None:
			self.df = df
			self.dim1 = df.shape[0]
			self.dim2 = df.shape[1]
			return
		self._columns = columns
		dflist = {}
		for i,col in enumerate(columns):
			dflist.update({'col{}'.format(i): col})
		self.df = pd.DataFrame(dflist)
		self._vm = vm
		self.dim1 = len(columns[0])
		self.dim2 = len(columns)

	@property
	def columns(self):
		return self._columns

	def subset(self, dim1, dim2):
		dim1 = dim1[0] if len(dim1) == 1 else dim1
		dim2 = dim2[0] if len(dim2) == 1 else dim2
		result = self.df.iloc[dim1, dim2]
		is_row = isinstance(dim1, int) and isinstance(dim2, list)
		is_col = isinstance(dim1, list) and isinstance(dim2, int)
		if is_row:
			result = pd.DataFrame([result])
		elif is_col:
			result = result.tolist()

		if isinstance(result, pd.DataFrame):
			result = DataFrame(None, None, result)
		return result

	def __str__(self):
		# Resolve columns
		return self.df.to_string(index = False, header = False)




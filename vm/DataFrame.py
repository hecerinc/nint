# DataFrame.py
import pandas as pd

class DataFrame:
	"""docstring for DataFrame"""
	def __init__(self, columns, vm):
		super().__init__()
		self._columns = columns
		self._vm = vm

	@property
	def columns(self):
		return self._columns

	def __str__(self):
		# Resolve columns
		dflist = {}
		for i,col in enumerate(self.columns):
			dflist.update({'col{}'.format(i): self._vm.get_value(col)})
		df = pd.DataFrame(dflist)
		return df.to_string(index = False, header = False)




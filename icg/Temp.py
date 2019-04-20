# Temp.py

class Temp():
	""" AVAIL to get the next temporary """
	counter = 0

	def __init__(self, token):
		super(Temp, self).__init__()
		self.token = token

	@staticmethod
	def getTmp():
		Temp.counter = Temp.counter + 1
		return Temp("t{}".format(Temp.counter))

	def toString(self):
		return self.token

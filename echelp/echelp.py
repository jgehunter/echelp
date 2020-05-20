

class electricalCircuit():

	def __init__(self, name=None, parameters=None):
		self.name = name
		self.parameters = parameters

	def getParameters(self, **kwargs):
		if self.name is None:
			raise Exception("Electrical Circuit name not specified.")


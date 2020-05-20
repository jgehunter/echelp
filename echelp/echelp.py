

class electricalCircuit():

	def __init__(self, name=None, parameters=None, **kwargs):
		self.name = name
		self.parameters = parameters
		for key in kwargs:
			setattr(self, key, kwargs[key])
			print(key)

	def getParameters(self, **kwargs):
		if self.name is None:
			raise Exception("Electrical Circuit name not specified.")



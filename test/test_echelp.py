import pytest
from echelp import echelp

class TestCircuits:

	def test_CircuitObjectCreated(self):
		testObject = echelp.electricalCircuit()
		assert isinstance(testObject, echelp.electricalCircuit)



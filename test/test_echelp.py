import pytest
from .. import echelp

class TestCircuits:

	def test_CircuitObjectCreated():
		testObject = electricalCircuit()
		assert isinstance(testObject, electricalCircuit)


def test_test():
	assert 1 == 1



import pytest
from echelp.echelp import electricalCircuit

class TestCircuits:

	def test_CircuitObjectCreated(self):
		testObject = electricalCircuit(name="Test")
		assert isinstance(testObject, electricalCircuit)

	def test_CreateCircuitObject(self):
		testString = "This is a test circuit."
		testCircuit = electricalCircuit(name = testString)
		assert testCircuit.name == testString, "Expected %r but received %r" % testString % testCircuit.name

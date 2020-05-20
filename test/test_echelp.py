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

	def test_PassCircuitCharacteristics(self):
		exampleCharacteristics = {
									"R1": 10,
									"R2": 20,
									"C1": 10,
		}

		testCircuit = electricalCircuit(name = "Test", parameters = exampleCharacteristics)
		assert testCircuit.parameters == exampleCharacteristics

	def test_ExceptionIfGetCharacteristicsNoName(self):
		testCircuit = electricalCircuit()
		assert pytest.raises(Exception)

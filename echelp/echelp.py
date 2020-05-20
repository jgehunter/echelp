from sympy import *

circuitDictionary = {
    "SallenKeyLowPass": {
        "Unknowns": 4,
        "Parameters": ["RA", "RB", "F", "R", "C"],
        "Equations": ["3-(RA+RB)/RA-1.4142", "F-1/(2*PI*R*C)"]
    }
}


class electricalCircuit():

    def __init__(self, name=None, parameters=None, circuitDictionary=None, **kwargs):
        self.name = name
        self.parameters = parameters
        self.circuitDictionary = circuitDictionary
        for key in kwargs:
            setattr(self, key, kwargs[key])
            print(key)

    def setCircuit(self):
        """Function that calculates the missing parameter values.

        This function asks the user for the necessary parameters to set
        and calculates the remaining parameters of the circuit.

        """
        if self.name is not None:
            raise Exception("Electrical Circuit name not specified.")

    def setParameters(self):
        """Function that calculates parameters based on circuit name."""

        if self.name is not None:
            for key in self.circuitDictionary.keys():
                if self.name == key:
                    self.parameters = self.circuitDictionary[key]["Parameters"]

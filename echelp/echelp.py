circuitDictionary = {
    "SallenKeyLowPass": {
        "Unknowns": 4,
        "Parameters": ["RA", "RB", "F", "R", "C"],
        "Equations": ["3-(RA+RB)/RA-1.4142", "F-1/(2*PI*R*C)"]
    }
}


class electricalCircuit():

    def __init__(self, name=None, parameters=None, circuitDictionary=None, ** kwargs):
        self.name = name
        self.parameters = parameters
        self.circuitDictionary = circuitDictionary
        for key in kwargs:
            setattr(self, key, kwargs[key])
            print(key)

    def getParameters(self):
        if self.name is None:
            raise Exception("Electrical Circuit name not specified.")

from echelp import electricalCircuit

circuitDictionary = {
    "SallenKeyLowPass": {
        "Unknowns": 4,
        "Parameters": ["RA", "RB", "F", "R", "C"],
        "Equations": ["3-(RA+RB)/RA-1.4142", "F-1/(2*pi*R*C)"]
    }
}


if __name__ ==  "__main__":
    testCircuit = electricalCircuit(circuitDictionary=circuitDictionary, name="SallenKeyLowPass")
    testCircuit.setParameters()


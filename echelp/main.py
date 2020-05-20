from echelp import electricalCircuit

circuitDictionary = {
    "SallenKeyLowPass": {
        "Unknowns": 4,
        "Parameters": ["RA", "RB", "F", "R", "C"],
        "Equations": ["3-(RA+RB)/RA-1.4142", "F-1/(2*pi*R*C)"]
    }
}


if __name__ == "__main__":
    print("Hello")
    val = input("What kind of circuit are you designing?\n")
    testCircuit = electricalCircuit(
        circuitDictionary=circuitDictionary,
        name=val)
    testCircuit.setParameters()
    testCircuit.setEquations()
    testCircuit.getValues()

from sympy import solve, symbols
from sympy.parsing.sympy_parser import parse_expr

circuitDictionary = {
    "SallenKeyLowPass": {
        "Unknowns": 4,
        "Parameters": ["RA", "RB", "F", "R", "C"],
        "Equations": ["3-(RA+RB)/RA-1.4142", "F-1/(2*pi*R*C)"]
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

        variables = ""
        for parameter in self.parameters:
            variables += parameter + " "

        variables = symbols(variables)
        listVariables = []
        for variable in variables:
            listVariables.append(variable)
        self.variables = listVariables
        print(listVariables)

    def setEquations(self):
        """Function that calculates equations based on circuit name."""

        if self.name is not None:
            for key in self.circuitDictionary.keys():
                if self.name == key:
                    self.equations = self.circuitDictionary[key]["Equations"]

            equationList = []
            for equation in self.equations:
                equationList.append(parse_expr(equation))
            self.system = equationList
            print(equationList)

    def getValues(self):
        """Function that calculates values for the unknowns"""

        numberUnknowns = len(self.variables) - len(self.system)
        unknownsFixed = [0] * len(self.variables)
        listSubs = []
        while numberUnknowns > 0:
            print("The unknown variables are:")
            for idx, variable in enumerate(self.variables):
                if unknownsFixed[idx] == 0:
                    print(variable)
            val = input("Which variable do you want to fix?\n")
            chosenVar = symbols(val)
            for idx, variable in enumerate(self.variables):
                if chosenVar == variable:
                    unknownsFixed[idx] = 1
                    val2 = input("What value do you want to give it?\n")
                    val2 = float(val2)
                    listSubs.append((variable, val2))
                    numberUnknowns = numberUnknowns - 1

        newSystem = []
        for equation in self.system:
            equation = equation.subs(listSubs)
            newSystem.append(equation)

        newVariables = []
        for idx, variable in enumerate(self.variables):
            if unknownsFixed[idx] == 0:
                newVariables.append(variable)

        solution = solve(newSystem, newVariables)
        print(type(solution))

        for variable in newVariables:
            print(f"The value of {variable} is {solution[variable]}.")

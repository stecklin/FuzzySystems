import numpy as np


class RuleBase(object):
    """
    Representation of a set of rules in order to determine a fuzzy relation that fits the rule base.
    """

    def __init__(self, num_rules, set1, set2):
        """Initialize rule base with a fixed number of rules and two crisp sets."""
        self.set1 = set1
        self.set2 = set2
        self.rules = {i: () for i in range(1, num_rules + 1)}
        self.solutions = {i: [] for i in range(1, num_rules + 1)}
        self.solution = []

    def _validate_single_solution(self, index):
        """Validate a single solution for a specific rule."""
        rule = self.rules[index]
        for col, elem2 in enumerate(rule[1]):
            # compare result of composition to given rules
            comp = max([min(rule[0][i], self.solutions[index][i][col]) for i in range(len(self.set1))])
            if elem2 != comp:
                return False
        return True

    def _validate_solution(self):
        """Validate the global solution."""
        for rule in self.rules.values():
            for col, elem2 in enumerate(rule[1]):
                # compare result of composition to given rules
                comp = max([min(rule[0][i], self.solution[i][col]) for i in range(len(self.set1))])
                if elem2 != comp:
                    return False
        return True

    def set_rule(self, index, rule):
        """Set rule for a specific index."""
        if len(rule[0]) != len(self.set1):
            raise ValueError('Left-hand side of the rule should have length ' + str(len(self.set1)) + '.')
        if len(rule[1]) != len(self.set2):
            raise ValueError('Right-hand side of the rule should have length ' + str(len(self.set2)) + '.')
        for value in rule[0] + rule[1]:
            if not 0 <= value <= 1:
                raise ValueError('Fuzzy sets must contain values between 0 and 1.')

        self.rules[index] = rule

    def get_single_solution(self, index):
        """Compute the Goedel relation for a single rule and check whether it is a solution."""
        if not self.solutions[index]:
            self.solutions[index] = np.zeros((len(self.set1), len(self.set2)))
            for row, elem1 in enumerate(self.rules[index][0]):
                for col, elem2 in enumerate(self.rules[index][1]):
                    if elem1 <= elem2:
                        self.solutions[index][row][col] = 1
                    else:
                        self.solutions[index][row][col] = elem2

        if not self._validate_single_solution(index):
            raise ValueError('There is no solution to given rule ' + str(index) + '.')

        return self.solutions[index]

    def get_solution(self):
        """Compute the global relation as the minimum of all Goedel relations and check whether it is a solution."""
        if not self.solution:
            self.solution = np.zeros((len(self.set1), len(self.set2)))
            for row in range(len(self.set1)):
                for col in range(len(self.set2)):
                    self.solution[row][col] = min([solution[row][col] for solution in self.solutions.values()])

        if not self._validate_solution():
            raise ValueError('There is no global solution to the given set of rules.')

        return self.solution

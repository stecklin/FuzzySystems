from fuzzy_rules.fuzzy_rules import RuleBase


# subtask a) Enter crisp sets
set1_input = raw_input('Please enter first crisp set X (e.g. s m l): ') or 's m l'
set1 = set1_input.split(' ')
set2_input = raw_input('Please enter second crisp set Y (e.g. 140 160 180 200): ') or '140 160 180 200'
set2 = set2_input.split(' ')

# subtask b) Enter fuzzy sets
num_rules_input = raw_input('Please enter the number of rules (e.g. 2): ') or '2'
num_rules = int(num_rules_input)

rule_base = RuleBase(num_rules, set1, set2)

example1 = ' '.join(['0.8'] * len(set1))
example2 = ' '.join(['0.2'] * len(set2))

for i in range(1, num_rules + 1):
    rule_left_input = raw_input('Please enter fuzzy set ' + str(i) + ' for X (e.g. ' + example1 + '): ') or example1
    rule_right_input = raw_input('Please enter fuzzy set ' + str(i) + ' for Y (e.g. ' + example2 + '): ') or example2
    rule_left = [float(value) for value in rule_left_input.split(' ')]
    rule_right = [float(value) for value in rule_right_input.split(' ')]
    rule_base.set_rule(i, (rule_left, rule_right))

# subtask c) Compute single solutions
for i in range(1, num_rules + 1):
    print 'Solution for rule ' + str(i) + ':'
    try:
        print rule_base.get_single_solution(i)
    except ValueError as e:
        print e.message

# subtask d) Compute overall solution
print 'Solution for all rules:'
try:
    print rule_base.get_solution()
except ValueError as e:
    print e.message

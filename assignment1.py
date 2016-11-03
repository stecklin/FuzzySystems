from alphacuts.alphacuts import FuzzySet


# subtask a) Read alpha levels
alpha_levels = raw_input('Please enter alpha levels (e.g. 0 0.5 1): ')
alpha_level_list = [float(level) for level in alpha_levels.split(' ')]
fuzzy_set = FuzzySet(alpha_level_list)

# subtask b) Read alpha cuts for each level
for level in fuzzy_set.get_alpha_levels():
    alpha_cut = raw_input('Please enter alpha cut for level ' + str(level) + ' (e.g. 5-7 10-12): ')
    alpha_cut_list = alpha_cut.split(' ')

    for set_tuple in alpha_cut_list:
        lower_bound, upper_bound = set_tuple.split('-')
        fuzzy_set.append_alpha_cut(level, (float(lower_bound), float(upper_bound)))

# subtask c) Return membership degree for an element x
while True:
    x = raw_input('Please enter an element to request its membership: ')
    print fuzzy_set.membership_degree(float(x))

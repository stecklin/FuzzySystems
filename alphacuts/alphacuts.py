from collections import OrderedDict


class FuzzySet(object):
    """
    Horizontal representation of a fuzzy set by its alpha cuts.
    """

    def __init__(self, alpha_levels):
        """Initialize fuzzy set with a list of alpha levels."""
        # check if levels are between 0 and 1
        for level in alpha_levels:
            if not 0 <= level <= 1:
                raise ValueError('Levels must be between 0 and 1.')

        alpha_levels.sort(reverse=True)
        self.alpha_cuts = OrderedDict((level, []) for level in alpha_levels)

    def _contains(self, alpha_list, x):
        """Check whether x is contained in alpha_list."""
        for element in alpha_list:
            if element[0] <= x <= element[1]:
                return True
        return False

    def get_alpha_levels(self):
        """Return list of alpha levels."""
        return self.alpha_cuts.keys()

    def set_alpha_cut(self, alpha_level, alpha_cut):
        """Set alpha cut for a specific alpha level."""
        self.alpha_cuts[alpha_level] = alpha_cut

    def append_alpha_cut(self, alpha_level, set_tuple):
        """Append a single tuple to a specific alpha level."""
        self.alpha_cuts[alpha_level].append(set_tuple)

    def membership_degree(self, x):
        """Return the membership degree for element x."""
        for alpha_level in self.alpha_cuts:
            if self._contains(self.alpha_cuts[alpha_level], x):
                return alpha_level
        raise ValueError('Element out of universe of discourse.')

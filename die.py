"""Model a die with a configurable number of sides."""
from random import randint


class Die:
    """A die whose sides are numbered from 1 to num_sides."""

    def __init__(self, num_sides=6):
        if not isinstance(num_sides, int) or num_sides < 2:
            raise ValueError("A die must have at least two sides")
        self.num_sides = num_sides

    def roll(self):
        """Return one randomly selected face."""
        return randint(1, self.num_sides)

from random import randint


class Die:
    """A class to represent single die"""

    def __init__(self, num_sides=6):
        """Default assumption is die has 6 sides """
        self.num_sides = num_sides

    def roll(self):
        """Randomly chose a side"""
        return randint(1, self.num_sides)

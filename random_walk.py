from random import choice


class RandomWalk:
    """A class to generate random walk"""

    def __init__(self, num_points=5000):
        """Initialize a walk"""
        self.num_points = num_points

        # All walks starts at (0,0)
        self.x_val = [0]
        self.y_val = [0]

    def get_step(self):
        """define the number of steps and direction"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        steps = distance * direction
        return steps

    def fill_walk(self):
        """Calculate the points of walk"""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_val) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_steps = self.get_step()
            y_steps = self.get_step()
            if x_steps == 0 and y_steps == 0:
                continue
            x = self.x_val[-1] + x_steps
            y = self.y_val[-1] + y_steps
            self.x_val.append(x)
            self.y_val.append(y)

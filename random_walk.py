"""Generate a two-dimensional random walk."""
from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        if not isinstance(num_points, int) or num_points < 1:
            raise ValueError("num_points must be a positive integer")
        self.num_points = num_points
        self.x_val = [0]
        self.y_val = [0]

    @staticmethod
    def get_step():
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return distance * direction

    def fill_walk(self):
        """Generate points up to num_points, starting at the origin."""
        while len(self.x_val) < self.num_points:
            x_step, y_step = self.get_step(), self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            self.x_val.append(self.x_val[-1] + x_step)
            self.y_val.append(self.y_val[-1] + y_step)

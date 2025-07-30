import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
def scatter():
    while True:
        # Make a random walk
        rw = RandomWalk(250000)
        rw.fill_walk()

        # plot the points in the walk
        plt.style.use('classic')
        # The figsize parameter takes a tuple, which tells Matplotlib the dimensions of the plotting window in inches
        # Matplotlib assumes that your screen resolution is 100 pixels per inch.
        # if you know your system’s resolution, pass plt.subplots() the resolution
        # using the 'dpi' parameter to set a plot size. eg:- plt.subplots(figsize=(15, 9), dpi=120)
        fig, ax = plt.subplots(figsize=(15, 9))

        point_numbers = range(rw.num_points)
        ax.scatter(rw.x_val, rw.y_val, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
        # Emphasize the first and last points.
        ax.scatter(rw.x_val[0], rw.y_val[0], c='green', edgecolor='none', s=10)
        ax.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolor='none', s=10)
        # Remove the axes
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.show()

        keep_running = input("Make another walk? (y,n): ")
        if keep_running == 'n':
            break


def plot():
    while True:
        # Make a random walk
        rw = RandomWalk(5000)
        rw.fill_walk()

        # plot the points in the walk
        plt.style.use('classic')
        # The figsize parameter takes a tuple, which tells Matplotlib the dimensions of the plotting window in inches
        # Matplotlib assumes that your screen resolution is 100 pixels per inch.
        # if you know your system’s resolution, pass plt.subplots() the resolution
        # using the 'dpi' parameter to set a plot size. eg:- plt.subplots(figsize=(15, 9), dpi=120)
        fig, ax = plt.subplots(figsize=(12, 7))

        point_numbers = range(rw.num_points)
        ax.plot(rw.x_val, rw.y_val, c='blue', linewidth=1)
        # Emphasize the first and last points.
        ax.scatter(rw.x_val[0], rw.y_val[0], c='green', edgecolor='none', s=30)
        ax.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolor='none', s=30)
        # Remove the axes
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.show()

        keep_running = input("Make another walk? (y,n): ")
        if keep_running == 'n':
            break


while True:
    w = input("plot(p), scatter(s) or quit(q): ")
    if w == 'p':
        plot()
    elif w == 's':
        scatter()
    elif w == 'q':
        break
    else:
        print("Invalid value! Try again.")
        continue

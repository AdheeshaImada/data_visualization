"""Explore random walks as scatter plots or connected paths."""
import matplotlib.pyplot as plt
from random_walk import RandomWalk


def draw_walk(mode="scatter", num_points=None):
    if mode not in ("scatter", "plot"):
        raise ValueError("mode must be scatter or plot")
    if num_points is None:
        num_points = 50000 if mode == "scatter" else 5000
    walk = RandomWalk(num_points)
    walk.fill_walk()
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(12, 7))
    if mode == "scatter":
        ax.scatter(walk.x_val, walk.y_val, c=range(len(walk.x_val)),
                   cmap=plt.cm.Blues, s=1, edgecolors="none")
    else:
        ax.plot(walk.x_val, walk.y_val, linewidth=1)
    ax.scatter(walk.x_val[0], walk.y_val[0], c="green", s=30, label="Start")
    ax.scatter(walk.x_val[-1], walk.y_val[-1], c="red", s=30, label="End")
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")
    fig.tight_layout()
    plt.show()
    plt.close(fig)


def main():
    while True:
        mode = input("Plot (p), scatter (s), or quit (q): ").strip().lower()
        if mode == "q":
            break
        if mode not in ("p", "s"):
            print("Enter p, s, or q.")
            continue
        while True:
            draw_walk("plot" if mode == "p" else "scatter")
            if input("Make another walk? (y/n): ").strip().lower() != "y":
                break


if __name__ == "__main__":
    main()

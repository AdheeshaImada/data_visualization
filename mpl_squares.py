"""Plot the first five square numbers with Matplotlib."""
import matplotlib.pyplot as plt


def main():
    values = [1, 2, 3, 4, 5]
    squares = [value ** 2 for value in values]
    plt.style.use("Solarize_Light2")
    fig, ax = plt.subplots()
    ax.plot(values, squares, linewidth=3)
    ax.set_title("Square numbers", fontsize=14)
    ax.set_xlabel("Value", fontsize=10)
    ax.set_ylabel("Square", fontsize=10)
    ax.tick_params(axis="both", labelsize=10)
    plt.show()


if __name__ == "__main__":
    main()

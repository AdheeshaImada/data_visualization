"""Three Matplotlib examples showing square numbers."""
import matplotlib.pyplot as plt


def chart(sample_size=5, mode="scatter", gradient=False):
    x_values = list(range(1, sample_size + 1))
    y_values = [x ** 2 for x in x_values]
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    if mode == "line":
        ax.plot(x_values, y_values)
    else:
        kwargs = {"s": 200 if sample_size == 5 else 10}
        if gradient:
            kwargs.update(c=y_values, cmap=plt.cm.Blues)
        ax.scatter(x_values, y_values, **kwargs)
    ax.set_title("Square numbers", fontsize=14)
    ax.set_xlabel("Value", fontsize=12)
    ax.set_ylabel("Square", fontsize=12)
    ax.tick_params(axis="both", which="major", labelsize=10)
    if sample_size > 5:
        ax.axis([0, sample_size + 100, 0, (sample_size + 50) ** 2])
    plt.show()


def ex1():
    chart(sample_size=5)


def ex2():
    chart(sample_size=1000)


def ex3():
    chart(sample_size=1000, gradient=True)


def main():
    while True:
        answer = input("Which example? (1, 2, 3 or q): ").strip().lower()
        if answer == "q":
            break
        actions = {"1": ex1, "2": ex2, "3": ex3}
        if answer in actions:
            actions[answer]()
        else:
            print("Choose 1, 2, 3 or q.")


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt


def ex1():
    x_value = [1, 2, 3, 4, 5]
    y_value = [1, 4, 9, 16, 25]

    plt.style.use('seaborn-v0_8')

    fig, ax = plt.subplots()
    ax.scatter(x_value, y_value, s=200)

    # set chart title and label axes
    ax.set_title("Squire numbers", fontsize=14)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squire", fontsize=14)

    # Set size of tick labels.
    ax.tick_params(axis='both', which='major', labelsize=14)

    plt.show()


def ex2():
    x_val = range(1, 1001)
    y_val = [x**2 for x in x_val]

    plt.style.use('seaborn-v0_8')

    fig, ax = plt.subplots()

    ax.scatter(x_val, y_val, c='red', s=10)

    ax.set_title("squire number", fontsize=14)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squire", fontsize=14)

    ax.tick_params(axis='both', which='major', labelsize=14)

    # Set the range for each axis.
    ax.axis([0, 1100, 0, 1100000])

    plt.show()


def ex3():
    """use color map"""
    x_val = range(1, 1001)
    y_val = [x**2 for x in x_val]

    plt.style.use('seaborn-v0_8')

    fig, ax = plt.subplots()

    ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Blues, s=10)

    ax.set_title("squire number", fontsize=14)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squire", fontsize=14)

    ax.tick_params(axis='both', which='major', labelsize=14)

    # Set the range for each axis.
    ax.axis([0, 1100, 0, 1100000])

    plt.show()


def which_example():
    n = int(input("Which example? "))
    if n == 1:
        ex1()
    elif n == 2:
        ex2()
    elif n == 3:
        ex3()
    else:
        print(f"There are not example {n}.\nSo here is all examples")
        ex1()
        ex2()
        ex3()


which_example()

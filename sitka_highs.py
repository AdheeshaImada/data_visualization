import csv
from matplotlib import pyplot as plt
from datetime import datetime

f1 = "data/sitka_weather_07-2021_simple.csv"
#f2 = "data/sitka_weather_2021_simple.csv"
f2 = "data/death_valley_2021_simple.csv"

while True:
    fl = input("Only a July month(m) or entire year(y): ")
    if fl == "m":
        filename = f1
        ttl = "Daily high temperatures of Sitka, July 2021"
        break
    elif fl == "y":
        filename = f2
        ttl = "Daily high temperatures of Sitka 2021"
        break
    else:
        print("Enter valid input!")
        continue

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()


def basic():
    # basic reading csv file
    # get headers as a list
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)


def second():
    # get headers one at a time with their index
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)


def third():
    # get rows from csv file
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get high temperatures from this file.
        highs = []
        for row in reader:
            high = int(row[4])
            highs.append(high)

        print(highs)


def fourth():
    # get rows from csv file and draw chart
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get high temperatures and date from this file.
        highs = []
        dates = []
        for row in reader:
            high = int(row[4])
            highs.append(high)
            date = datetime.strptime(row[2], "%Y-%m-%d")
            dates.append(date)

        # Use scatter only for monthly data and change linewidth according to the data set
        # because otherwise chart looks like a mess.
        if fl == "m":
            ax.plot(dates, highs, c="Red", linewidth=2)
            ax.scatter(dates, highs, c="Red", s=100)
        else:
            ax.plot(dates, highs, c="Red", linewidth=1)
        ax.set_title(ttl, fontsize=14)
        ax.set_xlabel('Date', fontsize=10)
        fig.autofmt_xdate()
        ax.set_ylabel('Temperature(F)', fontsize=10)
        ax.tick_params(axis='both', which="major", labelsize=10)
        plt.show()


print("if you want to quit press 'q'.")

while True:
    function = input("function which want to run: ")
    if function == "q":
        break
    if function == "1":
        basic()
    elif function == "2":
        second()
    elif function == "3":
        third()
    elif function == "4":
        fourth()
    else:
        continue

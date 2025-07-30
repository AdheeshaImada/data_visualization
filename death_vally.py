import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/death_valley_2021_simple.csv"

with open(filename) as fl:
    reader = csv.reader(fl)
    headers = next(reader)

    for index, head in enumerate(headers):
        print(index, head)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
ax.plot(dates, lows, c="blue", linewidth=1, alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="brown", alpha=0.1)

ax.set_title("Temperature of Death vally, California", fontsize=14)
ax.set_xlabel("day", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("temperature", fontsize=10)
ax.tick_params(axis="both", which="major", labelsize=10)

plt.show()

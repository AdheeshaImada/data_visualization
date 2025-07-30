import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = "data/sitka_weather_2021_simple.csv"

with open(filename) as fl:
    reader = csv.reader(fl)
    headers = next(reader)

    # Get high, low temperature and date from file
    highs, lows, dates = [], [], []
    for row in reader:
        high = int(row[4])
        low = int(row[5])
        date = datetime.strptime(row[2], "%Y-%m-%d")
        highs.append(high)
        lows.append(low)
        dates.append(date)

plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots()

ax.plot(dates, highs, c="Red", linewidth=1, alpha=0.5)
ax.plot(dates, lows, c="Blue", linewidth=1, alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("low and high temperature of sitka through out year", fontsize=18)
ax.set_xlabel("Date", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Temperature", fontsize=10)
ax.tick_params(axis="both", which="major", labelsize=8)
plt.show()

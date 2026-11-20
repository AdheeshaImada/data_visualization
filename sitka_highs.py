"""Explore daily highs for Sitka (July or full-year 2021)."""
import csv
import matplotlib.pyplot as plt
from weather_data import DATA_DIR, load_temperatures

MONTHLY = DATA_DIR / "sitka_weather_07-2021_simple.csv"
YEARLY = DATA_DIR / "sitka_weather_2021_simple.csv"


def show_highs(filename, title, monthly=False):
    dates, highs = load_temperatures(filename)
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, linewidth=2 if monthly else 1)
    if monthly:
        ax.scatter(dates, highs, s=30)
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°F)")
    fig.autofmt_xdate()
    fig.tight_layout()
    plt.show()


def main():
    while True:
        period = input("July only (m), full year (y), or quit (q): ").strip().lower()
        if period == "q":
            return
        if period in ("m", "y"):
            break
        print("Enter m, y, or q.")
    filename = MONTHLY if period == "m" else YEARLY
    title = "Daily high temperatures — Sitka, July 2021" if period == "m" else "Daily high temperatures — Sitka, 2021"
    while True:
        function = input("1=Headers, 2=Indexed headers, 3=Values, 4=Chart, q=Quit: ").strip().lower()
        if function == "q":
            break
        if function in ("1", "2"):
            with filename.open(newline="", encoding="utf-8-sig") as handle:
                headers = next(csv.reader(handle))
            print(headers if function == "1" else list(enumerate(headers)))
        elif function == "3":
            _, highs = load_temperatures(filename)
            print(highs)
        elif function == "4":
            show_highs(filename, title, monthly=period == "m")
        else:
            print("Choose 1, 2, 3, 4 or q.")


if __name__ == "__main__":
    main()

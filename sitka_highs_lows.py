"""Plot Sitka daily highs and lows throughout 2021."""
import matplotlib.pyplot as plt
from weather_data import DATA_DIR, load_temperatures


def main():
    dates, highs, lows = load_temperatures(DATA_DIR / "sitka_weather_2021_simple.csv", include_lows=True)
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, linewidth=1, alpha=0.65, label="High")
    ax.plot(dates, lows, linewidth=1, alpha=0.65, label="Low")
    ax.fill_between(dates, highs, lows, alpha=0.12)
    ax.set_title("Daily high and low temperatures — Sitka, 2021")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°F)")
    ax.legend()
    fig.autofmt_xdate()
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

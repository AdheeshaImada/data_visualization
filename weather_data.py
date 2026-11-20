"""Load NOAA-style CSV weather records included with this project."""
import csv
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


def load_temperatures(csv_path, include_lows=False):
    """Return (dates, highs) or (dates, highs, lows), omitting missing data.

    Dates and temperatures are read by header name, not by column position.
    """
    csv_path = Path(csv_path)
    dates, highs, lows = [], [], []
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"DATE", "TMAX"}
        if include_lows:
            required.add("TMIN")
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(f"{csv_path.name} must have columns {sorted(required)}")
        for line, row in enumerate(reader, start=2):
            try:
                date = datetime.strptime(row["DATE"], "%Y-%m-%d")
                high = int(row["TMAX"])
                low = int(row["TMIN"]) if include_lows else None
            except (ValueError, TypeError, KeyError):
                print(f"Skipping row {line} in {csv_path.name}: missing or invalid value")
                continue
            dates.append(date)
            highs.append(high)
            if include_lows:
                lows.append(low)
    if not dates:
        raise ValueError(f"No valid temperature records in {csv_path}")
    return (dates, highs, lows) if include_lows else (dates, highs)

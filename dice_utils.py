"""Shared dice simulation and input helpers."""
from collections import Counter
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def read_int(prompt, minimum=1, maximum=None):
    """Ask repeatedly until the user provides a valid integer."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value < minimum or (maximum is not None and value > maximum):
            condition = f"from {minimum} to {maximum}" if maximum is not None else f"at least {minimum}"
            print(f"Please enter a number {condition}.")
            continue
        return value


def simulate(dice, rolls):
    """Return (possible totals, frequencies) from rolling one or more dice."""
    if not dice:
        raise ValueError("Supply at least one die")
    if rolls < 1:
        raise ValueError("Rolls must be positive")
    counter = Counter(sum(die.roll() for die in dice) for _ in range(rolls))
    totals = list(range(len(dice), sum(d.num_sides for d in dice) + 1))
    return totals, [counter.get(total, 0) for total in totals]


def export_figure(fig, filename):
    """Create a self-contained HTML chart in the outputs folder."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT_DIR / filename
    fig.write_html(str(destination), include_plotlyjs=True, auto_open=False)
    print(f"Saved chart: {destination}")
    return destination

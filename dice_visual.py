"""Simulate two dice and generate a Plotly bar chart."""
import plotly.graph_objects as go
from die import Die
from dice_utils import export_figure, read_int, simulate


def main():
    sides_1 = read_int("Number of sides in die 1: ", minimum=2)
    sides_2 = read_int("Number of sides in die 2: ", minimum=2)
    rolls = read_int("Number of rolls: ", minimum=1)
    totals, frequencies = simulate([Die(sides_1), Die(sides_2)], rolls)
    fig = go.Figure(data=[go.Bar(x=totals, y=frequencies)])
    fig.update_layout(
        title=f"Results of rolling D{sides_1} and D{sides_2} {rolls} times",
        xaxis_title="Total rolled",
        yaxis_title="Frequency",
    )
    fig.update_xaxes(dtick=1)
    export_figure(fig, f"d{sides_1}_d{sides_2}.html")


if __name__ == "__main__":
    main()

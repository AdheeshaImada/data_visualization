"""Plot the outcomes of rolling one six-sided die 1,000 times."""
import plotly.graph_objects as go
from die import Die
from dice_utils import simulate, export_figure


def main():
    totals, frequencies = simulate([Die()], rolls=1000)
    fig = go.Figure(data=[go.Bar(x=totals, y=frequencies)])
    fig.update_layout(title="Results of rolling one D6 1,000 times",
                      xaxis_title="Die face", yaxis_title="Frequency")
    fig.update_xaxes(dtick=1)
    export_figure(fig, "d6.html")


if __name__ == "__main__":
    main()

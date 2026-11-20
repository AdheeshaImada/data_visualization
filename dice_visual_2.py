"""Roll 1–10 dice and save either a bar chart or a pie chart."""
import plotly.graph_objects as go
from die import Die
from dice_utils import export_figure, read_int, simulate


def main():
    while True:
        chart = input("Bar chart (b) or pie chart (p): ").strip().lower()
        if chart in ("b", "p"):
            break
        print("Enter b or p.")

    count = read_int("Number of dice (1–10): ", minimum=1, maximum=10)
    dice = [Die(read_int(f"Number of sides in die {i + 1}: ", minimum=2))
            for i in range(count)]
    rolls = read_int("Number of rolls: ", minimum=1)
    totals, frequencies = simulate(dice, rolls)
    if chart == "b":
        fig = go.Figure(data=[go.Bar(x=totals, y=frequencies)])
        fig.update_layout(xaxis_title="Total rolled", yaxis_title="Frequency")
        fig.update_xaxes(dtick=1)
    else:
        fig = go.Figure(data=[go.Pie(labels=[str(x) for x in totals], values=frequencies)])
    title = ", ".join(f"D{die.num_sides}" for die in dice)
    fig.update_layout(title=f"Results of rolling {title} ({rolls} times)")
    filename = "_".join(f"d{die.num_sides}" for die in dice)
    export_figure(fig, f"{filename}_{'bar' if chart == 'b' else 'pie'}.html")


if __name__ == "__main__":
    main()

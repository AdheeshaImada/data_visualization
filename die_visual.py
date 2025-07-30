from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create D6
die = Die()

# Do some rolls and store results in alist
die_results = []
for roll_num in range(1000):
    result = die.roll()
    die_results.append(result)

# Analise the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = die_results.count(value)
    frequencies.append(frequency)

# Visualise the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results'}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, "layout": my_layout}, filename='d6.html')

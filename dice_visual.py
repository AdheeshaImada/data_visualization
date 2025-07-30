from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two D6

s_1 = int(input('Number of sides in die 01: '))
s_2 = int(input('Number of sides in die 02: '))

rolls = int(input('Number of rolls: '))

die_1 = Die(s_1)
die_2 = Die(s_2)

# Do some rolls and store results in alist
results = []
for roll_num in range(rolls):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analise the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title=f'Results of rolling D{s_1}, D{s_2} {rolls} times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, "layout": my_layout}, filename=f'd{s_1}_d{s_2}.html')

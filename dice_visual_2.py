from die import Die
from plotly.graph_objs import Bar, Layout, Pie
from plotly import offline

# Create two D6
chart = input("Bar chart(b) or Pie chart(p): ")
while True:
    num_of_die = int((input('Number of die you want to use: ')))
    if num_of_die <= 10:
        break
    else:
        print("Maximum number of die is 10 !")

die_number = ['die_1', 'die_2', 'die_3', 'die_4', 'die_5', 'die_6', 'die_7', 'die_8', 'die_9', 'die_10']
dies = []
for die in range(num_of_die):
    sides = int(input(f'Number of sides in die {die + 1}: '))
    die_number[die] = Die(sides)
    dies.append(die_number[die])

rolls = int(input('Number of rolls: '))

# Do some rolls and store results in alist
results = []
for roll_num in range(rolls):
    result = 0
    for d in dies:
        result += d.roll()
    results.append(result)


# Analise the results
frequencies = []
max_result = 0
min_result = 0
for d in dies:
    max_result += d.num_sides
    min_result += 1
for value in range(min_result, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results
x_values = list(range(min_result, max_result+1))
if chart == 'b':
    data = [Bar(x=x_values, y=frequencies)]
else:
    data = [Pie(labels=x_values, values=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}
# Generate title for layout and name for file
ds = ""
dsf = ""
for d in dies:
    d_s = d.num_sides
    ds = ds + f"D{d_s},"
    dsf = dsf + f"d{d_s}_"
# Remove ',' and '_' from end of the title and file name respectively
ds = f"{len(dies)} dies ({ds[0: -1]})"
dsf = dsf[0: -1]
my_layout = Layout(title=f'Results of rolling {ds}  {rolls} times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, "layout": my_layout}, filename=f'{dsf}.html')

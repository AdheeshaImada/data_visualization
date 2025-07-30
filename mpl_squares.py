import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squire = [1, 4, 9, 16, 25]

# just for check what are the available styles
print(plt.style.available)

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()
ax.plot(input_value, squire, linewidth=3)

ax.set_title("squire number", fontsize=14)
ax.set_xlabel("value", fontsize=10)
ax.set_ylabel("squire", fontsize=10)

ax.tick_params(axis='both', labelsize=10)

plt.show()

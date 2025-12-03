import matplotlib.pyplot as plt
import numpy as np

# Common styles for the lines and markers
common_styles = dict(
    marker=".",
    markerSize=20,
    linestyle='dotted',
    linewidth=3
)

# x & y coordinates
x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

# Title of the line graph
plt.title("Class size", fontsize="24", fontweight='bold',
          family='Consolas', color='#0a1cca')

# x label of the line graph
plt.xlabel("Year", fontsize='18', fontweight='bold',
           family='Consolas', color='#409fe7')

# y label of the line graph
plt.ylabel("Students", fontsize='18', fontweight='bold',
           family='Consolas', color='#409fe7')

# change colors of tick values
plt.tick_params(axis="both", colors="#6cafc6")

# to make the x ticks only show at the x coordinates
plt.xticks(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()

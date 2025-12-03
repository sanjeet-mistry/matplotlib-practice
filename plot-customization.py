import matplotlib.pyplot as plt
import numpy as np

colors = np.array([
    dict(markerfacecolor='#176f25',
         markeredgecolor='#1a281c',
         color="#1a281c"),
    dict(markerfacecolor="#f66764",
         markeredgecolor="#871111",
         color="#871111"),
    dict(markerfacecolor='#79bfe0',
         markeredgecolor="#156782",
         color="#156782"),
])

y = np.array([
    np.array([15, 25, 30, 20]),
    np.array([17, 23, 38, 5]),
    np.array([13, 15, 20, 30])
])

plotstyle = dict(marker=".",
                 markersize="30",
                 linestyle='dashed',
                 linewidth=3,
                 )

x = np.array([2023, 2024, 2025, 2026])

for i in np.arange(len(colors)):
    plt.plot(x, y[i], **plotstyle, **colors[i])

plt.show()

import matplotlib.pyplot as plt
import numpy as np

plot_styles = dict(
    marker="o",
    markersize=10,
    linewidth='2'
)

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 10, 15, 20, 25])

plt.plot(x, y, **plot_styles)
plt.grid(linestyle='dashed')
plt.show()

import matplotlib.pylab as plt
import numpy as np

# Figure = The entire canvas
# Axes = A single plot
x = np.array([1, 2, 3, 4, 5])

figure, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, x * 2, color='red')
axes[0, 0].set_title("x * 2")

axes[0, 1].plot(x, x * 3 + 3, color='blue')
axes[0, 1].set_title("x * 3 + 3")

axes[1, 0].plot(x, x ** 2, color='green')
axes[1, 0].set_title("x ** 2")

axes[1, 1].plot(x, x ** 3, color='yellow')
axes[1, 1].set_title("x ** 3")

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"]
values = [4, 3, 2, 5, 3, 1]

plt.bar(categories, values)
plt.title("Daily Consumption", fontsize=22, fontweight='bold')
plt.xlabel("Food", fontsize=18, fontweight='bold')
plt.ylabel("Quantity", fontsize=18, fontweight='bold')
plt.show()

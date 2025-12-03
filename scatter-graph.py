import matplotlib.pyplot as plt

# Scatter graph = Shows the relationship between two variables
#                 Helps to identify a correlation (+, -, None)
#                 Example: Study hours vs Test scores

x1 = [0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]  # Hours studied
y1 = [55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]  # Grades

x2 = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]  # Hours studied
y2 = [50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97]  # Grades

plt.xlabel("Hours studied", fontsize=16, fontweight='bold')
plt.ylabel("Grades", fontsize=16, fontweight='bold')
plt.title("Test scores", fontsize=22, fontweight='bold')
plt.scatter(x1, y1, color='red', alpha=.8, s=100, label='Class A')
plt.scatter(x2, y2, color='green', s=100, label='Class B')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Histogram = A visual representation of the distribution of quantitative data.
#             They group values into bins (intervals)
#             and count how many fall in each range

test_scores = np.random.normal(loc=70, scale=20, size=100)
test_scores = np.clip(test_scores, 0, 100)
plt.hist(test_scores, bins=10, color="lightblue", edgecolor='black')
plt.title("Exam Scores", fontsize=24, fontweight='bold')
plt.xlabel("Score", fontsize=16, fontweight='bold')
plt.ylabel("No. of Students", fontsize=16, fontweight='bold')
plt.show()

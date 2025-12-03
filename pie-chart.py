import matplotlib.pyplot as plt

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = [300, 250, 275, 200]
colors = ["#208d7d", "#ca1515", "#0a54da", "#d6c815"]

plt.pie(values,
        labels=categories,
        autopct="%1.1f%%",
        colors=colors,
        explode=[0, 0, 0, .1],
        shadow=True)
plt.title("College", fontsize=24, fontweight='bold')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("./data/pokemons.csv")

type1_count = df["Type1"].value_counts()

plt.pie(type1_count.values, labels=type1_count.index, autopct="%1.1f%%")
plt.show()

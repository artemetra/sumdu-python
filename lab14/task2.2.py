import numpy as np
import matplotlib.pyplot as plt
from data import *

plt.figure(figsize=(10, 4))
plt.bar(years, ukraine_data, width=0.4, label="Ukraine", align="center")
plt.bar(years, sweden_data, width=0.4, label="Sweden", align="edge")
plt.title("Gini index", fontsize=15)
plt.xlabel("Year", fontsize=12, color="red")
plt.ylabel("Gini", fontsize=12, color="red")
plt.legend()
plt.show()

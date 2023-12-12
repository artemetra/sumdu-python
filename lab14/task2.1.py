import numpy as np
import matplotlib.pyplot as plt
from data import *

plt.plot(years, sweden_data, label="Ukraine", color="blue")
plt.plot(years, ukraine_data, label="Sweden", color="yellow")
plt.title("Gini index", fontsize=15)
plt.xlabel("Year", fontsize=12, color="red")
plt.ylabel("Gini", fontsize=12, color="red")
plt.legend()
plt.grid(True)
plt.show()

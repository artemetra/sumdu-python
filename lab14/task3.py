import numpy as np
import matplotlib.pyplot as plt
from data import *

fig, ax = plt.subplots()
ax.pie(ukraine_data, labels = years)
ax.axis("equal")
plt.legend() 
plt.show()
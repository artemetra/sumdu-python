import matplotlib.pyplot as plt

import numpy as np

# Y(x)=x^sin(10*x), x=[1...10]
x = np.linspace(1, 10, 51)
y = x ** (np.sin(10 * x))

plt.plot(x, y, label="x^sin(10*x)", color="red", linewidth=5)

plt.title("Графік Y(x)=x^sin(10*x), x=[1...10]", fontsize=15)

plt.xlabel("x", fontsize=12, color="blue")
plt.ylabel("y", fontsize=12, color="blue")
plt.legend()
plt.grid(True)
plt.show()

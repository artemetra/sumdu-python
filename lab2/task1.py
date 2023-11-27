import math
import task2

x = float(input("x: "))
y = float(input("y: "))

def expression(x,y):
    z = (math.cos(x))**2 + (math.sin(y))**2
    return z

print("expression:", expression(x,y))

while True:
    N = int(input("N: "))
    if N < 1:
        print("N не може бути менше одиниці.")
        continue
    
    print("Сума чисел від 1 до N:",task2.sum_to(N))
    break

import math

n = int(input("Введіть N: "))
arr = [float(input()) for _ in range(n)]
minimum = math.inf

for i in arr:
    if 0 < i < minimum:
        minimum = i

print("Найменший додатній елемент:", minimum)
while True:
    a = float(input("Введіть a:"))
    if not (1 <= a <= 100):
        print("Число `a` не у діапазоні від 1 до 100, спробуйте ще раз.")
        continue
    break
while True:
    b = float(input("Введіть b:"))
    if not (1 <= b <= 100):
        print("Число `b` не у діапазоні від 1 до 100, спробуйте ще раз.")
        continue
    break

if a > b:
    X = b / a + 61
elif a == b:
    X = -5
else:
    X = (b - a) / b

print("X =", X)

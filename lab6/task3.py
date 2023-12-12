from collections import Counter


def no_less_than_twice():
    s = input("Введіть рядок з латинських літер: ")
    counter = Counter(s)
    new_s = "".join(c for c in s if counter[c] >= 2)
    print("Новий рядок:", new_s)


no_less_than_twice()

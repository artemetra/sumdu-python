s = input("Введіть рядок: ")
new_str = "".join(c for c in s if c.isalpha())
print("Новий рядок:", new_str)
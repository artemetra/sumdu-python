while True:
    s = input("Введіть рядок: ")
    if len(s) >= 2:
        break
    print("Рядок закороткий! Спробуйте знову..")

print("Передостанній символ:", s[-2])
heights = {
    "Ellie Clarson": (173, "F"),
    "Ben Jenkins": (170, "M"),
    "Tom Smith": (162, "M"),
    "Julie Rose": (183, "F"),
    "Kirill Sawyer": (151, "F"),
    "Jimmy Kim": (179, "M"),
    "Kylie Johnes": (165, "M"),
    "James Jennar": (191, "M"),
    "Lisa Groot": (169, "F"),
    "Alan Alison": (159, "M"),
}


def print_dict(d: dict):
    for k, v in d.items():
        print(k, ":", v)


def add_kv(d: dict, k, v):
    d[k] = v
    print("Додано", k, ":", v)


def print_sorted(d):
    sd = {k: d[k] for k in sorted(d)}
    print("Відсортований словник: ")
    print_dict(sd)


def delete_key(d, k):
    del d[k]
    print("Видалено", k, ".")


def avg_height_men(d):
    arr = [person[0] for person in d.values() if person[1] == "M"]
    print("Середня висота чоловіків:", sum(arr) / len(arr))


while True:
    print("0: Вийти")
    print("1: Переглянути словник")
    print("2: Додати значення")
    print("3: Видалити значення")
    print("4: Переглянути словник за відсортованими значеннями")
    print("5: Знайти значення середньої висоти чоловіків")

    match input(">>"):
        case "0":
            print("Дякую за використання")
            break
        case "1":
            print_dict(heights)
        case "2":
            name = input("Введіть імʼя та призвіще: ")
            height = int(input("Введіть висоту: "))
            gender = input("Введіть стать (F/M): ").upper()
            add_kv(heights, name, (height, gender))
        case "3":
            name = input("Введіть імʼя яке треба видалити: ")
            delete_key(heights, name)
        case "4":
            print_sorted(heights)
        case "5":
            avg_height_men(heights)

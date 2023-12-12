import json
import sys
from pprint import pprint

heights = [
    {"Name": "Ellie Clarson", "Height": 173, "Gender": "F"},
    {"Name": "Ben Jenkins", "Height": 170, "Gender": "M"},
    {"Name": "Tom Smith", "Height": 162, "Gender": "M"},
    {"Name": "Julie Rose", "Height": 183, "Gender": "F"},
    {"Name": "Kirill Sawyer", "Height": 151, "Gender": "F"},
    {"Name": "Jimmy Kim", "Height": 179, "Gender": "M"},
    {"Name": "Kylie Johnes", "Height": 165, "Gender": "M"},
    {"Name": "James Jennar", "Height": 191, "Gender": "M"},
    {"Name": "Lisa Groot", "Height": 169, "Gender": "F"},
    {"Name": "Alan Alison", "Height": 159, "Gender": "M"},
]

FILENAME = "data.json"
RESULT_FILENAME = "data2.json"

json_data = json.dumps(heights)
with open(FILENAME, "w") as f:
    f.write(json_data)


def print_json(filename: str):
    with open(filename, "r") as f:
        data = json.loads(f.read())
        pprint(data)


def add_record(filename: str, name: str, height: int, gender: str):
    with open(filename, "r") as f:
        data = list(json.loads(f.read()))
        data.append({"Name": name, "Height": height, "Gender": gender})
    with open(filename, "w") as f:
        f.write(json.dumps(data))
    print("Додано!")


def delete_record(filename: str, name: str):
    with open(filename, "r") as f:
        data = list(json.loads(f.read()))
        new_data = [entry for entry in data if entry["Name"] != name]
        n = len(data) - len(new_data)
    with open(filename, "w") as f:
        f.write(json.dumps(new_data))
    print(f"Видалено {n} поле!" if n == 1 else f"Видалено {n} полей!")


def avg_height_men(filename_in: str, filename_out: str):
    men_heights = []
    with open(filename_in, "r") as f:
        data = list(json.loads(f.read()))
        for elem in data:
            if elem["Gender"] == "M":
                men_heights.append(elem["Height"])
    avg_height = sum(men_heights) / len(men_heights)
    with open(filename_out, "w") as f:
        f.write(json.dumps({"AverageHeightMen": avg_height}))
    print(f"Результат надруковано у {filename_out}.")


def get_record(filename: str, name: str):
    results = []
    with open(filename, "r") as f:
        data = list(json.loads(f.read()))
        for elem in data:
            if elem["Name"] == name:
                results.append(elem)
    return results


while True:
    print("0: Вийти")
    print("1: Переглянути файл JSON")
    print("2: Додати поле")
    print("3: Видалити поле")
    print("4: Переглянути поле за ключем")
    print("5: Знайти значення середньої висоти чоловіків")

    match input(">>"):
        case "0":
            print("Дякую за використання")
            sys.exit()
        case "1":
            print_json(FILENAME)
        case "2":
            name = input("Введіть імʼя та призвіще: ")
            height = int(input("Введіть висоту: "))
            gender = input("Введіть стать (F/M): ").upper()
            add_record(FILENAME, name, height, gender)
        case "3":
            name = input("Введіть імʼя яке треба видалити: ")
            delete_record(FILENAME, name)
        case "4":
            name = input("Введіть імʼя яке треба шукати: ")
            results = get_record(FILENAME, name)
            for result in results:
                pprint(result)
        case "5":
            avg_height_men(FILENAME, RESULT_FILENAME)

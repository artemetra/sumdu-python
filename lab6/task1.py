def insert_at_even():
    arr = [int(i) for i in input("Введіть масив: ").split()]
    print("Список:", arr)
    for idx, _ in enumerate(arr):
        if idx % 2:
            continue
        arr[idx] = int(input(f"Введіть елемент, індекс {idx}: "))
    print("Новий список", arr)

insert_at_even()

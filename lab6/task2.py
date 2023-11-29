def swap_even_odd():
    arr = input("Введіть список: ").split()
    new_arr = []
    for e, o in zip(arr[::2], arr[1::2]):
        new_arr.append(o)
        new_arr.append(e)
    print("Новий список:", " ".join(new_arr))
    
swap_even_odd()

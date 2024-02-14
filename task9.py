def read_and_sort_strings():
    num_strings = int(input("Введите количество строк: "))
    strings = []
    for i in range(num_strings):
        string = input("Введите строку : ")
        strings.append(string)

    # Сортировка списка по длине строк
    sorted_strings = sorted(strings, key=len)

    return sorted_strings


sorted_strings = read_and_sort_strings()


print("Отсортированный список по длине строк:")
for string in sorted_strings:
    print(string)

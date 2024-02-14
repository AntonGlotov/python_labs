def sort_string():
    num_strings = int(input("Введите количество строк: "))
    strings = []
    for i in range(num_strings):
        string = input("Введите строку : ")
        strings.append(string)

    # Сортировка списка по длине строк
    sorted_strings = sorted(strings, key=len)

    return sorted_strings


sorted_strings = sort_string()


print("Отсортированный список по длине строк:")
for string in sorted_strings:
    print(string)

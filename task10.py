def sort_string():
    num_strings = int(input("Введите количество строк: "))
    strings = []
    for i in range(num_strings):
        str1 = input(f"Введите строку : ")
        strings.append(str1)
    sorted_strings = sorted(strings, key=lambda x: len(x.split()))

    return sorted_strings


sorted_strings = sort_string()

print("\nОтсортированный список по количеству слов в строке:")
for string in sorted_strings:
    print(string)

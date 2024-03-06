print("Введите количество строк: ")
n = int(input())
strings = []
for i in range(n):
    print("Введите строку")
    string = input()
    strings.append(string)

strings = sorted(strings, key=len)

print("\nВывод: ")
for string in strings:
    print(string)


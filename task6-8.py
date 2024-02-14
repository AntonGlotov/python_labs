def is_russian(symb):
    russian_code = [ord('А'), ord('я')]
    if russian_code[0] < ord(symb) < russian_code[1]:
        return True
    return False


def count_russian(sentence):
    count = 0
    for i in sentence:
        if is_russian(i):
            count += 1
    return count


def str_symb_lat(sentence):
    result = []
    str_lat = [ord('a'), ord('z')]
    for i in sentence:
        if str_lat[0] < ord(i) < str_lat[1]:
            result.append(i)
    return result


def str_min_number(sentence):
    mn = '9'
    for i in sentence:
        if ord('0') < ord(i) < ord('9') and ord(i) < ord(mn):
            mn = i
    return mn


print("1 - Посчитать количество русских символов в строке\n"
      "2 - Найти все строчные латинские символы строки\n"
      "3 - Найти минимальное из имеющихся в строке целых чисел\n"
      "Выберите, чем хотите заняться:")

number = int(input())

if number == 1:
    print("Напишите свое предложение: ")
    print(count_russian(input()))
elif number == 2:
    print("Напишите свое предложение: ")
    print(str_symb_lat(input()))
elif number == 3:
    print("Напишите свое предложение: ")
    print(str_min_number(input()))

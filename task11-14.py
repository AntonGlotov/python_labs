# Для задачи 3,5
# Найти самый часто встречаемы символ в строке
def sentences(sentence):
    char_counts = {}
    for i in sentence:
        if i not in char_counts:
            char_counts[i] = 1
        else:
            char_counts[i] += 1
    s = max(char_counts, key=char_counts.get)
    return s


# Найти самый часто встречаемы символ в строках
def sentences1(sentence):
    char_counts = {}
    for i in sentence:
        for j in i:
            if j not in char_counts:
                char_counts[j] = 1
            else:
                char_counts[j] += 1
    return char_counts


# Количество вхождений символа в строку
def find_in_all(s, c):
    count = 0
    for i in s:
        for j in i:
            if s[i][j] == c:
                count += 1
    return count


# Количество вхождений символа в строки
def find_all(a):
    count = 0
    for i in a:
        count += len(i)
    return count


#
def max_str(c, a):
    count = 0
    for i in a:
        if i == c:
            count += 1
    return count


# Находим колчество символов в строке
def count_chars_in_list(list):
    count = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            count += 1
    return count


# Возвращает частоту вхождения символа в строку
def frequency_in_str(s, c):
    count = 0
    for i in range(len(s)):
        if s[i] == c:
            count += 1
    return count / len(s)


# Самый частый символ
def sup_find_symb(list):
    charfrequency = {}
    for string in list:
        for char in string:
            if char in charfrequency:
                charfrequency[char] += 1
            else:
                charfrequency[char] = 1
    rt = max(charfrequency, key=charfrequency.get)
    return rt, charfrequency[rt]


# Проверка на гласную
def is_vowel(symb):
    russian_code = [ord('А'), ord('я')]
    vowels = [ord('А'), ord('О'), ord('У'), ord('Е'), ord('И'), ord('Э'), ord('Ю'), ord('Я')]
    for i in range(len(vowels)):
        vowels.append(vowels[i] + 32)
    if ord(symb) in vowels:
        return True
    return False


def count_vowel_consonant(s):
    count = 0
    for i in range(len(s) - 1):
        if is_vowel(s[i]) and not is_vowel(s[i + 1]):
            count += 1
    return count


def count_consonant_vowel(s):
    count = 0
    for i in range(len(s) - 1):
        if not is_vowel(s[i]) and is_vowel(s[i + 1]):
            count += 1
    if count != 0:
        return count
    else:
        return 1


# 3 В порядке увеличения разницы между частотой наиболее часто
# встречаемого символа в строке и частотой его появления в алфавите.
string1 = []
a = input('Введите строку: ')
while a != '0':
    string1.append(a)
    a = input('Введите строку: ')
c = sentences1(string1)
d = find_all(string1)
str1 = string1
print('Упорядоченный список(для 3):')
string1.sort(key=lambda x: (max_str(sentences(x), x) / len(x) - c[sentences(x)] / d))
print(string1)
print('Частоты списка:')
for i in range(0, len(string1)):
    print((max_str(sentences(string1[i]), string1[i]) / len(string1[i]) - c[sentences(string1[i])] / d))

# 5 В порядке увеличения частоты квадратичного отклонения
# встречаемости самого часто встречаемого в строке символа от частоты его
# встречаемости в текстах на этом алфавите.
print('Упорядоченный список(для 5):')
string1.sort(key=lambda x: (max_str(sentences(x), x) / len(x) - (c[sentences(x)] / d)) ** 2)
print(string1)
print('Частоты списка:')
for i in range(0, len(string1)):
    print((max_str(sentences(string1[i]), string1[i]) / len(string1[i]) - (c[sentences(string1[i])] / d)) ** 2)

# 7 В порядке увеличения разницы между количеством сочетаний
# «гласная-согласная» и «согласная-гласная» в строке.
print('Упорядоченный список(для 7):')
string1.sort(key=lambda x: (count_vowel_consonant(x) / count_consonant_vowel(x)))
print(string1)

# 12 В порядке увеличение квадратичного отклонения частоты
# встречаемости самого распространенного символа в наборе строк от частоты
# его встречаемости в данной строке.
c = sentences1(string1)
d = find_all(string1)
str1 = string1
print('Упорядоченный список(для 12):')
string1.sort(key=lambda x: (max_str(sentences(x), x) / len(x) - c[sentences(x)] / d))
print(string1)

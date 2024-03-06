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



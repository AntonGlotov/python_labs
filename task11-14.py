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



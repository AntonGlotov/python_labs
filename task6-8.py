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



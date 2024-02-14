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


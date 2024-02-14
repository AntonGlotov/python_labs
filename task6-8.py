def is_russian(symb):
    russian_code = [ord('А'), ord('я')]
    if russian_code[0] < ord(symb) < russian_code[1]:
        return True
    return False

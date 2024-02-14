import random


def shuffle(s1):
    words = s1.split()
    random.shuffle(words)
    s1 = ' '.join(words)
    return s1

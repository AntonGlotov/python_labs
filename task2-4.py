import random
sentence = "раз два три четыре пять шесть семь восемь"


def shuffle(s1):
    words = s1.split()
    random.shuffle(words)
    s1 = ' '.join(words)
    return s1


def count_even_words(s2):
    words = s2.split()
    count = 0
    for i in words:
        if len(i) % 2 == 0:
            count += 1
    return count

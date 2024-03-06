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


def flag_sort(colors):
    sorted_colors = sorted(colors, key=lambda x: x[1])
    color = ' '.join(sorted_colors)
    return color


print("1 - Перемешать слова в предложении\n"
      "2 - Посчитать количество слов в предложении с четным количеством символов\n"
      "3 - Отсортировать цвета в порядке флага России\n"
      "Выберите, чем хотите заняться:")

number = int(input())

if number == 1:
    print("Напишите свое предложение: ")
    print(shuffle(input()))
elif number == 2:
    print("Напишите свое предложение: ")
    print(count_even_words(input()))
elif number == 3:
    print("Напишите цвета через пробел: ")
    color = input().split()
    print(flag_sort(color))

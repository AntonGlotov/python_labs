from math import sqrt


def isprime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def max_isprime_divide(x):
    mx = 1
    for i in range(2, int(x / 2)):
        if x % i == 0 & isprime(i):
            mx = i
    return mx


def function2(x):
    temp = [int(x) for x in str(x)]
    pr = 1

    for i in temp:
        if i % 5 != 0:
            pr *= i
    return pr


def function3(x):
    temp = [int(x) for x in str(x)]
    pr = 1

    for i in temp:
        pr *= i

    mx = 1
    for i in range(1, int(x / 2), 2):
        if x % i == 0 and not isprime(i):
            mx = i

    while mx != 0:
        pr, mx = mx, pr % mx

    return pr


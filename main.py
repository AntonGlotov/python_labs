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
    list = [int(x) for x in str(x)]
    pr = 1

    for i in list:
        if i % 5 != 0:
            pr *= i
    return pr


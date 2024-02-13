from math import sqrt


def isprime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


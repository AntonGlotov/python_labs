def glob_max(massive, index):
    for i in range(len(massive)):
        if massive[i] > massive[index]:
            return False
    return True


def loc_min(massive, index):
    if massive[index - 1] > massive[index] < massive[index + 1]:
        return True
    return False


def shift_mass(massive):
    temp = massive[0]
    for i in range(0, len(massive) - 1):
        massive[i] = massive[i+1]
    massive[len(massive) - 1] = temp
    return massive

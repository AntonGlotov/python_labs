def glob_max(massive, index):
    for i in range(len(massive)):
        if massive[i] > massive[index]:
            return False
    return True


def loc_min(massive, index):
    if massive[index - 1] > massive[index] < massive[index + 1]:
        return True
    return False



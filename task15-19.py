def glob_max(massive, index):
    for i in range(len(massive)):
        if massive[i] > massive[index]:
            return False
    return True


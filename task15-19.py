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


def print_mass_ch_nch(massive):
    list1 = []
    list2 = []
    for i in massive:
        list1.append(i) if i % 2 == 0 else list2.append(i)
    print(list1)
    print(list2)


def oper_with_list(list):
    L1 = []
    L2 = []
    for i in list:
        if i not in L1:
            L1.append(i)
    for i in L1:
        L2.append(list.count(i))
    return L1, L2


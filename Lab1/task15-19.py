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


print("1 - Проверить, является ли i-ый элемент глобальным максимумом списка\n"
      "2 - Проверить, является ли i-ый элемент списка локальным минимумом\n"
      "3 - Осуществить циклический сдвиг элементов массива влево\n"
      "4 - Вывести сначала четные потом нечетные элементы массива\n"
      "5 - Построить два списка, в первом будут неповторяющиеся элементы исходного списка,\n"
      "    а во втором будет количество, сколько раз элемент первого встретился в исходном\n"
      "Выберите, чем хотите заняться:")

number = int(input())

print("Введите список: ")
mass = input()
mass = mass.split()
mass = [int(i) for i in mass]

if number == 1:
    print("Введите номер элемента")
    print(glob_max(mass, int(input())))
elif number == 2:
    print("Введите номер элемента")
    print(loc_min(mass, int(input())))
elif number == 3:
    print(shift_mass(mass))
elif number == 4:
    print_mass_ch_nch(mass)
elif number == 5:
    l1, l2 = oper_with_list(mass)
    print(l1)
    print(l2)
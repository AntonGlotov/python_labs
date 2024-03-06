election_list = 'McCain 10 McCain 5 Obama 9 Obama 8 McCain 1 Obama 10 McCain 10'
candidates = election_list.split()

dict = {}
for i in range(0, len(candidates), 2):
    if candidates[i] not in dict:
        dict[candidates[i]] = candidates[i + 1]
    else:
        dict[candidates[i]] = int(candidates[i + 1]) + int(dict[candidates[i]])
print(dict)

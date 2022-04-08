list = list(map(int, input('nhap day so: ').split()))
sp_list = [0] * len(list)
new_list = []


def check(a, b):
    if list[a] < list[b]: return True
    return False


for i in range(0, len(list)):
    if i == 0:
        new_list.append(list[0])
    for j in range(i + 1, len(list)):
        if check(i, j):
            new_list.append(list[i])
print(new_list)
print(sp_list)

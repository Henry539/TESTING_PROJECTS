import random

n = random.randint(1, 60)
bo_so = [[0] for i in range(20)]
list = []
while True:
    i = len(list)
    if i == 60:
        break
    n = random.randint(1, 60)
    if n not in list:
        list.append(n)
a = 0


def triple(x, y):
    bo_so[y] = [x[0], x[1], x[2]]
    x.remove(x[0])
    x.remove(x[0])
    x.remove(x[0])
    return bo_so[y]


while True:
    if len(list) == 0:
        break
    triple(list, a)
    a += 1

print(bo_so)

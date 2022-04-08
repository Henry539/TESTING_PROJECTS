# DE QUY
a = int(input('nhap so can tinh day thua: '))


def day_thua(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return x * day_thua(x - 1)


print(day_thua(a))

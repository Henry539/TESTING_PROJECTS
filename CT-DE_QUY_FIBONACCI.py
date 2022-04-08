# DE QUY FIBONACCI
a = int(input('nhap day thu n: '))


def tong_fabonacci(x):
    if x == 1 or x == 2:
        return 1
    return tong_fabonacci(x - 1) + tong_fabonacci(x - 2)


print(tong_fabonacci(a))

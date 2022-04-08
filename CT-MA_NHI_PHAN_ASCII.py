# MA NHI PHAN ASCII
so = list(input('nhap ma nhi phan: '))
so.reverse()
x = 0
sum = 0

if len(so) == 8:
    for i in so:
        a = int(i)
        if a == 1 or a == 0:
            sum = sum + a * (2 ** x)
            x += 1
        else:
            print('so sai, moi nhap lai')
            break
    print(sum)
else:
    print('so sai, moi nhap lai')

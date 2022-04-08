n = int(input('nhập số tiền cần thối: '))
menh_gia_1000 = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000]
i = 0
while True:
    if i == len(menh_gia_1000):
        break
    b = n // menh_gia_1000[i]
    a = menh_gia_1000[i]
    n -= (b * a)
    print('mệnh giá', a, 'vnđ:', b, 'tờ')
    i += 1

print('tiền thừa:', n, 'vnđ')

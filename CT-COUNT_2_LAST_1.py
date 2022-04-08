N = int(input())


def counting(x):
    while True:
        x = sum([int(i) for i in list(str(x))])
        if len(str(x)) == 1:
            break
    return x


print(counting(N))

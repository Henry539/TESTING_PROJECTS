input = list(map(int, input('Nhập các số (cách nhau bằng khoảng trống): ').split()))


# list.sort()
# print(list)
def quicksort(m):
    if len(m) < 2:
        return m
    else:
        k = m[0]
        L = [i for i in m[1:] if i < k]  # i<=k neu lay gia tri lap
        R = [i for i in m[1:] if i > k]
        return quicksort(L) + [k] + quicksort(R)


print(quicksort(input))

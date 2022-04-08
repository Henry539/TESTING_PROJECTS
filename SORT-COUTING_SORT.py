input = list(map(int, input('Nhập các số (cách nhau bằng khoảng trống): ').split()))
a = max(input)


def main(arr):
    list = []
    seen = [0] * (a + 1)  # tạo seen max+1 element giá tri = 0
    for i in arr:  # giá trị tại arr là thứ tự trong seen
        seen[i] += 1  # thứ tự tại đó = 1

    ## LIST THU TU CO LAP LAI GIA TRI
    # list=[]
    # for i,val in enumerate(seen):
    #     if val == 1:
    #         list.append(i)
    #     if val > 1:
    #         for j in range(val):
    #             list.append(i)

    ## LIST THU TU KO LAP LAI GIA TRI
    list = [i for i, val in enumerate(seen) if val == 1]

    return list


print(main(input))

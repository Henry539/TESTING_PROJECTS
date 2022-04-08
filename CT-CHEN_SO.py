lis = [-10,-6,-5,-4,-3,-1,0,1,4,5,6,9,10]

n = int(input('nhap so: '))

for i in range(0,len(lis)):
    if n > lis[len(lis)-1]:
        lis.append(n)
        break
    if n < lis[0]:
        lis.insert(0,n)
        break
    elif n not in lis :
        if lis[i] < n and lis[i+1] > n:
            lis.insert(i+1,n)
            break
    else:
        print('n da trong lis')
        break

print(lis)
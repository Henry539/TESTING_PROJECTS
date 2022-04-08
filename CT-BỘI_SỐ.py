#
# so_nguyen_to=[]
#
# import math
# for num in range(2,10**9):
#     if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
#        so_nguyen_to.append(num)
#
# print(so_nguyen_to)
# # def check(x):
# #     if x < 2:
# #         return  False
# #     for a in range(2, x):
# #         if x % a == 0:
# #             return  False
# #             break
# #     return True
# #
# # for i in N:
# #     if check(i) == True:
# #         so_nguyen_to.append(i)
# #
# # def chia_het(x):
# #     mum=[0]*101
# #     list_ts=[]
# #     mum[0]=x
# #     for a in range(0,100):
# #         for i in so_nguyen_to:
# #             b = mum[a]
# #             if b % i == 0 and b != 0:
# #                 list_ts.append(i)
# #                 mum[a+1] = b/i
# #                 break
# #     return list_ts
# #
# # print(chia_het(10124))


n = int(input('NHẬP SỐ: '))
j = 3
out = []
def snt(a):
    for i in range(3, int(a**0.5)+1,2):
        if a % i ==0: return False #(not n%i)
    return True

while not n % 2:#n%2==0
    n /= 2
    out.append(2)
while n != 1:
    while not n % j and snt(j):
        n/=j
        out.append(j)
    j+=2
print(*out, sep=' ')

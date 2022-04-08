# n = int(input('nhap gioi han: '))
# so_nguyen_to=[2]
#
#
# #kiem tra ko ton tai so chia het
# def check(x):
#     for a in range(3, int(x ** 0.5) + 1, 2):
#         if x % a == 0:
#             return False
#     return True
#
# #ktra list le bang while
# i = 3
# while n!=1:
#     if check(i):
#         so_nguyen_to.append(i)
#     i+=2
#     if i > n:
#         break


a = int(input())

# CHECK SNT_1
# so_le = [int(i) for i in range(3,a+1,2)]
# def check2(n):
#     if n in so_le and (n+1)%3== 0:return True
#     if n in so_le and (n-1)%3==0:return True
#     if n == 2 or n == 3: return True
#     return False
# #kiem tra so nguyen to trong list so le
# if check2(a):
#     print('yes')
# else:
#     print('no')

# CHECK SNT_2

if (a + 1) % 6 == 0 or a == 2:
    print(True)
elif (a - 1) % 6 == 0 or a == 3:
    print(True)
else:
    print(False)

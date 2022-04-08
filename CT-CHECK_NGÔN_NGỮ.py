li = [i for i in input('nhập văn bảng: ')]

# import bảng chữ cái (LOWER + UPPER)
import string

bang_chu_cai1 = list(string.ascii_lowercase)
bang_chu_cai2 = list(string.ascii_uppercase)
numbers = [str(i) for i in range(0, 10)]  # list str(số 1-9)
bang_chu_cai = bang_chu_cai1 + bang_chu_cai2
# append khoảng cách vào bcc
bang_chu_cai.append(' ')


# func check tiếng anh
def check(x):
    for i in x:
        if i in numbers:
            continue
        if i not in bang_chu_cai:
            return False
    return True

# check input (final)
if check(li):
    print('ngôn ngữ: Tiếng Anh')
else:
    print('ngôn ngữ: Tiếng Việt')


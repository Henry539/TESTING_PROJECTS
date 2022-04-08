# DEM SO LUONG KI TU
import string

bang_chu_cai = list(string.ascii_lowercase)
bang = list(input('nhap chu cai: '))
chu_cai = []
so_luong = []

for i in bang:
    if i in bang_chu_cai and i not in chu_cai:
        chu_cai.append(i)
for j in chu_cai:
    z = bang.count(j)
    so_luong.append(z)

tong_so_chu = dict(zip(chu_cai, so_luong))
print(tong_so_chu)

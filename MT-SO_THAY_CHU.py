type = int(input('nhap 1 neu la dich mat thu so thay chu,'
                 ' nhap 2 neu la ma hoa mat thu so thay chu: '))


def so_thay_chu():  # MAT THU SO THAY CHU
    import string
    import re

    mat_thu = input('nhap mat thu: ')
    a = int(input('so thu tu: '))
    b = input('chu cai: ')
    bang_chu_cai = list(string.ascii_lowercase)
    new_bcc = []
    stt = []
    van = []
    # tong_hop_mat_thu = []
    # bo_ma = dict()
    x = bang_chu_cai.index(b)

    for j in bang_chu_cai:
        if x < 26:
            new_bcc.append(bang_chu_cai[x])
            x += 1
        else:
            y = x - 26
            new_bcc.append(bang_chu_cai[y])
            x += 1

    for i in range(0, 26):
        if a <= 26:
            stt.append(a)
            a += 1
        else:
            b = a - 26
            stt.append(b)
            a += 1

    giai_ma = dict(zip(stt, new_bcc))

    # tach rieng so
    tong_hop_mat_thu = re.findall(r'\d+|–', mat_thu)

    for so in tong_hop_mat_thu:
        if so != '–':
            key = int(so)
            van.append(giai_ma[key])
        else:
            van.append(" ")

    bach_van = "".join(van)
    return print("bach van la:", bach_van)


def ma_hoa():  # MA HOA MAT THU
    a = input('nhap bach van can ma hoa: ')
    b = input('tu khoa: ')
    c = int(input('so khoa: '))

    new_bcc = []
    stt = []
    mat_thu = []

    import string
    bang_chu_cai = list(string.ascii_lowercase)

    x = bang_chu_cai.index(b)
    for i in bang_chu_cai:
        if x < 26:
            new_bcc.append(bang_chu_cai[x])
            x += 1
        else:
            y = x - 26
            new_bcc.append(bang_chu_cai[y])
            x += 1

    for j in range(1, 26 + 1):
        if c < 26 + 1:
            stt.append(c)
            c += 1
        else:
            z = c - 26
            stt.append(z)
            c += 1

    bo_ma_hoa = dict(zip(new_bcc, stt))

    bach_van = list(a)
    for i in bach_van:
        if i == ' ':
            mat_thu.append('-')
            mat_thu.append(' ')
        else:
            mat_thu.append(str(bo_ma_hoa[i]))
            mat_thu.append(' ')
    mat_thu.append('/AR')

    bang_ma_hoa = ''.join(mat_thu)
    return print('bang ma hoa la: ', bang_ma_hoa)


if type == 1:
    so_thay_chu()
elif type == 2:
    ma_hoa()
else:
    print('moi nhap lai so')

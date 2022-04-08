hi = input('nhập số (tối đa 12 chữ số): ')
# ép chữ thành số vào 1 list
inp = list(map(int, hi))

if len(inp) > 12:  # check số lượng chữ số quá 12 chữ
    print('xin mời nhập lại (12 chữ số)')
elif sum(inp) == 0:  # check nhập full chữ số 0
    print('đọc thành chữ: không .')
else:
    # dict số và chữ tương ứng
    nums = {0: 'không', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bốn', 5: 'năm', 6: 'sáu', 7: 'bảy', 8: 'tám', 9: 'chín',
            10: 'mười', 100: 'trăm', 1000: 'nghìn', 1000000: 'triệu', 1000000000: 'tỷ',
            11: 'mốt', 12: 'mươi', 22: 'lẻ'}

    # chữ số hàng trăm
    def tram(a):
        if len(a) < 3:
            return ''
        if a[-3] == 0 and sum(a) != 0:
            return 'không trăm'
        if a[-3] == 1:
            return nums[1] + ' ' + nums[100]
        if (a[-3] * 100 + a[-2] * 10 + a[-1]) > 100:
            return nums[a[-3]] + ' ' + nums[100]
        else:
            return ''


    # chữ số hàng chục
    def chuc(a):
        if len(a) < 2:
            return ''
        if a[-2] == 1:
            return nums[10]
        elif (a[-2] * 10 + a[-1]) > 10:
            return nums[a[-2]] + ' ' + nums[12]
        else:
            return ''


    # chữ số hàng đơn vị
    def don_vi(a):
        if a[-1] == 1 and sum(a) != 1 and a[-2] > 1:
            return nums[11]
        if len(a) == 3 and a[-2] == 0:
            return nums[22] + ' ' + nums[a[-1]]
        if a[-1] in nums and a[-1] != 0:
            return nums[a[-1]]
        return ''


    # xử lý trăm-chục-đơnvị theo từng khung dv-nghìn-triệu-tỷ
    def tram_chuc_dv(a):
        return tram(a) + ' ' + chuc(a) + ' ' + don_vi(a) + ' '


    # loại bỏ 0 đứng trước số - vd:0020 = 20
    def check_0(x):
        if x[0] == 0:
            return True
        return False


    while check_0(inp):
        inp.remove(inp[0])

    # phân loại các giá trị: nghìn-triệu-tỷ
    ket_qua = []  # list chứa các chữ
    if len(inp) <= 3:  # dv
        ket_qua.append(tram_chuc_dv(inp))
    elif len(inp) <= 6:  # nghìn-dv
        # nghìn
        ket_qua.append(tram_chuc_dv(inp[-len(inp):-3]))
        if sum(inp[-len(inp):-3]) > 0:
            ket_qua.append('nghìn')
        # dv
        ket_qua.append(tram_chuc_dv(inp[-3:]))
    elif len(inp) <= 9:  # triệu-nghìn-dv
        # triệu
        ket_qua.append(tram_chuc_dv(inp[-len(inp):-6]))
        if sum(inp[-len(inp):-6]) > 0:
            ket_qua.append('triệu')
        # nghìn
        ket_qua.append(tram_chuc_dv(inp[-6:-3]))
        if sum(inp[-6:-3]) > 0:
            ket_qua.append('nghìn')
        # dv
        ket_qua.append(tram_chuc_dv(inp[-3:]))
    elif len(inp) <= 12:  # tỷ-triệu-nghìn-dv
        # tỷ
        ket_qua.append(tram_chuc_dv(inp[-len(inp):-9]))
        if sum(inp[-len(inp):-9]) > 0:
            ket_qua.append('tỷ')
        # triệu
        ket_qua.append(tram_chuc_dv(inp[-9:-6]))
        if sum(inp[-9:-6]) > 0:
            ket_qua.append('triệu')
        # nghìn
        ket_qua.append(tram_chuc_dv(inp[-6:-3]))
        if sum(inp[-6:-3]) > 0:
            ket_qua.append('nghìn')
        # dv
        ket_qua.append(tram_chuc_dv(inp[-3:]))

    # ép list thành string, dùng split bỏ khoảng trống và trả lại string
    a = ' '.join(ket_qua)
    b = a.split()
    b.append('.')
    print('đọc thành chữ: ', ' '.join(b))

input('PRESS ENTER TO ESCAPE!')
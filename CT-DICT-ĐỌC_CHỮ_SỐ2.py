nums = {0: 'không', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bốn', 5: 'năm', 6: 'sáu', 7: 'bảy', 8: 'tám', 9: 'chín',
        10: 'mười', 11: 'mốt', 12: 'mươi', 22: 'lẻ'}


def speech_3(number):  # func check trăm-chục-đv
    numbers = list(map(int, number))
    original_length = len(numbers)
    text = []
    if original_length == 1:  # khi inp = 1
        text.append(nums[numbers[0]])
    if len(numbers) == 3:  # trăm
        text.append('{} trăm'.format(nums[numbers[0]]))
        numbers = numbers[1:]
        if numbers[0] == 0 and numbers[1] == 0:  # x-0-0 return x trăm
            return text
        if len(numbers) == 2 and numbers[0] == 0 and numbers[1] != 0:  # x-0-x return x lẻ x
            text.append('lẻ {}'.format(nums[numbers[1]]))
            return text

    if len(numbers) == 2:  # chục
        if numbers[0] == 1:
            text.append('mười')
            if numbers[1] != 0 and numbers[1] != 5:
                text.append(nums[numbers[1]])
            if numbers[1] == 5:
                text.append(nums[55])
        else:
            text.append('{} mươi'.format(nums[numbers[0]]))
            if numbers[1] == 0:
                return text
            if numbers[1] == 1:
                text.append(nums[11])
            elif numbers[1] == 5:
                text.append(nums[55])
            else:
                text.append((nums[numbers[1]]))
    return text

while True:
    num_inp = input('Mời nhập số (12 chữ số trở xuống): ')
    units = ['', 'nghìn', 'triệu', 'tỷ', '']  # đơn vị theo từng cặp trăm-chục-đv
    if len(num_inp) > 12:
        print('Quá 12 chữ số, xin mời nhập lại!')
    else:
        try:
            number_input = '0' * (3 - len(num_inp) % 3) + num_inp  # thêm '0' vô trước để len%3
            loop = len(number_input) // 3  # chia lấy phần nguyên, nếu '/' sẽ là n.0
            unit = units[:loop]  # tạo list đơn vị phù hợp với input
            speech_nums = []
            for i in range(loop):  # loop số cặp trăm-chuc-đv
                numbers_3 = number_input[i * 3: i * 3 + 3]  # tạo từng list trăm-chục-đv
                if numbers_3 != '000':  # nếu trăm-chục-đv == '000' thì ko gọi func,1000 = 1nghìn
                    if i == 0:
                        numbers_3 = str(int(numbers_3))
                    speech_nums += speech_3(numbers_3) + [unit[-i - 1]]
        except:
            print("XIN NHAP LAI!")
            continue
        print('Đọc thành chữ:', (' '.join(speech_nums).strip()), '.')

    a = input('PRESS ENTER or Q2QUIT!')
    if a == "q":
        break
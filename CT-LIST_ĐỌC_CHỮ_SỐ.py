def speech_3(number):
    single = ('một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'không')
    double = ('mốt', 'hai', 'ba', 'tư', 'lăm', 'sáu', 'bảy', 'tám', 'chín')
    original_length = len(number)
    text = []
    if len(number) == 3:
        text.append('{} trăm'.format(single[int(number[0]) - 1]))
        print(number)
        number = str(int(number[1:]))
        print(len(number))
        if len(number) == 1 and number[0] != '0':
            text.append('linh {}'.format(single[int(number[0]) - 1]))
    if len(number) == 2:
        if number[0] == '1':
            text.append('mười')
            if number[1] != '0' and number[1] != '5':
                text.append(single[int(number[1]) - 1])
            if number[1] == '5':
                text.append(double[int(number[1]) - 1])
        else:
            text.append('{} mươi'.format(single[int(number[0]) - 1]))
            if number[1] != '0':
                text.append(double[int(number[1]) - 1])
    if original_length == 1:
        text.append(single[int(number[0]) - 1])
    return text


unit = ('nghìn', 'triệu', 'tỷ', '')
number = str(int(input('Nhập số có 12 chữ số trở xuống: ')))
number = '0' * (3 - len(number) % 3) + number

loop = len(number) // 3

speech_number = []
for i in range(loop):
    number_3 = number[i * 3: i * 3 + 3]
    if number_3 != '000':
        if i == 0:
            number_3 = str(int(number_3))
        speech_number += speech_3(number_3) + [unit[loop - i - 2]]

print(str(' '.join(speech_number).strip()))

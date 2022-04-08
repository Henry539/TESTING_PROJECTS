dict = {'a': 5, 'b': 14, 'c': 32, 'd': 32, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
n = int(input('nhap n chu so max_values: '))

def find_max(a):
    all_values = list(dict.values())
    new_all = []
    max_n = {}
    #check gia tri united
    for i in all_values:
        if i not in new_all:
            new_all.append(i)

    #tim max in value_dict
    for i in range(a):
        x = max(new_all)
        for k, v in dict.items():
            if v == x:
                max_n[k] = v
        new_all.remove(x)
    return max_n

print(find_max(n))


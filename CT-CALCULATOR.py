so1, phep_tinh, so2 = input().split()

def calculator(x,y,z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "x" or y == "*":
        return x * z
    elif y == ":" or y == "/":
        return x / z
    else:
        return False

so1=float(so1)
so2=float(so2)
ketqua = calculator(so1,phep_tinh,so2)

if ketqua:
    print("{} {} {} = {}".format(so1,phep_tinh,so2,ketqua))
else:
    print("sai")


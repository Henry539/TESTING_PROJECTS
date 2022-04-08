
day=["5","3"]
road = int(input("do cao cua gieng: "))

way = 0
day=0
night=0
while road > way:
    day+=1
    if day%3 == 0:
        way += 3
    way+=5

print(day)
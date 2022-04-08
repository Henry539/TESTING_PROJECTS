#input str_string => list_str
li= list(input())
#input str_strins (cách nhau) -> list_str    input ab abc abcd -> [ab,abc,abcd]
li=list(input().split())


#input 1 số n -> 1 int
n = int(input())
#input str_nums (cách nhau) -> list_int      input: 12 3 45 -> [12,3,45]
li=list(map(int, input().split()))
#input str_nums (ko cách) -> list_int        input 12345 -> [1,2,3,4,5]
li=[int(i) for i in input()]
li=list(map(int,input()))


#Sum của list
su = sum([int(i)for i in str(a)])


#bảng chữ cái aphal: list_str
import string
bang_chu_cai1 = list(string.ascii_lowercase)

#tìm n số max trong list: list_num
import heapq
max_values = heapq.nlargest(n, all_values)

#random số trong khoảng a-b (bao gồm b)
import random
n = random.randint(a,)
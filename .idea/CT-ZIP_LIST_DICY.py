org_dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
new_list=[]
new_dict={}
b = org_dict['Science']
c = org_dict['Language']
for i,j in zip(b,c):
    new_dict['Science']=i
    new_dict['Language']=j
    new_list.append(new_dict)
    new_dict={}

print(new_list)
lst=[1,2,3,2,10,2,1]
max=lst[0]
for i in lst:
    fre_count=lst.count(i)
    if fre_count>max:
        max=i
print(max)
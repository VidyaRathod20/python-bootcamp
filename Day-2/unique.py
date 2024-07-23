#print unique key values
arr=[1,3,6,2,5,3,7,5,1]
d={}
for i in arr:
    if i not in d:
        d[i]=1
        
    else:
        d[i]+=1
for num,count in d.items():
    if count==1:
        print(num)

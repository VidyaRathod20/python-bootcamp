#count frequency of each number

arr=[1,3,6,2,5,3,7,5,1]
#arr=list(map(int,input().split()))
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

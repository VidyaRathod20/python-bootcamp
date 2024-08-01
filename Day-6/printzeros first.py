arr=[1,1,0,1,1,1,1,0,0,0,0,0]
'''printing all zero  once and once after
output:
    0,0,0,1,1,1,1'''
o=[]
z=[]
for i in arr:
    if i==0:
        z.append(i)
    else:
        o.append(i)
z.extend(o)
print(z)

















    

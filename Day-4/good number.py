#Good number

arr=[35,9,1]

count=0
for ele in arr:
    low=1
    high=math.ceil(ele**0.3)
    print(high)
    while low<high:
        res=low**3 + high**3
        if res==ele:
            count+=1
        if res<ele
            count+=1
            low+=1
        
print(ele)
print('yhe count is: ',count)
  

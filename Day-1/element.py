#printing no of elements div by 4 and 6 in array

def div(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            print(i)
            count+=1
    return count
arr=[1,36,24,9,2,12]
print(div(arr))

#reverse of words and sentence
def reverse(arr):
    rev=''
    for i in arr:
        rev=i+rev  
    return rev
arr=str(input())
print(reverse(arr))

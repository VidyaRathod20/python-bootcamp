n1=7823
n2=5489
n3=1384
'''find sum of all min digit
sum od all max digit
and find the diffrence'''
def min_check(n):
    s=str(n)
    min_int(s[0])  
    for i in s:
        if int(i)<min:
            min=int(i)
    return min
def max_check(n):

    s=str(n)
    max=int(s[0])
    for i in s:
        max=int(i)
    return max
min_sum=min-check(n1)+min_check(n2)+min_check(n3)
max_sum=max-check(n1)+max_check(n2)+max_check(n3)
diff=abs(min_sum=max_sum)
print(diff)

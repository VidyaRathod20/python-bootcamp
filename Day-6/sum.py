num=[1,2,3,4,5]

'''hide 1 and do sum 14
hide 2 and do sum 13
hide 3 and do sum 12
hide 4 and do sum 11
hide 5 and do sum 10
maximun sum:14
minimum sum:10

diff:4  '''

num.sort()

min_sum=sum(num[:len(num)-1])
max_sum=sum(num[1:])
diff=abs(min_sum-max_sum)
print(diff)      

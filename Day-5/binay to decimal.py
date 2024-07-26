n=101011
'''1*2**0  1
1*2**1  2
0*2**2  0
1*2**3  8
0*2**4  0
0*2**5  32
output:43 convert binay num to decimal num'''
sum=0
i=0
while n>0:
    rem=n%10
    pro=rem*pow(2,i)
    sum+=pro
    i+=1
    n=n//10
print(sum)
'''# Convert binary number to decimal
decimal_num = 0
for i, digit in enumerate(reversed(binary_num)):
    decimal_num += int(digit) * (2 ** i)

# Print the result
print(f"The decimal equivalent of binary number {binary_num} is: {decimal_num}")'''

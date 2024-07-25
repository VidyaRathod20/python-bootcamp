s='a1d2c3d492nm45'
'''output:
    123494abcdnm'''
s1=''
s2=''
for char in s:
    if char.isdigit():
        s1+=char
    else:
        s2+=char
print(s1+s2)
        

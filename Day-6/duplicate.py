s='hello world hello world good morning good afternoon'
'''remove duplicate word
output=hello world morning afternoon'''

'''s=s.split()
s1=''
for i in s:
    if i not in s1:
         s1=s1+i+' '
print(s1)'''
s=s.split()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
s1=''
for k,v in d.items():
    if v>=1:
       s1+=k+' '
print(s1)       
        
   

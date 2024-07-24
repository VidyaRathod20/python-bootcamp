s=input()
ucount,lcount,dcount,scount=0,0,0,0

for char in s:
    if char.isupper():
        ucount+=1
    elif char.islower():
        lcount+=1
    elif char.isdigit():
        dcount+=1
    else:
        scount+=1
if len(s)>8 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print('valid')
else:
    print('not valid')     

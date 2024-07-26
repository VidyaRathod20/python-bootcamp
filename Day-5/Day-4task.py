s=['aba','sasdad','aaaccc','tapdog','emepe']
count=0
for i in s:
    if i==i[::-1]:
        count+=1
        
    else:
         m=len(i)//2
         if len(i)%2==0:
           
            first=i[:m]
            secord=i[m:]
         if first==first[::-1] or secord[::-1]:
                count+=1
               
         else:
           first=i[:m+1]
           secord=i[m+1:]
           if first==first[::-1] or secord[::-1]:
                count+=1
                
print(count)
            

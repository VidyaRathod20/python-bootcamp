'''convert time in 12hr format'''
time='13:60:55'
time=time.split(':')
hrs=time[0]
min=time[0]
sec=time[0]

if int (hrs)>12:
    hrs=int(hrs)-12
    
if int(min)>59:
    hrs+=1
    min=0
    
if int(sec)>59:
    min+=1
    sec=0
print(str(hrs)+':'+str(min)+':',str(sec))    

import random
ran=andom.randint(1,100)
chances=1
while chances<=3:
    guess=int(input('enter the number'))
    if guess==ran:
        print('congracts')
        break
    else:
        chances+=1
        continue
if chances>=3:
   print('failed try next time')

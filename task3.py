

import functools
def sum_even():
   total=0
   even_square=[]
   for i in range(0,10):
        if(i%2==0):
           a=i**2
           even_square.append(a)
   total+=functools.reduce((lambda x,y: x+y),even_square)
   print(total)
sum_even()

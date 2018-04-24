import functools
def sum_even(a,b):
    total=0
    mylist=[]
    for i in range(100,500):
        if(i % 2 == 0):
            mylist.append(i)
    total+=functools.reduce((lambda x,y: x+y),mylist)
    return total
print(sum_even(100,500))

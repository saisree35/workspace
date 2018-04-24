import functools
def nested_sum():
    total = 0
    list_a=[1,[2],3,4]
    for i in list_a:
        if (isinstance(i,list)):
                   total+=functools.reduce((lambda x,y: x+y),i)
        else:
             total +=i
    print(total)
nested_sum()

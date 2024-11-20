my_list = ['Marry', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
    # del my_list[3]
    my_list[3] = 'ram'
    return my_list
    
print(my_list(my_list))

my_list = [x * x for x in range(5)]
print(my_list)
def fun(lst):
    del lst[lst[2]]
    return lst
    
    
print(fun(my_list))

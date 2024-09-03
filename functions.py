def any():
    print(var + 1, end='')
var = 2
any()
print(var)


tup = (1,)
print(type(tup))
print(tup[0])

# def fun(a=b=2):
#     return a * b


def arguments(a, b, c):
    print(a + b + c)
# arguments(1) # missing required argument
arguments(1, 2, 3) # positional call
arguments(a=1, b=2, c=3) # keyword call
arguments(1, b=2, c=3) # mix of positional and keyword call
# arguments(a=1, 2, c=3) # SyntaxError: positional argument follows keyword argument

# def arguments1(a, b=2, c):  # SyntaxError: positional argument follows keyword argument
    # print(a + b + c)

def arguments2(a, b, c=5):
    print(a + b + c)
arguments2(1, 2) # positional call
arguments2(a=1, b=2, c=3) # keyword call
arguments2(1, b=2, c=3) # mix of positional and keyword call
# arguments(a=1, 2, c=3) # SyntaxError: positional argument follows keyword argument



var = 2


def mult_by_var(x):
    global var
    var = 5
    return x * var
print(mult_by_var(7))   
print(var)


# try:
number = int(input("Enter an integer number: "))
print(number/2)
# except:
#     print("Warning: the value entered is not a valid number. Try again...")



my_list = ["Adam", "John", "Lucy"]
def hi_everybody(my_list):
    del my_list[1]
    print(my_list)
hi_everybody(my_list)
print(my_list)


# def fun(in=2, out=2):
#     return in * out
# print(fun(3))

print()

def f(x):
    if x == 0:
        return 0
    print(x)
    return x + f(x - 1)
    
print(f(3))


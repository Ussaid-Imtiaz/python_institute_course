stack = []  # Declare in the global scope

def push(val):
    stack.append(val)  # Use the global stacks

push(1)
print(stack) 
push(2)
print(stack) 
push(3)
print(stack) 
stack[0] = 0

def pop():
    val = stack[-1]
    del stack[-1]
    return val

print(pop())
print(stack) 
print(pop())
print(stack) 
print(pop())
print(stack) 


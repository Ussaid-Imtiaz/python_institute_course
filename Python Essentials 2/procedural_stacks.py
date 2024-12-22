stacks = []  # Declare in the global scope

def push(val):
    stacks.append(val)  # Use the global stacks

push(1)
push(2)
push(3)

print(stacks)  # This should now work

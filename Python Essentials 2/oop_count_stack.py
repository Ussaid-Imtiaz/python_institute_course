class Stack:
    def __init__(self):
        self.__stack_list = []

    def get_stack(self):
        return self.__stack_list

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class CountStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def get_counter(self):
        return self.__count

    def pop(self):
        val = Stack.pop(self)
        self.__count += 1
        return val

stack_object = CountStack()

for i in range(100):
    stack_object.push(i)
    stack_object.pop()
    
print(stack_object.get_counter())






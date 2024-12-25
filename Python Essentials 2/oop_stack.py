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

stack_object = Stack()

# stack_object.push(3)
# print(stack_object.get_stack())
# stack_object.push(2)
# print(stack_object.get_stack())
# stack_object.push(1)
# print(stack_object.get_stack())

# print(stack_object.pop())
# print(stack_object.get_stack())
# print(stack_object.pop())
# print(stack_object.get_stack())
# print(stack_object.pop())
# print(stack_object.get_stack())

# stack_object_1 = Stack()
# stack_object_2 = Stack()

# stack_object_1.push(3)
# print(stack_object_1.get_stack())
# print(stack_object_2.get_stack())

# stack_object_2.push(stack_object_1.pop())
# print(stack_object_1.get_stack())
# print(stack_object_2.get_stack())


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

stack_object_3 = AddingStack()

for i in range(1,5):
    stack_object_3.push(i)
    print("List of Stack :",stack_object_3.get_stack())
    print("SUM of Stack :", stack_object_3.get_sum())

for i in range(1,5):
    stack_object_3.pop()
    print("List of Stack :",stack_object_3.get_stack())
    print("SUM of Stack :", stack_object_3.get_sum())






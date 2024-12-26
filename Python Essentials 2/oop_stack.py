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

stack_object.push(3)
print(stack_object.get_stack())
stack_object.push(2)
print(stack_object.get_stack())
stack_object.push(1)
print(stack_object.get_stack())

print(stack_object.pop())
print(stack_object.get_stack())
print(stack_object.pop())
print(stack_object.get_stack())
print(stack_object.pop())
print(stack_object.get_stack())

stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
print(stack_object_1.get_stack())
print(stack_object_2.get_stack())

stack_object_2.push(stack_object_1.pop())
print(stack_object_1.get_stack())
print(stack_object_2.get_stack())


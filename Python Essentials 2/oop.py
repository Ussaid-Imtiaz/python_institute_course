# class QueueError(IndexError):
#     pass


# class Queue:
#     def __init__(self):
#         self.queue = []
#     def put(self,elem):
#         self.queue.insert(0,elem)
#     def get(self):
#         if len(self.queue) > 0:
#             elem = self.queue[-1]
#             del self.queue[-1]
#             return elem
#         else:
#             raise QueueError
        
# class SuperQueue(Queue):
#     def isempty(self):
#         return len(self.queue) == 0
        
# que = SuperQueue()
# que.put(1)
# que.put("dog")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Queue empty")

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# stack_object = Stack()

# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)

# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

#     def gen_sum(self):
#         return self.__sum


class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)




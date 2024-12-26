class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1

ex_obj_1 = ExampleClass()
ex_obj_2 = ExampleClass(2)
ex_obj_3 = ExampleClass(4)
# print(ex_obj_1.__dict__, ex_obj_1._ExampleClass__counter)
# print(ex_obj_2.__dict__, ex_obj_2._ExampleClass__counter)
# print(ex_obj_3.__dict__, ex_obj_3._ExampleClass__counter)

class Ex_Class_2:
    varia = 1
    def __init__(self, val):
        Ex_Class_2.varia = val
        
# print(Ex_Class_2.__dict__)

ex_obj_4 = Ex_Class_2(2)

# print(Ex_Class_2.__dict__)
# print(ex_obj_4.__dict__)






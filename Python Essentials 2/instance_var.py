
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val):
        self.__second = val

ex_obj = ExampleClass()
print("First Obj :", ex_obj.__dict__)

ex_obj_2 = ExampleClass(2)
ex_obj_2.set_second(3)
print("Second Obj :",ex_obj_2.__dict__)

ex_obj_3 = ExampleClass(4)
ex_obj_3.__third = 5
print("Thirt Obj :",ex_obj_3.__dict__)

print(ex_obj._ExampleClass__first)




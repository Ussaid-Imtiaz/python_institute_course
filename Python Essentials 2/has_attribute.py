class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 2

example_obj_1 = ExampleClass(1)

print(example_obj_1.a)

if hasattr(example_obj_1, "b"):
    
print(example_obj_1.b)

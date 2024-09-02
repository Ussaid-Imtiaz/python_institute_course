def fun(a):
    if a > 30:
        print("Returning 3 because", a, "is greater than 30")
        return 3
    else:
        result = a + fun(a + 3)
        print(f"At a = {a}, returning {result}")
        return result

print(fun(25))

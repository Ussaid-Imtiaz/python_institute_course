def is_prime(num):
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
            
print(is_prime(89))

# for i in range(1, 20):
# 	if is_prime(i + 1):
# 			print(i + 1, end=" ")

# print()

# def ckeck_digit_of_life():
#     date_of_birth = input("Enter your date of birth (YYYYMMDD) : ")
#     digit_of_life = 0
    
#     for ch in date_of_birth:
#         digit_of_life += int(ch)
#         print(digit_of_life)

#     str_dol = str(digit_of_life)
#     print(type(str_dol))

#     digit_of_life_2 = 0

#     for digit in str_dol:
#         digit_of_life_2 += int(digit)
#         print(digit_of_life_2)
        


#     print(digit_of_life_2)


# ckeck_digit_of_life()


def digit_of_life():
    """Calculate the Digit of Life for a given date."""
    # Get the user's input
    date_of_birth = input("Enter your date of birth (YYYYMMDD): ")
    
    # Ensure input consists only of digits
    if not date_of_birth.isdigit():
        print("Invalid input. Please enter digits only.")
        return
    
    # Calculate the sum of digits until a single digit is obtained
    while len(date_of_birth) > 1:
        date_of_birth = str(sum(int(digit) for digit in date_of_birth))
    
    print(f"The Digit of Life is: {date_of_birth}")

# Call the function
digit_of_life()

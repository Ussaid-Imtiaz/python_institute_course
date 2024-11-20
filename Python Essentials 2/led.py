# Define the patterns for all digits (0 to 9) as a list of rows
digits = [
    [" ### ", "#   #", "#   #", "#   #", " ### "],  # 0
    ["  #  ", "  #  ", "  #  ", "  #  ", "  #  "],  # 1
    [" ### ", "    #", " ### ", "#    ", " ### "],  # 2
    [" ### ", "    #", " ### ", "    #", " ### "],  # 3
    ["#   #", "#   #", " ### ", "    #", "    #"],  # 4
    [" ### ", "#    ", " ### ", "    #", " ### "],  # 5
    [" ### ", "#    ", " ### ", "#   #", " ### "],  # 6
    [" ### ", "    #", "    #", "    #", "    #"],  # 7
    [" ### ", "#   #", " ### ", "#   #", " ### "],  # 8
    [" ### ", "#   #", " ### ", "    #", " ### "]   # 9
]

def display_digits(num_str):
    # Ensure the input is valid
    if not num_str.isdigit():
        print("Invalid input. Please enter only digits.")
        return
    
    # Create a list to hold each row of the final output
    rows = [""] * 5  # 5 rows for the 7-segment style
    
    # Process each digit in the input string
    for digit in num_str:
        # Get the digit pattern
        digit_pattern = digits[int(digit)]
        # Add each row of the digit to the corresponding row in the output
        for i in range(5):
            rows[i] += digit_pattern[i] + "  "  # Add spacing between digits
    
    # Print the rows
    for row in rows:
        print(row)

# Get user input
num_str = input("Enter a number: ")
display_digits(num_str)





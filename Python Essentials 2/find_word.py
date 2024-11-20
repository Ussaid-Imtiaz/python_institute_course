# string = input("Enter a word: ").lower()
# substring = input("String to find the letters of the word: ").lower()
# def pos(string, substring):
#     ch_found = ''

#     for ch in string:
#         print(ch)
#         if not substring.find(ch) == -1:
#             ch_found += ch

#     if string == ch_found:
#         print("Yes")
#     else:
#         print("No")

# pos(string, substring)

# GPT Solution:
def pos(string, substring):
    """Check if all characters of 'string' exist in 'substring'."""
    for ch in string:
        if substring.find(ch) == -1:  # If a character is missing
            print("No")
            return
    print("Yes")


# Sample Input and Output
string = input("Enter a word: ").lower()  # Convert to lowercase for case insensitivity
substring = input("String to find the letters of the word: ").lower()  # Convert to lowercase
pos(string, substring)

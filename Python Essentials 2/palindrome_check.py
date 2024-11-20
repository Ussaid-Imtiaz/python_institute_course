text = input("Enter text: ")
def palindrome_check(text):
    text = text.replace(" ", "").lower()
    if not text:
        print("The input is an empty string. It's not a palindrome.")
        return
    if text == text[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

palindrome_check(text)

# text = input("Enter text: ")
# def palindrome_check(text: str) -> None:
#     """Check if given text is a palindrome."""
#     stripped = "".join(char.lower() for char in text if char.isalpha())
#     if not stripped:
#         print("The input is an empty string after removing non-alphabetical characters. It's not a palindrome.")
#         return
#     print("It's a palindrome" if stripped == stripped[::-1] else "It's not a palindrome")

# palindrome_check(text)


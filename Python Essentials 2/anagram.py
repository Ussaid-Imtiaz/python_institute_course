first_str = input("Enter first string: ")
first_str = first_str.replace(" ", "").lower()
if not first_str:
    print("Empty string can not be anagram")

second_str = input("Enter second string: ")
second_str = second_str.replace(" ", "").lower()
if not second_str:
    print("Empty string can not be anagram")

first_list = list(first_str)
second_list = list(second_str)

first_list.sort()
second_list.sort()

if first_list == second_list:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")




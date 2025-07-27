strings_list = input("Enter a list of strings separated by commas: ").split(',')

search_char = input("Enter the character to search for: ")

print(f"Strings containing the character '{search_char}':")
for string in strings_list:
    if search_char in string:
        print(string)
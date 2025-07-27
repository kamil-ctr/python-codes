s = input("Enter a string: ")
s = s.lower()
reversed_str = ""
for char in s:
    reversed_str = char + reversed_str

if s == reversed_str:
    print(" is a palindrome.")
else:
    print(" is not a palindrome.")
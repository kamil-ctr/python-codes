def lcm(a, b):
    largest = max(a, b)

    while True:
        if largest % a == 0 and largest % b == 0:
            return largest
        largest += 1


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


result = lcm(num1, num2)


print(f"The LCM of {num1} and {num2} is: {result}")
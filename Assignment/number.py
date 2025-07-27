def find_sequence(phone_number, sequence):
    index = phone_number.find(sequence)
    if index != -1:
        result = phone_number[index + len(sequence):]
        if result:
            print(f"Number after the sequence '{sequence}' is: {result}")
        else:
            print(f"The sequence '{sequence}' is found, but there's nothing after it.")
    else:
        print(f"The sequence '{sequence}' is not found in the phone number.")

def main():
    phone_number = input("Enter a phone number: ")
    sequence = input("Enter a sequence of numbers to search for: ")
    find_sequence(phone_number, sequence)

if __name__ == "__main__":
    main()
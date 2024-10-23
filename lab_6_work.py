def encode_password(password: str) -> str:
	encoded_password = ""
	for digit in password:
		new_digit = (int(digit) + 3) % 10
		encoded_password += set(new_digit)
	return encoded_password


# partner edits code here


def main():
    """
    Main function that provides a menu for encoding, decoding, and quitting.
    It loops until the user decides to quit.
    """
    encoded_password = ""  # Variable to store the encoded password

    while True:
        # Displaying the menu
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1":
            # Option 1: Encoding the password
            password = input("Please enter your 8-digit password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode_password(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid input. Please enter an 8-digit numeric password.")

        elif option == "2":
            # Option 2: Decoding the password (if an encoded password exists)
            if encoded_password:
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No password has been encoded yet.")

        elif option == "3":
            # Option 3: Quitting the program
            print("Goodbye!")
            break

        else:
            # Invalid input handling
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

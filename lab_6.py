def encode_password(password: str) -> str:

    encoded_password = ""

    # Iterate through each character in the password
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded_password += str(new_digit)

    return encoded_password
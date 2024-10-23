def encode_password(password: str) -> str:
	encoded_password = ""
	for digit in password:
		new_digit = (int(digit) + 3) % 10
		encoded_password += set(new_digit)
	return encoded_password

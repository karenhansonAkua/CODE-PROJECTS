def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert the character to its ASCII code
            ascii_offset = ord('A') if is_upper else ord('a')
            
            # Apply the Caesar Cipher shift and convert back to a character
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            
            # Append the encrypted character to the result
            encrypted_text += encrypted_char
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char
    
    return encrypted_text

# Get user input
plain_text = input("Enter the message you want to encrypt: ")
shift_amount = int(input("Enter the shift amount for encryption: "))

# Encrypt the message
encrypted_message = encrypt_caesar(plain_text, shift_amount)

# Display the results
print("Original Message:", plain_text)
print("Encrypted Message:", encrypted_message)

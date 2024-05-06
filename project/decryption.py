def decrypt_caesar(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
               # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()

               # Determine whether the character is uppercase or lowercase
            ascii_offset = ord('A') if is_upper else ord('a')

             # Apply the Caesar Cipher shift and convert back to a character
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)

               # Append the decrypted character to the result
            decrypted_text += decrypted_char
        else:

             # If the character is not a letter, leave it unchanged 
            decrypted_text += char
    return decrypted_text

# Get user input for the encrypted message
encrypted_message = input("Enter the message you want to decrypt: ")

# Get user input for the shift amount used for encryption
shift_amount = int(input("Enter the shift amount for decryption: "))

# Call the decrypt_caesar function with the user input
decrypted_message = decrypt_caesar(encrypted_message, shift_amount)

# Display the original and decrypted messages
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

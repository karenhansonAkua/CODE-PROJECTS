def decrypt_caesar(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            ascii_offset = ord('A') if is_upper else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Get user input for the encrypted message
encrypted_message = input("Enter the message you want to decrypt: ")

# Get user input for the shift amount used for encryption
shift_amount = int(input("Enter the shift amount for decryption: "))

# Adjust the shift amount for negative values
if shift_amount < 0:
    shift_amount += 26

# Call the decrypt_caesar function with the user input
decrypted_message = decrypt_caesar(encrypted_message, shift_amount)

# Display the original and decrypted messages
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
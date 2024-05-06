def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            ascii_offset = ord('A') if is_upper else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

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

# Get user input for the text they want to encrypt
text = input("Enter the message you want to encrypt: ")

# Get user input for the shift amount used for encryption
shift_amount = int(input("Enter the shift amount for encryption: "))

# Adjust the shift amount for negative values
if shift_amount < 0:
    shift_amount += 26

# Call the encrypt_caesar function with the user input
encrypted_message = encrypt_caesar(text, shift_amount)

# Display the original and encrypted messages
print("Original Message:", text)
print("Encrypted Message:", encrypted_message)

# Get user input for the shift amount used for decryption
shift_amount_decryption = int(input("Enter the shift amount for decryption: "))

# Adjust the shift amount for negative values
if shift_amount_decryption < 0:
    shift_amount_decryption += 26

# Call the decrypt_caesar function with the user input
decrypted_message = decrypt_caesar(encrypted_message, shift_amount_decryption)

# Display the original and decrypted messages
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)



#Caesar Cipher: A type of substitution cipher in which each letter in the plaintext is 'shifted' 
# a certain number of places down the alphabet. 
# For example, with a shift of 1, A would be replaced by B, B would become C, and so on. 
# The cipher becomes significantly stronger if random numbers are used to determine the shift amount.
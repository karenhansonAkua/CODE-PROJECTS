import math

def decrypt_cyber_text(cyber_text, substitution_matrix):
   decrypted_text = ""
   for i in range(0, len(cyber_text), 2):
       key_pair = cyber_text[i:i+2]
       if key_pair in substitution_matrix:
           decrypted_text += substitution_matrix[key_pair]
       else:
           decrypted_text += key_pair
   return decrypted_text

# Get user input for the encrypted message
cyber_text = input("Enter the message you want to decrypt: ")

# Get user input for the shift amount used for encryption
shift_amount = int(input("Enter the shift amount for decryption: "))

# Define the substitution matrix for decryption
substitution_matrix = {}
for i in range(26):
   char1 = chr((i - shift_amount) % 26 + ord('A'))
   char2 = chr((i + shift_amount) % 26 + ord('A'))
   substitution_matrix[char1 + char2] = chr(i + ord('A'))

# Call the decrypt_cyber_text function with the user input
decrypted_message = decrypt_cyber_text(cyber_text, substitution_matrix)

# Display the original and decrypted messages
print("Encrypted Message:", cyber_text)
print("Decrypted Message:", decrypted_message)
#importing modules
import random
import string

#defining a function to generate a password with a given criteria.
def generator_password(min_length, numbers=True, special_characters=True):

#defining charcter sets for letters, digits and special characters.
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
#initializing characters with letters
    characters = letters
    #adding digits to characters if required.
    if numbers:
        characters += digits

        #adding special charcters to charcters if special characters are required
    if special_characters:
            characters += special

#initializing password and criteria check variables.
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

#loop until the password meets criteria and has the min length
    while not meets_criteria or len(pwd) < min_length:

        #selecting a random charcter from the defined character set
        new_char = random.choice(characters)

        #appending the character to the passsword
        pwd += new_char


#checking if the new character is a digit and updating has_number
        if new_char in digits:
            has_number = True

          # Checking if the new character is a special character and updating has_special   
        elif new_char in special:
            has_special = True

# Checking if the password meets criteria
        meets_criteria =True

        # If numbers are required, checking if the password has at least one number
        if numbers:
            meets_criteria = has_number

              # If special characters are required, checking if the password has at least one special character
        if special_characters:
            meets_criteria = meets_criteria and has_special               

 # Returning the generated password
    return pwd

# Taking user input for minimum password length
min_length = int(input("Enter the minimum length: "))

# Taking user input for including numbers and special characters
has_number = input("Do you want to have numbers (Y/N)? ").lower == "y"
has_special = input("Do you want to have special characters (Y/N)? ").lower == "y"

# Generating a password using the defined function
pwd = generator_password(min_length, has_number, has_special)

# Printing the generated password
print("The generated password is: ", pwd)
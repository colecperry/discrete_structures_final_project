from Gcd import GCD
from Caesar import CaesarCipher
import string
from chinese_remainder import ChineseRemainder
from Caesar import CaesarCipher
from affine import AffineCipher

# Create a print menu for each Theorem
def print_menu():
    print("\nWhat would you like to do? \n")
    print("0 - nothing (terminate the program)")
    print("1 - Find greatest common divisor")
    print("2 - Find bezout's coefficients")
    print("3 - Caesar cipher encryption")
    print("4 - Caesar cipher decryption")
    print("5 - Solve Chinese Remainder Theorem")
    print("6 - Affine cipher encryption")
    print("7 - Affine cipher decryption")

# Create function to check valid input for Caesar Cipher
def is_valid_input(text):
    return all(char in string.ascii_letters or char == " " for char in text)

if __name__ == "__main__":
    # Create an infinite loop
    while True:
        print_menu()
        choice = input("\nEnter choice: ")

        # If choice == 0 terminate the program
        if choice == "0":
            print ("Terminating Program")
            break
        
        # If choice == 1 calculate GCD
        if choice == "1":
            # Get input for X and Y to find GCD
            try:
                x_variable = int(input("Enter X variable: "))
                y_variable = int(input("Enter Y variable: "))
            # Create error handling for non integers
            except ValueError:
                print("\nInvalid Input. Please enter an integer.\n")
                continue
            print(f"\nYou entered x: {x_variable}, y: {y_variable}")
            
            # Create an instance of the NumberTheory class
            my_instance = GCD(x_variable, y_variable)

            # Access instance attributes x and y
            x = my_instance.x
            y = my_instance.y

            # Call the gcd method using the instance
            result = my_instance.gcd()
            print(f"\nGreatest common divisor of {x} and {y} is {result}\n")
        
        # If choice == 2 find Bezout's Theorem
        if choice == "2":
            # Get 2 variables x and y, and use except block 
            try:
                x_variable_2 = int(input("Enter X variable: "))
                y_variable_2 = int(input("Enter Y variable: "))
            except ValueError:
                print("\nInvalid Input. Please enter an integer.\n")
                continue
            print(f"\nYou entered x: {x_variable_2}, y: {y_variable_2}")
            
            # Create another instance of the NumberTheory class
            my_instance_2 = GCD(x_variable_2, y_variable_2)
            
            # Run GCD function so we can store the correct values in the tuple to use for Bezout's Coefficients and run the code
                    # Implement error handling for 
            gcd = my_instance_2.gcd()
            if len(my_instance_2.variable_list) == 0 or gcd != 1:
                print("\nIf GCD != 1, cannot find Bezout's Coefficient\n")
                break
            result2 = my_instance_2.bezout()
            print(f"\nThe GCD of {x_variable_2} and {y_variable_2} is {gcd}\n.\nBezout's Coefficients must solve {gcd} = s*{x_variable_2} + t*{y_variable_2}.\nBezout's coefficients are s,t:{result2}\n")
        
        # If choice == 3 Encrypt Caesar Cipher plaintext
        if choice == "3":
            # Get user input for the shift and plaintext string
            try:
                shift = int(input("Enter shift: "))
                plaintext = str(input("Enter string: "))
                # Check valid input
                # if not is_valid_input(plaintext):
                #     print("\nError: Plaintext can only contain letters.\n")
                #     continue
            except ValueError:
                print("\nInvalid Input. Please enter an integer.\n")
                continue
            print(f"\nYou entered shift: {shift}\nPlaintext: {plaintext}")

            # Create new instance for CaesarCipher class and store the shift and run the code
            my_caesar_encrypt_instance = CaesarCipher(shift)
            cipher_text = my_caesar_encrypt_instance.encrypt(plaintext)
            print(f"\nEcrypted ciphertext:{cipher_text}\n")
        
        # If choice == 4 Decrypt Caesar Cipher
        if choice == "4":
            # Get user input for the shift and ciphertext
            try:
                shift = int(input("Enter shift: "))
                cipher_text2 = str(input("Enter string: "))
                # Check valid input
                # if not is_valid_input(cipher_text2):
                #     print("\nError: Ciphertext can only contain letters.\n")
                #     continue
            except ValueError:
                print("\nInvalid Input. Please enter an integer.\n")
                continue
            print(f"\nYou entered shift: {shift}\nCiphertext: {cipher_text2}")
            # Create new instance for Caesar cipher class and run the decrypt code
            my_caesar_decrypt_instance = CaesarCipher(shift)
            plaintext2 = my_caesar_decrypt_instance.decrypt(cipher_text2)
            print(f"Decrypted ciphertext:{plaintext2}\n")
        
        # If choice == 5 Solve Chinese Remainder Theorem
        if choice == "5":
            # Get the input for the number of congruences
            N = int(input("How many linear congruences are there in the system? "))
            # Create Chinese Remainder instance and run the function
            c = ChineseRemainder()
            c.chinese_remainder(N)
        
        # If choice == 6 Affine Cipher
        if choice == "6":
            # implement try & except logic for error handling
            try:
                # call an instance of the AffineCipher class
                # take user input and covert to int
                affine = AffineCipher(
                    int(input("Enter an x coefficient for the shift key function: ")),
                    int(input("Enter a constant for the shift key function: "))
                )
                # call the ecnrypt method, and assign True or False return value to 'success'
                success, a_encrypted = affine.encrypt(input("Enter a string to encrypt: "))
                
                if success: # if valid key entered print result of encryption
                    print(f"\nEncrypted string: {a_encrypted}")
                else:  # print error message if invalid key
                    print(a_encrypted)

            except ValueError:  # if user doesn't enter int value print message
                print(f"Please enter an integer value")
                continue

        if choice == "7":
            # implement try & except logic for error handling
            try:
                # call an instance of the AffineCipher class
                # take user input and covert to int
                affine = AffineCipher(
                    int(input("Enter an x coefficient for the shift key function: ")),
                    int(input("Enter a constant for the shift key function: "))
                )
                # call the decrypt method, and assign True or False return value to 'success'
                success, result = affine.decrypt(input("Enter a string to decrypt: "))
                if success: # if valid key entered print result of decryption
                    print(f"\nDecrypted string: {result}")
                else: # print error message if invalid key
                    print(result)
        
            except ValueError:  # if user doesn't enter int value print message
                print(f"Please enter an integer value")
                continue

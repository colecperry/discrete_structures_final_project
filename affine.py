from Gcd import GCD


class AffineCipher:
    """
    A class that encrypts and decrypts strings
    using the affine cipher
    """

    def __init__(self, coefficient, constant):
        self._coefficient = coefficient
        self._constant = constant

        # create a dictionary with affine cipher values for each letter
        self.char_values = {
            "A": 1, "B": 2, "C": 3, "D": 4,
            "E": 5, "F": 6, "G": 7, "H": 8,
            "I": 9, "J": 10, "K": 11, "L": 12,
            "M": 13, "N": 14, "O": 15, "P": 16,
            "Q": 17, "R": 18, "S": 19, "T": 20,
            "U": 21, "V": 22, "W": 23, "X": 24,
            "Y": 25, "Z": 26
        }

    def check_key(self):
        """
        Check if the coefficient value for the key
        is co-prime with 26
        """
        # call gcd function from number theory
        number_theory_variables = GCD(26, self._coefficient)
        gcd = number_theory_variables.gcd()
        # check if coefficient is co-prime w/ 26, gcd = 1, return True
        if gcd == 1:
            return True
        # if coefficient is not co-prime return false
        elif gcd != 1:
            return False

    def encrypt(self, s):
        """
        Shifts the letter values & replaces the letters using function E(x) = (ax + b) mod m
        Non-letter characters remain unchanged
        """
        a = self._coefficient
        b = self._constant
        s = s.upper()  # convert the string to all uppercase
        encrypted_string = ""  # intialize an empty string to store encrypted values

        # call the check_key function to see if the key is valid
        valid = self.check_key()

        if valid:  # if valid, begin encryption
            for char in s:  # loop through all characters in the string
                if char in self.char_values:  # check if each charcater in dict
                    # assign numeric value from dict
                    numeric_value = self.char_values[char]

                    # calculate the shift using function E(x) = (ax + b) mod m
                    # while accounting for values starting at 1 not 0
                    shifted_value = ((numeric_value * a) + b - 1) % 26 + 1

                    # loop through dict keys & values
                    for key, value in self.char_values.items():
                        # check for a match, add shifted value to encrypted string
                        if value == shifted_value:
                            encrypted_string += key
                            break  # end the loop after finding a match
                else:  # if char is not in alphabet, leave it unchanged
                    encrypted_string += char
            return True, str(encrypted_string)
        else: 
            return False, "\nInvalid key, the coefficient you entered is not co-prime with 26"

    def decrypt(self, s):
        """
        Reverses the shifted letter values & replaces the letters using function F(x) = a^-1 * (x - b) mod 26
        Non-letter characters remain unchanged
        """
        a = self._coefficient
        b = self._constant
        s = s.upper()  # convert the string to all uppercase
        decrypted_string = ""  # intialize an empty string to store decrypted values

        # call the check_key function to see if the key is valid
        valid = self.check_key()

        if valid:
            # find the multiplicative inverse of a for the decryption shift
            number_theory_variables = GCD(a, 26)
            number_theory_variables.gcd()
            bez_coeffs = number_theory_variables.bezout()
            a_inverse = bez_coeffs[0]
            # print(a_inverse)  # debug

            for char in s:  # loop through all characters in the string
                if char in self.char_values:  # check if each charcater in dict
                    # assign numeric value from dict
                    numeric_value = self.char_values[char]

                    # calculate the shift using function F(x) = a^-1 * (x - b) mod 26
                    # while accounting for values starting at 1 not 0
                    shifted_value = (a_inverse * (numeric_value - b) - 1) % 26 + 1

                    # loop through dict keys & values
                    for key, value in self.char_values.items():
                        # check for a match, add shifted value to encrypted string
                        if value == shifted_value:
                            decrypted_string += key
                            break  # end the loop after finding a match
                else:  # if char is not in alphabet, leave it unchanged
                    decrypted_string += char
            return True, str(decrypted_string)
        else:
            return False, "\nInvalid key, the coefficient you entered is not co-prime with 26"

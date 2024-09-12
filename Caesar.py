class CaesarCipher:
    """ A class that encrypts and decrypts strings using the Caesar cipher """

    def __init__(self, shift):
        self._shift = int(shift)  # initialise the cipher with a shift

        # create a dictionary with Caesar cipher values for each letter
        self.char_values = {
            "A": 1, "B": 2, "C": 3, "D": 4,
            "E": 5, "F": 6, "G": 7, "H": 8,
            "I": 9, "J": 10, "K": 11, "L": 12,
            "M": 13, "N": 14, "O": 15, "P": 16,
            "Q": 17, "R": 18, "S": 19, "T": 20,
            "U": 21, "V": 22, "W": 23, "X": 24,
            "Y": 25, "Z": 26
        }

    def encrypt(self, s):
        """
        Changes alphabetical characters using a shift and leaves non-alphabet characters unchanges
        Int, String --> String
        """
        s = s.upper()  # convert the string into all upper case
        shift = self._shift

        # create an empty string for encrypted values to be placed
        encrypted_string = ""

        for char in s:  # loop through all characters in the string
            if char in self.char_values:  # check if each charcater in dict
                # assign numeric value from dict
                numeric_value = self.char_values[char]
                # find the shifted value
                shifted_value = (numeric_value + shift - 1) % 26 + 1

                # loop through dict keys & values
                for key, value in self.char_values.items():
                    # check for a match, add shifted value to encrypted string
                    if value == shifted_value:
                        encrypted_string += key
                        break  # end the loop after finding a match
            else:  # if char is not in alphabet, leave it unchanged
                encrypted_string += char
        return str(encrypted_string).replace(" ", "")

    def decrypt(self, s):
        """
        Returns alphabetical charcaters to their origional value, reversing the shift
        Int, String -> String
        """
        s = s.upper()  # convert the string into all upper case
        shift = self._shift

        # create an empty string for decrypted values to be placed
        decrypted_string = ""

        for char in s:  # loop through all characters in the string
            if char in self.char_values:  # check if each charcater in dict
                # assign numeric value from dict
                numeric_value = self.char_values[char]
                # find the un-shifted value
                decrypted_value = (numeric_value - shift) % 26

                # handle the case where the decrypted value is 0
                if decrypted_value == 0:
                    decrypted_value = 26

                # loop through dict keys & values
                for key, value in self.char_values.items():
                    # check for a match, add shifted value to encrypted string
                    if value == decrypted_value:
                        decrypted_string += key
                        break  # end the loop after finding a match
            else:  # if char is not in alphabet, leave it unchanged
                decrypted_string += char
        return decrypted_string.replace(" ", "")
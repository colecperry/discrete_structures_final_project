To run the code, go to the main.py file and press the play button or cd into the correct working directory and run python main.py.

Overview of each Class & it's functions:
- Class GCD: The number theory class is initalized with the following variables:
        x : an integer x that is used as an input for functions gcd and bezout
        y : an integer y that is used as an input for functions gcd and bezout
        variable_list : a tuple that is used to store y, x, the coefficient, and remainder used at each step in the gcd calculation and to obtain coefficients for the bezout theorem'''

    - gcd: Function gcd takes two integers as the argument and outputs the greatest common divisor between the two numbers. After running the code, select "1" and input the two integers you would like to find the greatest common divisor of.
    - bezout: Computes the coefficients of Bézout's identity for the given numbers. Bézout's identity states that for any integers a and b, there exist integers x and y such that: a * x + b * y = gcd(a, b). After running the code, select "2" and input the two variables that you would like to find the bezout's coefficients of.


- Class CaesarCipher: A class that encrypts and decrypts strings using the Caesar cipher
    - encrypt: Changes alphabetical characters using a shift and leaves non-alphabet characters unchanges
        Input(s) -> Output(s): Int, String -> String
    - decrypt: Returns alphabetical charcaters to their origional value, reversing the shift
        Input(s) -> Output(s): Int, String -> String

-  Class ChineseRemainder: A class that solves systems of linear congruence
    - chinese_remainder: Implements the chinese remainder theorem to solve systesm of linear congruence
        Input(s) -> Output(s): Ints(N, r_i & m_i values for i = 1...N) -> Int

- Class AffineCipher: A class that encrypts and decrypts strings using the affine cipher
    - check_key: Check if the coefficient value for the key is co-prime with 26
        Input(s) -> Output(s): Int -> Boolean
    - encrypt: Shifts the letter values & replaces the letters using formula E(x) = (ax + b) mod m
               Non-letter characters remain unchanged.
        Input(s) -> Output(s): Int, String -> Boolean, String
    - decrypt: Reverses the shifted letter values & replaces the letters using function F(x) = a^-1 * (x - b) mod 26
               Non-letter characters remain unchanged.
        Input(s) -> Output(s): Int, String -> Boolean, String
import math

class GCD:
    def __init__(self, x, y):
        '''The GCD class is initalized with the following variables:
        x : an integer x that is used as an input for functions gcd and bezout
        y : an integer y that is used as an input for functions gcd and bezout
        variable_list : a tuple that is used to store y, x, the coefficient, and remainder used at each step in the gcd calculation and to obtain coefficients for the bezout theorem'''
        self.x = x
        self.y = y
        self.variable_list = []


    def gcd(self):
        ''' Function gcd takes no arguments and outputs the greatest common divisor between the two numbers'''
        # Obtain values from GCD class and store in x and y, loop var used for debugging purposes
        x = self.x
        y = self.y
        # Create a loop that continues until the remainder of y and x is equal to 0:
        while y % x != 0:
            # Create coefficient variable, remainder variable 
            coefficient = int(y/x)
            coefficient = math.floor(coefficient)
            remainder = y % x
            # Append the tuple to variable_list with all 4 variables needed to calculate bezout's theorem
            data_tuple = (y, x, coefficient, remainder)
            self.variable_list.append(data_tuple)
            # Update the variables y and x to continue with the correct values to the next loop
            y = x
            x = remainder
        # Return the remainder on the second to last loop which is equivalent to the GCD between x and y
        return x

    def bezout(self):
        ''' Computes the coefficients of Bézout's identity for the given numbers. Bézout's identity states that for any integers a and b, there exist integers x and y such that:
        a * x + b * y = gcd(a, b)
        This function calculates the coefficients x and y such that the equation above holds for the two numbers provided during the initialization of the NumberTheory object. '''
            
        # Obtain the last element of the tuple created in the GCD function, the remainder, x-coefficient, and y coefficient
        last_element = self.variable_list[-1]
        # Initialize the x_coefficient to 1 to track the coefficient of the largest number, which is 1 to start with, and 
        x_coefficient = 1
        y_coefficient = -last_element[2]

        # Starting from the second to last element in the tuple, iterate backwards through the list
        for i in range(len(self.variable_list) - 2, -1, -1):
            # Obtain the element at the index you are iterating on
            element = self.variable_list[i]
            last_element = self.variable_list[i+1]

            # Update the coefficients 
            s = y_coefficient
            t = x_coefficient - element[2] * y_coefficient

            # Update the s and t coefficients for the next iteration
            x_coefficient = s
            y_coefficient = t

        return y_coefficient, x_coefficient
    


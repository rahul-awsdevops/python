num = 3
num_float = 3.14

# Printing types of num and num_float
print(type(num))  # Prints the type of num
print(type(num_float))  # Prints the type of num_float

# Arithmetic Operations
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2
print(3 + 2)  # Addition
print(3 - 2)  # Subtraction
print(3 / 2)  # Division (float result)
print(3 // 2)  # Floor Division (integer result)
print(3 * 2)  # Multiplication
print(3 ** 2)  # Exponentiation (3 raised to the power of 2)
print(3 % 2)  # Modulus (remainder when 3 is divided by 2)
print(4 % 2)  # Modulus (remainder when 4 is divided by 2)
print(3 * 2 + 1)  # Order of operations: first multiplication then addition
print(3 * (2 + 1))  # Parentheses first: 2 + 1, then multiplication

# Sum examples
sum = 1
sum = sum + 1
print(sum)  # Increment sum by 1: Output: 2
sum1 = 1
sum1 += 1  # Using shorthand for increment
print(sum1)  # Output: 2
sum2 = 1
sum2 *= 10  # Multiply sum2 by 10
print(sum2)  # Output: 10

# Math functions
print(abs(-3))  # Absolute value of -3, Output: 3
print(round(3.75))  # Round to nearest integer, Output: 4
print(round(3.25))  # Round to nearest integer, Output: 3
print(round(3.75, 1))  # Round to 1 decimal place, Output: 3.8

# Comparison Operations
# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num_1 = 3
num_2 = 2
print(num_1 == num_2)  # Checks if num_1 equals num_2, Output: False
print(num_1 != num_2)  # Checks if num_1 does not equal num_2, Output: True
print(num_1 > num_2)   # Checks if num_1 is greater than num_2, Output: True
print(num_1 < num_2)   # Checks if num_1 is less than num_2, Output: False
print(num_1 >= num_2)  # Checks if num_1 is greater than or equal to num_2, Output: True
print(num_1 <= num_2)  # Checks if num_1 is less than or equal to num_2, Output: False

# String concatenation and type conversion
num_3 = '100'
num_4 = '200'
print(num_3 + num_4)  # Concatenates strings, Output: '100200'

# Converting strings to integers and adding
num_3 = '100'
num_4 = '200'
num_3 = int(num_3)  # Convert num_3 to integer
num_4 = int(num_4)  # Convert num_4 to integer
print(num_3 + num_4)  # Adds the integers, Output: 300

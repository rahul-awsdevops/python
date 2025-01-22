# Printing strings with various quote styles
print('hello rahul')  # Prints a simple string
print("hello's ranjan")  # Demonstrates using double quotes to include a single quote within the string

# Multiline string
message = '''hello world
Today is sunday'''  # Creates a multiline string using triple quotes
print(message)  # Prints the multiline string

# Basic string operations
my_message = "hello world"  # Assigns a string to a variable
print(len(my_message))  # Prints the length of the string

# Accessing characters and slicing
print(my_message[0])  # First character ('h')
print(my_message[10])  # Last character ('d')
print(my_message[0:5])  # Slices first 5 characters ('hello')
print(my_message[:5])  # Same as above
print(my_message[6:11])  # Slices characters ('world')
print(my_message[6:])  # Slices from index 6 to the end ('world')

# String methods
print(my_message.upper())  # Converts to uppercase ('HELLO WORLD')
print(my_message.lower())  # Converts to lowercase ('hello world')
print(my_message.count("hello"))  # Counts occurrences of "hello" (1)
print(my_message.count("l"))  # Counts occurrences of 'l' (3)
print(my_message.find("hello"))  # Finds index of "hello" (0)
print(my_message.find("world"))  # Finds index of "world" (6)
print(my_message.find("universe"))  # Returns -1 since "universe" isn't in the string

# String replacement
new_my_message = my_message.replace("world", "universe")  # Replaces "world" with "universe"
print(new_my_message)  # Prints 'hello universe'

# String concatenation
greeting = "hello"
name = "sam"
greet_msg = greeting + name  # Concatenates without space
print(greet_msg)  # Output: 'hellosam'

new_greet_msg = greeting + ' ' + name  # Concatenates with a space
print(new_greet_msg)  # Output: 'hello sam'

# String formatting using format() and f-strings
new_greet_msg = '{}, {}. Welcome!'.format(greeting, name)
print(new_greet_msg)  # Output: 'hello, sam. Welcome!'

new_greet_msg = f'{greeting}, {name}. Welcome!'
print(new_greet_msg)  # Output: 'hello, sam. Welcome!'

new_greet_msg = f'{greeting}, {name.upper()}. Welcome!'  # Converts 'name' to uppercase
print(new_greet_msg)  # Output: 'hello, SAM. Welcome!'

# Using dir() and help() for introspection
print(dir(name))  # Prints the list of methods and attributes available for the string object

print(help(str))  # Provides detailed help documentation about the 'str' class
print(help(str.upper))  # Provides help for the 'upper()' method specifically

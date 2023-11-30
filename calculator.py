"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

input_string = input("Input?: ") # This is where the computer asks for you to input an expression and integer(s)
                                 # But the program recognizes the inputs as strings
tokens = input_string.split(' ') # We then split the string into individual strings (ex. + 10 5 is now ["+", "10", "5"])
tokens[1] = int(tokens[1]) # Tokens is now the list name and tokens[1] and tokens[2] need to be changed into integers. 
tokens[2] = int(tokens[2])


while True: 
    if "pow" in tokens:             #if tokens[0] is in the list, then we are calling the power function from the arithmetic file. 
                                    # "Pow" is still a string (or tokens[0]), and we are asking if something with that name is in the list tokens.
        print(power(tokens[1], tokens[2])) #if yes, we are calling the pow funcion which accepts two arguments (tokens[1] and [2], because they are integers now.)
    elif "q" in tokens:
        break
    elif "+" in tokens:
        print(add(tokens[1], tokens[2]))
    elif "-" in tokens:
        print(subtract(tokens[1], tokens[2]))
    elif "/" in tokens:
        print(divide(tokens[1], tokens[2]))
    elif "*" in tokens:
        print(multiply(tokens[1], tokens[2]))
    elif "square" in tokens:
        print(square(tokens[1]))
    elif "cube" in tokens:
        print(cube(tokens[1]))
    elif "mod" in tokens:
        print(mod(tokens[1]))

    break


# Replace this with your code

# defining operation functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a *b

def div(a, b):
    return a / b

# listing dictionary of operations 

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

# Getting User Inputs

number_1 = int(input("Enter first number: "))

select = input("Select operation from +, -, *, /: ")

number_2 = int(input("Enter second number: "))

# Doing the calculations

if select == '+':
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == '-':
    print(number_1, "-", number_2, "=", sub(number_1, number_2))

elif select == '*':
    print(number_1, "*", number_2, "=", mul(number_1, number_2))

elif select == '/':
    print(number_1, "/", number_2, "=", div(number_1, number_2))

else:
    print("Invalid input")
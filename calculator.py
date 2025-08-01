# a simple calculator with inbuilt history using python

while True:
    num1 = float(input("enter a number to proceed: "))
    operator = input("please enter an operator[+, -, *, **, /, //, %]: ")
    num2 = float(input("enter a number to proceed: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "**":
        result = num1 ** num2

    elif operator == "/" or operator == "//" and num2 == 0:
        result = "error division by 0"

    elif operator == "/":
        result = num1 / num2

    elif operator == "//":
        result = num1 // num2

    elif operator == "%":
        result = num1 % num2

    elif num1 == "":
        result = "invalid Input"	

    elif num2 == "":
        result = "invalid Input"

    else: 
        result = "invalid operator"
    print  ( "result:",num1, operator, num2, "=", result )









import math

num1 = float(input())
operation = str
while operation != "exit":
    operation = input("выберите операцию")
    if operation == "+" :
        num2 = float(input())
        num1 = num2 + num1
        print( f"промежуточный результат = {num1}" )
    elif operation == "-" :
        num2 = float(input())
        num1 = num1 - num2
        print(f"промежуточный результат = {num1}")
    elif operation == "*":
        num2 = float(input())
        num1 = num2 * num1
        print(f"промежуточный результат = {num1}")
    elif operation == "/":
        if num2 == 0:
            print("но, но, но мистер фиш низя делить на нуль")
            exit()
        else:
            num2 = float(input())
            num1 = num1 / num2
            print(f"промежуточный результат = {num1}")
    elif operation == "**":
        num2 = float(input())
        num1 = num2 ** num1
        print(f"промежуточный результат = {num1}")
    elif operation == "//":
        num2 = float(input())
        num1 = num2 // num1
        print(f"промежуточный результат = {num1}")

    elif operation == "=":
        print(f"результат = {num1}")
        exit()
    else:
        print("нету такова")
        exit()
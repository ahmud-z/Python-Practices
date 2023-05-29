def calculate(num1, num2, opt):  # here opt means operator
    if opt == "+":
        return num1 + num2
    elif opt == "-":
        return num1 - num2
    elif opt == "*":
        return num1 * num2
    elif opt == "/":
        return num1 / num2
    else:
        print("Invalid Input")


def main():
    num1 = float(input("\nEnter your first number: "))
    opt = input("Enter a operator: ")
    num2 = float(input("Enter your second number: "))

    result = calculate(num1, num2, opt)
    print("\nResult: " + str(result))


main()

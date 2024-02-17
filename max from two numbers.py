def findMax(num1, num2):
    if num1 >= num2:
        print(f"Max is: {num1}")
    else:
        print(f"Max is: {num2}")


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    findMax(num1, num2)

main()
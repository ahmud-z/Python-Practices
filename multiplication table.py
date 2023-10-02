def table(num):
    for i in range(1, 11):
        result = num * i
        print(str(num) + " * " + str(i) + " = " + str(result))


def main():
    num = int(input("Enter a number: "))
    table(num)


main()

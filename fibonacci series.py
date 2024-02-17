def caculateFibonacci(value):
    term1 = 0
    term2 = 1

    if value == 0:
        print(term1)

    print(f"{value} fibonacci numbers: ")
    print(term1)
    print(term2)

    for i in range(2, value):
        nextTerm = term1 + term2
        print(nextTerm)
        term1 = term2
        term2 = nextTerm


def main():
    number = int(input("Enter a number: "))
    caculateFibonacci(number)


main()

def findEvenOddSum(numbers):
    evenSum = 0
    oddSum = 0

    for i in numbers:
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i
    print(f"Sum of even elements: {evenSum}")
    print(f"Sum of odd elements: {oddSum}")


def main():
    numbers = [1, 2, 3, 4, 5]
    findEvenOddSum(numbers)


main()

def bubbleSort(numbers):
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp


def printList(numbers):
    for i in numbers:
        print(f"{i} ", end="")


def main():
    numbers = [3, 56, 48, 6, 45, 8]
    bubbleSort(numbers)
    print(f"Second Highest is: {numbers[1]}")


main()

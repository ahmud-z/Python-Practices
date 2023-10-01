def linearSearch(arr, searchValue):
    for i in range(0, len(arr) - 1):
        if arr[i] == searchValue:
            return i

    return -1


def main():
    arr = [4, 2, 15, 11, 3, 10]
    value = int(input("Enter a value to search: "))

    if linearSearch(arr, value) == -1:
        print("value not found")
    else:
        print("value found at " + str(linearSearch(arr, value)) + " position")


main()

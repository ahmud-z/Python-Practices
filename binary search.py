import math


def binarySearch(arr, left, right, searchValue):
    if right < left:
        return -1

    mid = math.ceil((left + right) / 2)

    if arr[mid] == searchValue:
        return mid

    if searchValue < arr[mid]:
        return binarySearch(arr, left, mid - 1, searchValue)

    if searchValue > arr[mid]:
        return binarySearch(arr, mid + 1, right, searchValue)


def main():
    arr = [1, 2, 3, 4, 5, 6]
    left = 0
    right = len(arr)

    searchValue = int(input("Enter a value to search: "))

    flag = binarySearch(arr, left, right - 1, searchValue)

    if flag == -1:
        print("value not found")
    else:
        print("value found at " + str(flag) + " position")


main()

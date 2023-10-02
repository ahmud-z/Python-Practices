def quickSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp


def main():
    arr = [15,29,30,12,4,21,17,11,1,8,19,13,10,5,9,28,6,25,20,24,3,27,22,18,2,7,14,23,16,26]

    quickSort(arr)

    for i in range(0, len(arr)):
        print(arr[i])


main()

def find_sum(arrayList):
    sum = 0

    print("Given numbers: ", end="")
    for i in arrayList:
        print(f"{i} ", end="")
        sum = sum + i

    return sum


def main():
    arrayList = [6,12,7,1,10]
    sum = find_sum(arrayList)
    print(f"\nSum Result: {sum}")

main()
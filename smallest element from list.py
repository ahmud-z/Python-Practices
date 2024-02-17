def findSmallest(numbers):
    min = numbers[0]
    for i in numbers:
        if i<min:
            min = i
    
    return min

def main():
    numbers = [25,10,3,2,13]
    print(f"Min element of given list: {findSmallest(numbers)}")

main()
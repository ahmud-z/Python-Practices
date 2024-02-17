def findSum(startRange, endRange):
    sum = 0

    print("Calculated Elements: ",end="")

    for i in range(startRange, endRange):
        if(i%3==0 and i%5!=0):
            print(f"{i} ",end="")
            sum+=i
    print(f"\nAddition Result: {sum}",end="")

def main():
    findSum(1,20)

main()
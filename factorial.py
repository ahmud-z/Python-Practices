def findFactorial(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    
    return fact        

def main():
    num = int(input("Enter a number: "))
    print(f"{num} factorial is {findFactorial(num)}" )

main()
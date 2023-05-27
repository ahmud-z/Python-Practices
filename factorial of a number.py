def find_factorial(num):
    fact = 1

    for i in range(1,num+1):
        fact *=i  

    return fact

def main():
    num = int(input("Enter a number: "))

    print(str(num)+" factorial is "+str(find_factorial(num)))


main()    

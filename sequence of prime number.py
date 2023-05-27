def find_prime(n):
    
    for i in range(2,n+1):
        if(i%2!=0):
            print(str(i))

def main():
    num = int(input("Enter a number: "))
    find_prime(num)

main()                
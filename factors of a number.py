def find_facrtors(num):
    print("Factor of "+str(num)+" are:")
    
    for i in range(1, num+1):
        if(num%i==0):
            print(i)

def main():
    num = int(input("Enter a number: "))
    find_facrtors(num)

main()
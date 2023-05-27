def find_sum(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum+i
        
    return sum

         
def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    print("sum of array element: "+str(find_sum(arr)))


main()
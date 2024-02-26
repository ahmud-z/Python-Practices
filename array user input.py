listLength = int(input("Enter array length: "))

listArray = []

for i in range(listLength):
    element = int(input())
    listArray.append(element)

print("Given Array Elements: ", end="")
for i in listArray:
    print(f"{i} ", end="")

#Python program to print all positive number in a range
numberList = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)
for num in numberList:
    if num > 0:
        print(num)

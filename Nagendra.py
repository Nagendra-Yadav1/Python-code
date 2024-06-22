size=int(input("Enter the size of array :->"))
arr=[]
for i in range(size):
    val=int(input("Enter the value of the array:->"))
    arr.append(val)
arr.sort()
print("Secod max :->",arr[-2])
print("second min:->",arr[1])

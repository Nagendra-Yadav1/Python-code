# No argument and no return 
# def sub():
#     a=int(input("enter the value of the first number>>>...."))
#     b=int(input("enter the value of the seond number>>>...."))
#     c=a-b
#     print(c)
# sub()


# argument and no return 
# def add(x,y):
#     c=x+y
#     print(c)
# a=int(input("enter the Value of the first number>>>>...."))
# b=int(input("enter the value of the second number>>>>....."))
# add(a,b)



# def add():
#     c=int(input("Enter the value of thr number>>>...."))
#     print(c)
# a=int(input("Enter the value of the number>>>....."))
# b=int(input("Enter the value of the number>>>....."))
# c=a+b
# add()
# print(c)


# argument with return
# def add(a,b):
#     c=a+b
#     return c
# x=int(input("enter the value of the number>>>>>....."))
# y=int(input("enter the value of the number>>>>......"))
# m=add(x,y)
# print(m)


# no argument with return
# def add():
#     a=int(input("enter the value of the number>>>>>>......"))
#     b=int(input("enter the value of the number>>>>>>....."))
#     c=a+b
#     return c
# x=add()
# print("addition=",x)


# def eveodd(m):
#     if m%2==0:
#         print("even number")
#     else:
#         print("odd number")
# m=int(input("enter the value of the number>>>...."))
# eveodd(m)


# reverse
# def rev(n):
#     rev=0
#     while n>=1:
#         rev=rev*10+n%10
#         n//=10
#     print(rev)
# n=int(input("enter the value of the number>>>>..."))
# rev(n)
# Add two number
# def add(number1,number2):
#     return number1+number2
# a=int(input("Enter the value of the first number :-"))
# b=int(input("Enter the value of the second number :-"))
# result=add(a,b)
# print(result)


# check prime number
# def prime(Number):
#     count=0
#     i=1
#     while(i<=Number):
#         if Number%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         return 1
#     else:
#         return 0
# n=int(input("Enter the value of the number :-"))
# result=prime(n)
# if result==1:
#     print(n,":-This is a Prime")
# else:
#     print(n,":-This is not a prime")
# print("\n")


# find the perfect number
# def perfect(number):
#     sum=0
#     i=1
#     while(i<number):
#         if number%i==0:
#             sum+=i
#         i+=1
#     if sum==number:
#         return 1
#     else:
#         return 0
# n=int(input("Enter the value of the number :-"))
# result=perfect(n)
# if result==1:
#     print(n,"This is perfect number")
# else:
#     print(n,"This is not perfect number")
# print("\n")



# print the star pattern
# def pattern(N):
#     i=1
#     while(i<=N):
#         j=1
#         while(j<=i):
#             print("*",end=" ")
#             j+=1
#         print(" ")
#         i+=1
# n=int(input("Enter the value of the number :-"))
# pattern(n)


# short a list
# def list(size):
#     a=[]
#     i=0
#     while(i<size):
#         m=int(input("Enter the value of the number :-"))
#         a.append(m)
#         i+=1
#     i=0
#     while(i<len(a)-1):
#         j=i+1
#         while(j<len(a)):
#             if a[i]>a[j]:
#                 temp=a[i]
#                 a[i]=a[j]
#                 a[j]=temp
#             j+=1
#         i+=1
#     print("Sorted list :-",a)
#     print("\n")
# n=int(input("Enter the size of the list :-"))
# result=list(n)


# find 1 to n prime number
# def prime(m):
#     count=0
#     j=1
#     while(j<=m):
#         if m%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         return 1
#     else:
#         return 0
# n=int(input("Enter the value of the number :-"))
# i=1
# while(i<=n):
#     result=prime(i)
#     if result==1:
#         print(i)
#     i+=1


# find the armstrong number
# def armstrong(number):
#     k=number
#     a=number
#     count=0
#     while(number>0):
#         count+=1
#         number//=10
#     sum=0
#     while(k>0):
#         sum+=(k%10)**count
#         k//=10
#     if sum==a:
#         return 1
# n=int(input("Enter the value of the number :-"))
# result=armstrong(n)
# if result==1:
#     print(n,":-This is armstrong number")
# else:
#     print(n,"This is not armstrong number")
# print("\n")


# find 1 to n armstrong number
# def armstrong(number):
#     a=number
#     b=number
#     count=0
#     sum=0
#     while(number>0):
#         count+=1
#         number//=10
#     while(a>0):
#         sum+=(a%10)**count
#         a//=10
#     if sum==b:
#         return 1
# n=int(input("Enter the value of the number  :-"))
# i=1
# while(i<=n):
#     result=armstrong(i)
#     if result==1:
#         print(i)
#     i+=1


# find the max of the three number
# def maximum(number1,number2,number3):
#     return max(number1,number2,number3)
# a=int(input("Enter the first value of the number   :-"))
# b=int(input("Enter the second value of the number  :-"))
# c=int(input("Enter the third value of the number   :-"))
# result=maximum(a,b,c)
# print(result)


# sum of the list 
# def listsum(size):
#     i=0
#     a=[]
#     while(i<size):
#         value=int(input("Enter the value of the list  :-"))
#         a.append(value)
#         i+=1
#     print("Orignal list :-",a)
#     sum=0
#     for i in range(size):
#         sum+=a[i]
#     return sum
# n=int(input("Enter the size of the list  :-"))
# result=listsum(n)
# print("Sum of the list :-",result)


# multiply of the list
# def multilist(size):
#     i=0
#     a=[]
#     while(i<size):
#         value=int(input("Enter the value of the list :-"))
#         a.append(value)
#         i+=1
#     print("Orignal list :-",a)
#     multiply=1
#     for i in range(size):
#         multiply*=a[i]
#     return multiply
# n=int(input("Enter the size of the list :-"))
# result=multilist(n)
# print("Multiply of the list :-",result)


# reverse  string
# def reverse(string):
#     a=string[: :-1]
#     return a
# n=input("Enter the element of the strin :-")
# result=reverse(n)
# print("reverse of the strint:-",result)
# print("\n")


# Factorial of the number
# def factorial(number):
#     fact=1
#     i=1
#     if number>0:
#         while(i<=number):
#             fact*=i
#             i+=1
#         return fact
#     else:
#         return 1
# n=int(input("Enter the value of the number  :->"))
# result=factorial(n)
# if result==1:
#     print("This is not positive number")
# else:
#     print(result)
# print("\n")



# count the string character upper and lower case
# def find(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for i in s:
#         if i.isupper():
#            d["UPPER_CASE"]+=1
#         elif i.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])
# n=input("Enter the element of the string :-")
# result=find(n)

# def find(String):
#     countUpper=0
#     countLower=0
#     flag=1
#     for i in String:
#         if i.isupper():
#             countUpper+=1
#         else:
#             countLower+=1
#     print("Count the Upper elements :-",countUpper)
#     print("Count the Lower elements :-",countLower)
# n=input("Enter the element into the list :-")
# print("Original String :-",n)
# result=find(n)



# remove the dublicate element in the list
# def unique(size):
#     a=[]
#     for i in range(size):
#         value=int(input("Enter the value of the list :-"))
#         a.append(value)
#     print("Orginal list :-",*a)
#     b=[]
#     [b.append(i) for i in a if i not in b]
#     print("Unique value :-",*b)
# n=int(input("Enter the size of the list :-"))
# result=unique(n)


# def unique(size):
#     a=[]
#     for i in range(size):
#         value=int(input("Insert the value of the list :-"))
#         a.append(value)
#     print("Original Element :-",*a)
#     b=list(set(a))
#     print("Uique Elements :-",*b)
# n=int(input("Enter the size of the list :-"))
# result=unique(n)


# find the even element in the list
# def prime(size):
#     a=[]
#     for i in range(size):
#         value=int(input("Enter the eliment of the list :-"))
#         a.append(value)
#     print("Orignal list :-",a)
#     b=[]
#     [b.append(i) for i in a if i%2==0]
#     print("Even list :-",b)
# n=int(input("Enter the size of the list :-"))
# result=prime(n)


# find the perfect number
# def perfect(number):
#     sum=0
#     for i in range(1,number):
#         if number%i==0:
#             sum+=i
#     if sum==number:
#         return 1
#     else:
#         return 0
# n=int(input("Enter the value of the number :-"))
# result=perfect(n)
# if result==1:
#     print("perfect number :-",n)
# else:
#     print("Not perfect number:-",n)
# print("\n")


# find 1 to n perfect number
# def perfect(number):
#     sum=0
#     for i in range(1,number):
#         if number%i==0:
#             sum+=i
#     if sum==number:
#         return 1
#     else:
#         return 0

# n=int(input("Enter the value of the nuber :-"))
# i=1
# while(i<=n):
#     result =perfect(i)
#     if result==1:
#         print(i)
#     i+=1


# check the string is palidrom or not
# def palidrom(string):
#     m=string
#     b=string[-1::-1]
#     if m==b:
#         return 1
#     else:
#         return 0
# n=input("Enter the element of the string :-")
# result =palidrom(n)
# if result==1:
#     print("This is palidrom number :-",n)
# else:
#     print("This is not palidrom number :-",n)


# find the pascal triangle 
# def pascal_triangle(number):
#     a=[1]
#     b=[0]
#     for i in range(number):
#         print(a)
#         a=[i+r for i,r in zip(a+b,b+a)]
# n=int(input("Enter the value of the number :-"))
# result=pascal_triangle(n)


# find the binary search
# def binarysearch(a,size,key):
#     i=0
#     j=size-1
#     flag=0
#     while(i<=j) and flag==0:
#         mid=(i+j)//2
#         if a[mid]==key:
#             pos=mid+1
#             flag=1
#         if key>a[mid]:
#             i=mid+1
#         if key<a[mid]:
#             j=mid-1
#     if flag==1:
#         print("Number found in ",pos,"position of the list")
#     else:
#         print("Number not found in the list")
#     print("")
# size=int(input("Enter the value of the number :-"))
# a=[]
# for i in range(size):
#     value=int(input("Ensert the value of the list :-"))
#     a.append(value)
# a.sort()
# print("orignal list :-",a)
# key=int(input("Search the value of the list :-"))
# result=binarysearch(a,size,key)


# def sum(n):
#     if n==1:
#         return 1
#     return(n+sum(n-1))
# n=int(input("Enter the value of the number :->"))
# sum(n)
# a=sum(n)
# print(a)


# def sum(n):
#     if n==1:
#         return 1
#     return(n**2+sum(n-1)**2)
# n=int(input("enter the value of the number  :->"))
# sum(n)
# a=sum(n)
# print(a)


# playing with the function
# def Enqueue(a):
#     a.append(value)
#     print(a)
#     print("Enequeue element successfully")
# def Dequeue(a):
#     x=a.pop()
#     print(x)
#     print("Dequeue element successfully")
# def Peak(a):
#     print(a[0])
#     print("Peak eleent successfully")
# def Display(a):
#     for i in a:
#         print(i,end=" ")
#     print('')
#     print("Display element successfully")
# a=[]
# while True:
#     choise=int(input("1=Enqueue of the element\n2=Dequeue of the element\n3=Bottom of the element\n4=Display of the element\n5=Exit of the group\n6=Choose given the option\nPlease choose your opstion:->"))
#     if choise==1:
#         value=int(input("enter the Enqueue of the element :->"))
#         Enqueue(a)
#     elif choise==2:
#         if len(a)==0:
#             print("Queue underflow")
#         else:
#             Dequeue(a)
#     elif choise==3:
#         if len(a)==0:
#             print("Queue underflow")
#         else:
#             Peak(a)
#     elif choise==4:
#         if len(a)==0:
#             print("Queue underflow")
#         else:
#             Display(a)
#     elif choise==5:
#         if len(a)==0:
#             print("Queue underflow")
#         else:
#             print("EXIT GROUP")
#     else:
#         print("Please choose the given option")


# playing with the function
# def push(a,value):
#     a.append(value)
#     print(a)
#     print("asserted successfully")
#     print("")
# def pop(a):
#     x=a.pop()
#     print(x)
#     print("Pop element successfully")
#     print("")
# def peak(a):
#     m=len(a)-1
#     print(a[m])
#     print("Peak element successfully")
#     print("")
# def display(a):
#     n=len(a)-1
#     for i in range(n,-1,-1):
#         print(a[i])
#     print("Display element successfully")
#     print("")
# a=[]
# while True:
#     choice=int(input("1=Push the element\n2=Pop the element\n3=Peak the element\n4=Display all the element\n5=Exit the choice\nPlease choose the given option\n>>>>>>>>>>......."))
#     if choice==1:
#         value=int(input("Enter the Push elements>>>>>...."))
#         push(a,value)
#     elif choice==2:
#         if len(a)==0:
#             print("Stack underflow")
#         else:
#             pop(a)
#     elif choice==3:
#         if len(a)==0:
#             print("stack underflow")
#         else:
#             peak(a)
#     elif choice==4:
#         if len(a)==0:
#             print("stack underflow")
#         else:
#             display(a)
#     elif choice==5:
#         if len(a)==0:
#             print("Stack underflow")
#         else:
#             print("EXIT")
#     else:
#         print("Please choose the given option")


# make the calculater
# def add(x,y):
#     c=x+y
#     print("Addition of the number :->",c)
#     print()
# def sub(x,y):
#     c=x-y
#     print("Subtration of the number :->",c)
#     print()
# def mult(x,y):
#     c=x*y
#     print("Multiplication of the numbers :->")
#     print()
# def div(x,y):
#     c=x/y
#     print("Division of the number :->",c)
#     print()
# def rim(x,y):
#     c=x%y
#     print("Riminders of the numbers :->",c)
#     print()
# while(True):
#     a=int(input("Enter the first number  :-"))
#     b=int(input("Enter the second number :-"))
#     print("1 :-> Addition(+) of the numbers\n2 :-> Substraction(-) of the numbers\n3 :-> Multiplication(*) of the numbers\n4 :-> Division(\) of the numbers\n5:-> Riminder(%)of the numbers\n6 :-> EXIT")
#     n=input("Select your option :-")
#     if n=="1":
#         add(a,b)
#     elif n=="2":
#         sub(a,b)
#     elif n=="3":
#         mult(a,b)
#     elif n=="4":
#         div(a,b)
#     elif n=="5":
#         rim(a,b)
#     elif n=="6":
#         print("Exit")
#         break
#     else:
#         print("Please choose your given option")



# consecatine number

# def Consecutive(arr):
#   arr.sort()
#   c=0
#   for i in range(len(arr)-1):
#     while arr[i+1] - arr[i] !=1 :
#       if arr[i]>0:
#         arr[i]+=1 
#         c+=1
#       else:
#         while arr[i+1] - arr[i] !=1:
#           arr[i]+=1 
#           c+=1 

#   # code goes here
# #   return c

# # keep this function call here 
# print(Consecutive(input()))


# power of the two number
# def PowersofTwo(num):
#   arr=[]
#   for i in range(num+1):
#     arr.append(2**i)
#   if num in arr:
#     return 'true'
#   else:
#     return 'false'

# keep this function call here 
# num=int(input())
# print(PowersofTwo(num))

































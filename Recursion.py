#sum of the element
# def sum(number):
#     if number==1:
#         return 1
#     else:
#         return (number+sum(number-1))
# n=int(input("Enter the value of the number :-"))
# result=sum(n)
# print("Sum of the Element :-",result)


# Factorial of the number
# def find(number):
#     if number==1:
#         return 1
#     else:
#         return (number*find(number-1))
# n=int(input("Enter the value of the number :-"))
# result=find(n)
# print(result)



# print 1 to n number
# def increasing(number,x):
#     if number==0:
#         return
#     print(x)
#     return increasing(number-1,x+1)
# n=int(input("Enter the value of the number :-"))
# print("   -:Increasing the number :-")
# result=increasing(n,1)


# print the number n to 1
# def decreasing(number):
#     if number==0:
#         return
#     print(number)
#     return decreasing(number-1)
# n=int(input("Enter the value of the number :-"))______
# result=decreasing(n)


# print the table
# def table(number,x):
#     if number==0:
#         return
#     print(n," x ",x,"=",n*x)
#     table(number-1,x+1)
# n=int(input("Enter the value of the number :-"))
# result=table(10,1)


# reverse the string
# def reverse(string,len):
#     if len==-1:
#         return
#     print(string[len],end="")
#     return reverse(string,len-1)
# s=input("Enter the character of the string :-")
# result=reverse(s,len(s)-1)


# reverse the character
# def reverse(string,len):
#     if len==0:
#         print(string[0])
#     else:
#         print(string[len],end="")
#         return reverse(string,len-1)
# s=input("Enter the character of the string :-")
# result=reverse(s,len(s)-1)


# find the power of the base and power
# def power(x,y):
#     if y==0:
#         return 1
#     else:
#         return x*power(x,y-1)
# x=int(input("Enter the value of the base :-"))
# y=int(input("Enter the value of the power :-"))
# result=power(x,y)
# print(result)


# find the febonaci series
# def febonaci(number):
#     if number==1:
#         return 0
#     if number==2:
#         return 1
#     return febonaci(number-1) + febonaci(number-2)
# n=int(input("Enter the value of the number :-"))
# for i in range(1,n+1):
#     result=febonaci(i)
#     print(result)


# print the star pattern in asending order
# def pattern(n,i=1):
#     if i>n:
#         return
#     print("* "*i)
#     return pattern(n,i+1)
# n=int(input("Enter the value of the number :-"))
# pattern(n)


# print the patern in desending order
# def pattern(n,i=1):
#     if i>n:
#      return
#     print("* "*n)
#     return pattern(n-1,i)
# n=int(input("Enter the value of the number :-"))
# pattern(n)


# print the square pattern
# def pattern(n,i=1):
#     if i>n:
#         return
#     print("* "*n)
#     return pattern(n,i+1)
# n=int(input("Enter the value of the number :->"))
# pattern(n)




n=int(input("Enter the value of the number:->"))
count=0
i=0
while(i<n):
    j=0
    while(j<=i):
        if(j==0):
            print(count,end=" ")
            j+=1
        else:
            print("N",end=" ")
            j+=1
    print("")
    count=2**i
    i+=1













      


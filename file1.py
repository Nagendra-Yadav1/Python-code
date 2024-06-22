#write a program to print from 1 to 1o
# i=1
# while i<=10:
#     print(i)
#     i+=1




#write a program to print from 1 to n
# n=int(input("ente the number>>>....."))
# i=1
# while i<=n:
#     print(i)
#     i+=1




#write a program to print from 10 to 1
# i=10 
# while i>=1:
#     print(i)
#     i-=1




#write a program to print from n to 1
# n=int(input("enter the number>>>>....."))
# while n>=1:
#     print(n)
#     n-=1




# write a program to print sum of n to 1
# sum=0
# n=int(input("enter the number>>>...."))
# while n>=1:
#     sum=sum+n
#     n-=1
# print("sum of the number=",sum)




#write a program to print sum of 1 to n
# sum=0
# i=1
# n=int(input("enter the number>>>...."))
# while i<=n:
#     sum=sum+i
#     i+=1
# print("sum of the number=",sum)




#write a program to print sum of square of 1 to n
# sum=0
# j=1
# n=int(input("enter the number>>>>...."))
# while j<=n:
#     sum+=j**2
#     j+=1
# print("sum of the square number=",sum)


#write a program to print sum of square of 1 to n
# sum=0
# j=1
# n=int(input("enter the number>>>>...."))
# while j<=n:
#     sum+=j**3
#     j+=1
# print("sum of the square number=",sum)


#write a program to print only even number between 1 to n
# n=int(input("enter the number>>....."))
# i=2
# while i<=n:
#     print("even number of=",i)
#     i+=2


#write a program to print only even number between 1 to n
# n=int(input("enter the number>>....."))
# i=1
# while i<=n:
#     if i%2==0:
#         print("even number of=",i)
#     else:
#         print("odd number  of=",i)
#     i+=1


#write a program to find the sum of even number between to 1 to n
# n=int(input("enter the number>>>>>......"))
# i=2
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=2
# print("sum of the number=",sum)


#write a program to find the sum of even number between to 1 to n
# n=int(input("enter the number>>>>>......"))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum=sum+i
#     i+=1
# print("sum of the even numbe=",sum)


#write a program to find sum of first n even number
# n=int(input("enter the number>>>>>......"))
# sum=0
# count=0
# i=1
# while count<n:
#     if i%2==0:
#         sum=sum+i
#         count=count+1
#     i+=1
# print("sum of even number=",sum)


#write a program to find sum of digits of a given number
# n=int(input("enter the number>>>>>>>>...."))
# sum=0
# while n>=1:
#     sum=sum+n%10
#     n//=10
# print("sum of given digit=",sum)


# write a program to find product of digits of a given number
# n=int(input("enter the number>>>>>>>>...."))
# product=1
# while n>=1:
#     product*=n%10
#     n//=10
# print("poduct of given digit=",product)


#write a program to find sum of even digits and product of odd digits of agiven number
# product=1
# sum=0
# i=1
# n=int(input("enter the value of number>>>......"))
# while n>=1:
#     if n%2==0:
#         sum=sum+n%10
#     else:
#         product*=n%10
#     n//=10
# print("sum of even number=",sum)
# print("product of odd num=",product)


#write a program to find sum of digits square of a given number
# n=int(input("enter the number>>>>>>>>...."))
# sum=0
# while n>=1:
#     sum=sum+(n%10)**2
#     n//=10
# print("sum of given digit sqaure=",sum)


#write a program to find sum of digits  cube of a given number
# n=int(input("enter the number>>>>>>>>...."))
# sum=0
# while n>=1:
#     sum=sum+(n%10)**3
#     n//=10
# print("sum of given digit cube=",sum)


#write a python program to check weather a given number is Armstrong or not
# n=int(input("enter the number>>>>>>>>...."))
# a = n
# sum=0
# while n>0:
#     sum=sum+(n%10)**3
#     n//=10
# if sum==a:
#     print("number armstrong")
# else:
#     print("number is not armstrong")


#write a program to reverse the given value
# n=int(input("enter the digit of the number>>>>....."))
# a=0
# while n>=1:
#     a=a*10+n%10
#     n//=10
# print("reverse the number=",a)


# n=int(input("enter the digit of the number>>>>....."))
# a=0
# c=n
# while n>=1:
#     a=a*10+n%10
#     n//=10
# if a==c:
#     print("Palidrom")
# else:
#     print("Not palidrom")
    
    
#wwrite a program to print factors of given number
# n=int(input("enter the value of the number>>>......"))
# i=1
# while n>0:
#     print(n,end="*")
#     i=n*i
#     n-=1
# print("=",i)

                                            
# x=0
# y=1
# z=0
# i=1
# n=int(input("enter the number>>>>....."))
# while i<=n:
#     print(z,end=" ")
#     x=y
#     y=z
#     z=x+y
#     i+=1


# x=0
# y=1
# z=0
# i=1
# n=int(input("enter the value of the number>>>>....."))
# while i<=n:
#     print(i*z)
#     x=y
#     y=z
#     z=x+y
#     i=i+1




# a="navgurukul"
# b=len(a)//2
# c=(b+1)
# d=(b-1)
# print((a[d].title()),(a[b].title()),(a[c]).title())



# a="nagendra"
# b="#"
# c=b*1000
# print(a+c)


# write a program to check wether a number is prime or composite 
# n=int(input("enter the number>>>......"))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count=count+1
#     i+=1
# if count==2:
#     print("prime    number=",n)
# else:
#     print("composite number=",n)


# a=12345
# print((((((((a%10*10)+(((a//10)%10)))*10)+(a//100)%10)*10)+(a//1000)%10))*10+(a//10000%10))


# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1


# for x in range(6):
#     for y in range(x):
#         print("*",end="")
#     print("")


# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(" ",end="")
#         j=j+1
#     k=1
#     while k<=i:
#         print("*",end="")
#         k+=1
#     print("")
#     i+=1


# n=5
# for x in range(n,-1,-1):
#     for x in range(x):
#         print("*",end="")
#         for x in range(5):
            
    
# n=5
# for x in range(n):
#     print("*",end="L*")
#     print("")
# for x in range(5):
#     print("*",end="L")
# print("")


# for x in range(10,0,-1):
#     for y in range(x):
#         print("*",end="")
#     print("")



# a=5
# n=int(input("enter the value of number>>>>......"))
# for x in range(n):
#     for m in range(a-n):
#         print(" ",end="")
#     for y in range(2*n-1):
#         print("*",end="")
#     n=n-1
#     print("")



# n=int(input("enter the value of the number>>>>....."))
# i=10
# while i<=n:
#     print(i,end=" ")
#     i=i+10
# print("")




# n=int(input("enter the value of the number>>>>......"))
# while n>=7:
#     print(n,end=" ")
#     n-=7
# print("")




# n=int(input("enter the number>>>......."))
# while n>=1:
#     print(n)
#     n-=1




# n=int(input("enter the number>>>>....."))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("sum of the number=",sum)
    
    
    
    
# n=int(input("enter the number>>>....."))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print("sum of the even number=",sum)




# n=int(input("enter the number>>>>....."))
# i=1
# while i<=n:
#     if i%7==0:
#         print("divide by 7=",i)
#     i=i+1




# n=int(input("enter the value of the number>>>......"))
# i=1
# while i<=n:
#     print(i*i,end=" ")
#     i=i+1
# print("")




# n=int(input("enter the value of the number>>>......"))
# sum=0
# i=1
# while i<=n:
#     print(i**3,end=" + ")
#     sum=sum+i**3
#     i=i+1
# print("  =",sum)
# print(" ")




# n=int(input("enter the number>>>....."))
# sum=0
# i=1
# j=1
# while i and j<=n:
#     print(i*j)
#     j=j+1
#     i=i+1




# i=1
# product=1
# n=int(input("enter the value of the number>>>>......."))
# while i<=n:
#     product*=i
#     print(product,end=" + ")
#     i=i+1
# print("")





# n=int(input("enter the number>>>....."))
# i=1
# while i<=n:
#     print("1/",i,end="!+ ")
#     i=i+1
# print(" ")




# n=int(input("enter the number>>>....."))
# i=1
# while i<=n:
#     print("x",i,"/",i,end="! + ")
#     i=i+1
# print(" ")




# n=int(input("enter the number>>>>....."))
# a=65
# for x in range(n):
#     for y in range(n-x):
#         print("",end="")
#     for j in range(x):
#         print(chr(a),end="")
#         a=a+1
#     print("")



# for i in range(5):
#     print(i)

# for i in (1,2,3):
#     print(i)

# for i in range(10):
#     if i%2!=0:
#         print("hello")


# for i in range(10,2,-2):
#     print("hello")



# str="python output based questions"
# word=str.split()
# for x in word:
#     print(x)




 # for x in range(7,10):
#     print("python output based questions")
# print("python output based questions")








# L,R=map(int,input().split())
# while L<=R:
#     if L%2==0:
#         L=L+1
#         continue
#     else:
#         print(L)
#     L=L+1



# N=int(input())
# for x in range(N+1):
#     for y in range((N+1-x)):
#         print(" ",end="")
#     for z in range(x):
#         print("*",end="")



# n=int(input("enter the value of the number>>>....."))
# for x in range(n):
#     for y in range(n-x):
#         print(x,end="")
#     for z in range(2*x-1):
#         print("*",end="")
#     print("")
# for a in range(n,0,-1):
#     for b in range(n-a):
#         print("N",end="")
#     for c in range(2*a-1):
#         print("*",end="")
#     print(" ")




# n=int(input("enter the value of the number>>......."))
# for x in range(2,n):
#     flag=0
#     if n%x==0:
#         flag=1
#         break
# if flag==1:
#     print("not prime number")
# else:
#     print("prime number")




# n=int(input("enter the value of the number>>....."))
# flag=0
# i=2
# while i<=n:
#     if n%i==0:
#         flag=1
#         break
#     i=i+2
# if flag==0:
#     print("prime number")
# else:
#     print("not prime number")




# n=int(input("enter the value of the number>>......"))
# i=2
# while i<=n:
#     flag=0
#     for x in range(2,i):
#         if i%x==0:
#             flag=1
#             break
#     if flag==0:
#         print(i)
#     i=i+1




# a=list(range(5))
# for i in range(len(a)):
#       a[i]=a[i]**2
# print(a)




# for x in range(1,11):
#     print("2 X",x,"=",2*x)



# m=1
# for i in range(10):
#     for j in range(i):
#         print(m,end=" ")
#         m=m+1
#     print("")




# for i in range(10):
#     if i%2==0:
#         print("even number=",i)  
#     else:
#         print("odd  number=",i)





# for i in range(0,5):
#     for j in range(i):
#         print("*",end="")
#     print("")



# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")



# m=0
# for x in range(5):
#     for x in range(3):
#         m+=1
#         print(m,end=" ")
#     print("")


# s=0
# n=10
# for x in range(1,n+1,1):
#     s+=x
# print("sum of",s)



# a=eval(input("enterthe number>>>>..."))
# for x in range(1,a+1,1):
#     print(x,"square of =",x*x)



# a=eval(input("enter the value>>>..."))
# for x in range(1,a+1,1):
#     print(x,"cube of =",x*x*x)



# a="python"
# l=len(a)-1
# for x in (range(l,-1,-1)):
#     print("indexing value:=",x ,"and find the vaue:=",a[x])



# a="python"
# b=len(a)-1
# for x in reversed(range(b)):
#     print("Indexing Value:=",x,"And reverse value=",a[x])




# n=10
# while(n!=0):
#     n=n-1
#     print(n,end=" ")
# print(" ")




#a=input("enter the chr>>>>>>>")
#for x in a:
#		print(x,"#")


#for num in range(10,14):
#	for i in range(2,num):
#		if(num%i==1):
#			print(num,end=",")
#			break



#sum=0
#for x in range(2,7):
#	sum+=x
#print(sum)



#value=list(range(132,78,-12))
#print(value)


# a=list(range(4,1,-1))
# print(a)



# for x in range (1,101):
#     if x==1:
#         print("odd   number=",x)
#     elif x==2:
#         print("prime number=",x)
#     elif x%2==0:
#         print("even  number=",x)
#     elif x%2==0 or x%3==0 or x%5==0:
#         print("odd   number=",x) 
#     else:
#         print("prime number=",x)


# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print(i*j,end="* *")
#         j=j+1
#     i=i+1
#     print("")




# n=int(input("enter the value of th number>>>...."))
# for x in range(n,-1,-1):
#     for j in range(2*n-1):
#         print(x,end="")
#     n-=1
#     print()




# A=5 
# a=5
# for x in range (A):
#     for y in range(a-x):
#         print(" ",end="")
#     for n in range(2*x-1):
#         print("*",end="")
#     print("")





# A=5 
# a=5
# for x in range (A,-1,-1):
#     for y in range(a-A):
#         print(" ",end="")
#     for n in range(2*A-1):
#         print(x,end="")
#     A-=1
#     print("")



# a=[10,20,30,40,50]
# for x,v in enumerate(a):
#     print("indexing value=",x,"::value of list=",v)



# a="Nagendra Yadav,Amit Yadav,Shivam Yadav,Siddhant Ydav"
# for x in a.split():
#     print(x)



# a=[10,20,30,40,50,60,70,80]
# for x,v in enumerate(a):
#     print("number[",x,"]=",v)



# a=range(10).start
# b=range(10).step
# c=range(10).stop
# print(a,c,b)



# a=[10,20,30,40,50,60,70,]
# b=[50,30,40,50,60]
# for x in a+b:
#     print(x,end=" ")
# print("")



# for x in range(10):
#     print(x)
#     x+=1



# for x in range(10):
#     print(x)




# n=int(input("enter the number>>>>...."))
# i=2
# m=0
# while i<=n:
#     if n%i==0:
#         m=1
#         break
#     i+=2
# if m==1:
#     print(" evan number")
# else:
#     print("odd number")




# n=int(input("enter the number>>>>....."))
# a=0
# while n>=1:
#     a=(a*10+n%10)
#     n//=10
# print(a) 



# a=1
# while a<=10:
#     print(a)
#     a=a+1


# n=int(input("enter the number>>>...."))
# i=0
# while i<=n:
#     print(i)
#     i+=1


# i=10
# while 1<=i:
#     print(i)
#     i-=1



# n=int(input("enter the number>>>...."))
# while 1<=n:
#     print(n)
#     n-=1



# n=int(input("enter the number>>>...."))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)



# n=int(input("enter the number>>>...."))
# sum=0
# while 1<=n:
#     sum=sum+n
#     n-=1
# print(sum)


# n=int(input("enter the number>>>...."))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i*i
#     i+=1
# print(sum)



# n=int(input("enter the number>>>...."))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i**3
#     i+=1
# print(sum)




# n=int(input("enter the number>>>....."))
# i=2
# while i<=n:
#     print("even number=",i)
#     i+=2




# n=int(input("enter the number>>>>...."))
# i=1
# while i<=n:
#     if i%2==0:
#         print("even number",i)
#     i+=1




# n=int(input("enter the number>>>>...."))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum=sum+i
#     i+=1
# print("sum of even number=",sum)




# n=int(input("enter the digit>>>....."))
# sum=0
# while 1<=n:
#     sum=sum+n%10
#     n//=10
# print("sum of digit=",sum)


# n=int(input("enter the digit>>>....."))
# sum=1
# while 1<=n:
#     sum*=n%10
#     n//=10
# print("product of digit=",sum)



# n=int(input("enter the digit>>>...."))
# sum=0
# product=1
# while 1<=n:
#     if n%2==0:
#         sum=sum+n%10
#     else:
#         product*=n%10
#     n//=10
# print("sum of even number=",sum)
# print("product of odd number",product)


# n=int(input("enter the digit>>>....."))
# sum=0
# while 1<=n:
#     sum+=(n%10)**2
#     n//=10
# print("product of digit=",sum)


# n=int(input("enter the digit>>>....."))
# sum=0
# while 1<=n:
#     sum+=(n%10)**3
#     n//=10
# print("product of digit=",sum)


# n=int(input("enter the number>>>>....."))
# i=1
# while n>=1:
#     print(n,end="*")
#     i=n*i
#     n-=1
# print("=",i)


# i=2
# while i<=20:
#     if i==16:
#         i=i+2
#         continue
#     print(i)
#     i=i+2


# i=1 
# while i<=5: 
#     print(i)
#     if i==4:
#         continue
#     i=i+1
    
# n=int(input("ENter the  number :->"))
# a=0
# b=1
# z=0
# for i in range(n+1):
#     print(z)
#     a=b
#     b=z
#     z=a+b


# a=int(input("Enter th value of the number :->"))
# b=int(input("Enter th value of the number :->"))
# c=int(input("Enter th value of the number :->"))
# max=0
# smax=0
# if a>b:
#     max=a
#     smax=b
# else:
#     max=b
#     smax=a
# if max>c:
#     if smax>c:
#         smax=smax
#     else:
#         smax=c
# else:
#     d=max
#     max=c
#     smax=d
# print("maximum number :->",max)
# print("Second Maximum :->",smax)




n=int(input("Enter the value of the number:->"))
count=0
count1=1
i=1
while(i<=n):
    j=1
    while(j<=i):
        if j==1:
            print(count,end=" ")
        else:
            print(2**count1,end=" ")
        j+=1
    print("")
    count=2**i
    i+=1
    count1+=1
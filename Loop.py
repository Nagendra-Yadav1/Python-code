# for x in range(1,11):
#     print("2 X",x,"=",2*x)



# m=1
# for i in range(10):
#     for j in range(i):
#         print(m,end="")
#         m=m+1
#     print("")




# for i in range(10):
#     if i%2==0:
#         print("even number=",i)  
#     else:
#         print("odd  number=",i)



# n=int(input("enter the number>>>....."))
# for x in range(n):
#     print()
#     if x%2==0 or x%3==0 or x%5==0:
#         print("THIS IS NOT PRIME NUMBER=",x)
#     else:
#         print("PRIME NUMBER            =",x)



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
    




# n=int(input("Enter the value of the number>>>>>......"))
# i=1
# y=" "
# a=1
# while n>0:
#     y+="*"*(n-1)
#     y+=str(a*a)
#     n-=1
#     a=a*10+1
#     print(y)
#     y=" "




# paskal triangle
# K=int(input("Enter the value of the value of the number    :-"))
# i=1
# i=0
# while i<=K:
#     j=1
#     while j<=K-i+1:
#         print(" ",end="")
#         j+=1
#     n=1
#     s=i
#     while s>0:
#         n*=s
#         s-=1
#     j=0
#     while j<=i:
#         m=i-j
#         n_r=1
#         while m>0:
#             n_r*=m
#             m-=1
#         r=1
#         y=j
#         while y>0:
#             r*=y
#             y-=1
#         ncr=n//(r*(n_r))
#         print(ncr,end="  ")
#         j+=1
#     print(" ")
#     i+=1



# paskal triangle
# n=int(input("Enter the value of the number>>>>>>>.  >:"))
# i=1
# while i<=2*n-1:
#     print(chr(i+64),end=" ")
#     i+=1
# print("")
# i=1
# while i<=n:
#     j=1
#     m=1
#     while j<=n-i:
#         print(chr(m+64),end=" ")
#         j+=1
#         m+=1
#     j=1
#     while j<=2*i-1:
#         print(" ",end=" ")
#         j+=1
#         m+=1
#     j=1
#     while j<=n-i:
#         print(chr(m+64),end=" ")
#         j+=1
#         m+=1
#     print(" ")
#     i+=1



# n=int(input("Enter the value of the number>>>>>>>.......  :>"))
# i=1
# while i<=n:
#     j=1
#     m=1
#     while j<=n-i:
#         print(" ",end=" ")
#         j+=1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     j=1
#     k=i-1
#     while j<=i-1:
#         print(k,end=" ")
#         k-=1
#         j+=1
#     print("")
#     i+=1



# special pattern
# n=int(input("Enter the value of the number>>>>>>>>>  :>"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         if j<i:
#             print(j,end="")
#         else:
#             print(i,end="")
#         j+=1
#     j=1
#     while j<=2*i-1:
#         print("",end=" ")
#         j+=1
#     j=1
#     while j<=n-i:
#         if j<i:
#             print(j,end="")
#         else:
#             print(i,end="")
#         j+=1
#     print(" ")
#     i+=1


# find the power of the number
# base=int(input("Enter the value of the base>>>>>>>...   :>"))
# power=int(input("Enter the value of the power>>>>>>.....:>"))
# i=1
# fact=1
# while i<=power:
#     fact*=(base)
#     i+=1
# print(fact)


# n=int(input("Enter the value of the number>>>>>......"))
# count=0
# a=n
# while n>0:
#     rev=n%10
#     count+=1
#     n//=10
# sum=0
# while a>0:
#     rev=a%10
#     i=1
#     fact=1
#     while i<=count:
#         fact*=rev
#         i+=1
#     sum+=fact
#     print(sum)
#     a//=10


# sum of the factorial number
# n=int(input("ENter the value of the number>>>>>>>>>>>>>>   :>"))
# x=int(input("ENter the value of the x>>>.>>>>>>>>>..  :>"))
# i=1
# sum=0
# while i<=n:
#     j=1
#     pro=1
#     while j<=i:
#         pro*=j
#         j+=1
#     sum+=(x)/pro
#     x=x*x
#     i+=1
# print(sum)


#  jigjag pattern
# while(True):
#     y=" "
#     i=0
#     while(i<=8):
#         y+=str(i*" ")+str(8*"*")
#         print(y)
#         i+=1
#         y=" "
#     m=" "
#     n=7
#     while(n>=0):
#         m+=str(n*" ")+str(8*"*")
#         n-=1
#         print(m)
#         m=""




# butter fly pattern
# n=int(int(input("Enter the value of the number  :- ")))
# i=0
# while(i<n):
#     j=0
#     while(j<=i):
#         print("*",end=" ")
#         j+=1
#     j=0
#     while(j<=(2*(n-i))-1):
#         print(" ",end=" ")
#         j+=1
#     j=0
#     while(j<=i):
#         print("*",end=" ")
#         j+=1
#     print(" ")
#     i+=1
# i=0
# while(i<=n):
#     j=0
#     while(j<=n-i):
#         print("*",end=" ")
#         j+=1
#     j=0
#     while(j<=(2*i)-1):
#         print(" ",end=" ")
#         j+=1
#     j=0
#     while(j<=n-i):
#         print("*",end=" ")
#         j+=1
#     print(" ")
#     i+=1


# import time
# start=time.time()
# for i in range(1,101):
#     print(i)
# print(time.time()-start)


# import time 
# start=time.time()
# i=0
# while(i<101):
#     print(i)
#     i+=1
# print(time.time()-start)














    



    










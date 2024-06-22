
# Question 1
#find divisible 11 and 5
# N=int(input())
# if N%5==0 or N%11==0:
#     print("ONE")
# elif N%5==0 and N%11==0:
#     print("BOTH")
# else:
#     print("NONE")


# QUESTION 2
# N=int(input())
# if N%5==0 or N%6==0:
#     print("YES")
# else:
#     print("NO")


# QUESTION 3
# a,b,x,y=map(int,input().split())
# print(a*x+b*y)



# QUESTION 4
# L,R=map(int,input().split())
# while R>=L:
#     if L%2!=0:
#         print(L)
#         L=L+1
#         continue
#     L=L+1



# QUETION 4
# L,R=map(int,input().split())
# while R>=L:
#     if R%L==0:
#         print(L)
#         L=L+1
#         continue
#     L=L+1



# QUESTION 5
# N=int(input())
# i=1
# sum=0
# count=0
# add=0
# while count<N:
#     if i%2==0:
#         sum=sum+i
#         count+=1
#     else:
#         add+=i
#     i=i+1
# print(add,sum)



# QUESTION 5
# N=int(input())
# sum=0
# add=0
# for x in range(N*2+1):
#     if x%2==0:
#         sum=sum+x
#     else:
#         add=add+x
# print(add,sum)



# QUESTION 6
# a,b,c=map(int,input().split())
# if (a>0 and b>0 and c>0) and (a+b)>c and (b+c)>a and (c+a)>b:
#         print("YES")
# else:
#         print("No")


# QUESTION 7
# N=int(input())
# for x in range(N+1):
#     for y in range(N+1-x):
#         print(" ",end="")
#     for z in range(x):
#         print("*",end="")




# QUESTION 7
# N=int(input())
# for x in range(N+1):
#     for y in range(N,0,-1):
#         print(" ",end="")
#     for z in range(x):
#         print("*",end="")



# QUESTION 8
# A=int(input())
# B=int(input())
# C=int(input())
# if A>B>C or C>B>A:
#     print(B)
# elif B>A>C or C>A>B:
#     print(B)
# else:
#     print(C)



# QUESTION 9
# a,b,c=map(int,input().split())
# if (a>0 and b>0 and c>0) and (a+b+c==180):
#     print("YES")
# else:
#     print("NO")


# QUESTION 10
# N=int(input())
# sum=0
# for x in range(N+1):
#     sum=sum+x
# print(sum)


# QUESTION 10
# N=int(input())   
# print((N*(N+1))//2)



# QUETION 11
# N=int(input())
# a=" "
# count=0
# for x in range(1,N+1):
#     if N%x==0:
#         a+=str(x)+" "
#         count+=1
# print(count,a)


# QUESTION 11
# N=int(input())
# i=1
# a=""
# count=0
# while N>=i:
#     if N%i==0:
#         a+=str(i)+" "
#         count+=1
#     i=i+1
# print(count,a)



# QUETION 12
# a,b,c=map(int,input().split())
# if (a+b)>c and (b+c)>a and (c+a)>b:
#     if a==b and b==c:
#         print("1")
#     elif a!=b and b!=c and c!=a:
#         print("3")
#     else:
#         print("2")
# else:
#     print("-1")


# string="Nagen  dra Yadav"
# print(string.replace(" ",""))
# print("".join(string.split()))
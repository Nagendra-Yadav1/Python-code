#printing the god singn
# for x in range(9):
#     for y in range(9):
#         if ((x==0) and (y<5)) or y==4 or ((x==8) and y>4):
#             print("*  ",end="")
#         elif (y==8 and x<5) or x==4 or ((y==0) and x>4):
#             print("*  ",end="")
#         elif ((x==2 or x==6) and (y==2)) or ((x==6 or x==2) and (y==6)):
#             print("*  ",end="")
#         else:
#             print("   ",end="")
#     print("")



# harshal number 
# n=int(input("enter the vallue of the number>>>>......"))
# sum=0
# Number=n
# while n>=1:
#     rev=n%10
#     sum+=rev
#     n//=10
# if Number%sum==0:
#     print(Number,"=harshal number")
# else:
#     print("not harshal number")




# perfect number 
# n=int(input("enter the value of the number>>>......."))
# sum=0
# for x in range(1,n):
#     if n%x==0:
#         sum=sum+x
# if n==sum:
#     print(n,"=perfect number")
# else:
#     print(n,"=not a perfect number")




# strong number
# n=int(input("enter the value of the number>>>....."))
# m=n
# sum=0
# while n>=1:
#     rev=n%10
#     fact=1
#     for x in range(1,rev+1):
#         fact*=x
#     sum=sum+fact
#     n//=10
# if m==sum:
#     print(m,"=This is the strong number")
# else:
#     print("Not strong number")




# spy number
# n=int(input("enter the value of the nu et>>......."))
# sum=0
# m=n
# product=1
# while n>=1:
#     rev=n%10
#     sum+=rev
#     product*=rev
#     n//=10
# if sum==product:
#     print(m,"=This is Spy number")
# else:
#     print(m,"=Not spy number")




# Neon number 
# n=int(input("enter the value of the numer>>....."))
# sum=0
# a=n*n
# m=a
# while a>=1:
#     rev=a%10
#     sum=sum+rev
#     a//=10
# if n==sum:
#     print(n,"=Neon number")
# else:
#     print(n,"=Not Neon number")


# sunny number
# n=int(input("enter the value of the number>>........"))
# a=n+1
# if (a**.5)==int(a**.5):
#     print("sunny Number")
# else:
#     print("Not sunny Number")



# armstrong number
# n=int(input("enter the value of the number>>......"))
# a=n
# sum=0
# while n>=1:
#     m=n%10
#     sum=sum+m**3
#     n//=10
# if a==sum:
#     print("ARMSTRONG NUMBER")
# else:
#     print("NOT ARMSTRONG NUMBER")
    



# PALIDROM NUMBER
# n=int(input("enter the value of the number>>......"))
# rev=0
# m=n
# while n>=1:
#     rev=rev*10+n%10
#     n//=10
# if m==rev:
#     print("PALIDROM NUMBER")
# else:
#     print("PALIDROM NUMBER")




# PRNIC NUMBER
# n=int(input("enter the value of the number>>>>>>........"))
# for x in range(n+1):
#     flag=0
#     if x*(x+1)==n:
#         flag=1
#         break
# if flag==1:
#     print("pr`onic number")




# dISARIUM NUMBER IN PYTHON
# n=int(input("enter the value of the number>>....."))
# count=0
# sum=0
# Number=n
# m=n
# r=n
# while r>=1:
#     r//=10
#     count+=1
# while m>=1:
#     k=m%10  
#     sum=sum+k**count
#     count=count-1
#     m//=10
# if Number==sum:
#     print(Number,"=DISARIUM NUMBER")
# else:
#     print(Number,"=NOT DISARIUM NUMBER")




# PRINTING SANGAMPUR
# for x in range(7):
#     for y in range(71):
        # if (x==0  and (y>0 and y<7)) or ((y==0) and (x>0 and x<3)) or  (y==6 and (x>3 and x<6)) or ((x==3) and (y>0 and y<6)) or (x==6 and y<6):
        #     print("*",end="") 
        # elif ((y==8 or y==14) and x>0 ) or ((x==0 or x==3) and (y>8 and y<14)):
        #     print("*",end="")
#         elif y==16 or y==22 or (x==1 and y==17) or (x==2 and y==18) or (x==3 and y==19) or (x==4 and y==20) or (x==5 and y==21):
#             print("*",end="")
#         elif  (y==24 and (x>0 and x<6 )) or ((x==0 or x==6) and (y>24 and y<30)) or ((y==30) and (x>2)) or ((x==3) and (y>27 and y<31)):
#             print("*",end="")
#         elif ((y==32 or y==38) and x>0 ) or ((x==0 or x==3) and (y>32 and y<38)):
#             print("*",end="")
#         elif y==40 or y==46 or ((x==1) and (y==41 or y==45)) or ((x==2) and (y==42 or y==44)) or (x==3 and y==43):
#             print("*",end="")
#         elif (y==48 and x>0 ) or ((x==0 or x==3) and (y>48 and y<54)) or ((y==54) and (x>0 and x<3))  :
#             print("*",end="") 
#         elif ((y==56 or y==62) and x<6) or ((x==6) and (y>56 and y<62)):
#             print("*",end="") 
#         elif (y==64 and x>0) or ((x==0 or x==3) and (y>64 and y<70)) or ((y==70) and ((x>0 and x<3) or (x>3))):
#             print("*",end="")     
#         else:
#             print(" ",end="")
#     print("")



# printing SANA
# for x in range(7):
#     for y in range(30):
#         if (x==0  and (y>0 and y<7)) or ((y==0) and (x>0 and x<3)) or  (y==6 and (x>3 and x<6)) or ((x==3) and (y>0 and y<6)) or (x==6 and y<6):
#             print("*",end=" ") 
#         elif ((y==8 or y==14) and x>0 ) or ((x==0 or x==3) and (y>8 and y<14)):
#             print("*",end=" ")
#         elif y==16 or y==22 or (x==1 and y==17) or (x==2 and y==18) or (x==3 and y==19) or (x==4 and y==20) or (x==5 and y==21):
#             print("*",end=" ")
#         elif ((y==24 or y==29) and x>0) or ((x==0 or x==3) and (y>24 and y<29)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")
    




# printing EHTESHAM
# for x in range(7):           
#     for y in range(63):
#         if ((x==0 or x==3 or x==6) and (y>=0 and y<7) or (y==0 and (x>0 and x<7)) ):
#             print("*",end=" ")
#         elif (y==8 or y==14) and(x>=0 and x<7) or (x==3 and (y>7 and y<15)):
#             print("*",end=" ")
#         elif(x==0) and (y>15 and y<23) or (y==19 and (x>=0 and x<7)):
#             print("*",end=" ")
#         elif((x==0 or x==3 or x==6) and (y>23 and y<31)) or (y==24 and (x>=0 and x<7)) :
#             print("*",end=" ")
#         elif (x==0  and (y>32 and y<39)) or ((y==32) and (x>0 and x<3)) or  (y==38 and (x>3 and x<6)) or ((x==3) and (y>32 and y<38)) or (x==6 and (y>31 and y<38)):
#             print("*",end=" ") 
#         elif(y==40 or y==46) and (x>=0) or (x==3 and (y>40 and y<47)):
#             print("*",end=" ")
#         elif ((y==48 or y==54) and x>0 ) or ((x==0 or x==3) and (y>48 and y<54)):
#             print("*",end=" ")
#         elif y==56 or y==62 or ((x==1) and (y==57 or y==61)) or ((x==2) and (y==58 or y==60)) or (x==3 and y==59):
#             print("*",end=" ")
        
#         else:
#             print(" ",end=" ")
#     print(" ")





# n=int(input("enter the value of the number>>>......"))
# i=1
# v=2
# m=1
# while (i or v or m)<=n:
#     print(i,v,m)
#     i=i+2
#     v=v+2
#     m=m+1




# Perfect number
# n=int(input("enter the value of the number>>>....."))
# sum=0
# m=n
# i=1
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==m:
#     print("perfect number")
# else:
#     print("not perfect number")



# Automarphic Number 
# n=int(input("enter the value of the number>>>>......."))
# a=n*n
# b=str(a)
# m=str(n)
# if m in b:
#     print(n,"=Automarphic Number")
# else:
#     print(n,"=Not Automarphic Number")





# LUCAS SPIRAL NUMBER
# x=0
# y=1
# z=0
# n=int(input("enter the value of the number>>>>......"))
# i=1
# while i<=n:
#     print(z,end=" ")
#     x=y
#     y=z
#     z=(x+y)
#     i=i+1
 
 



# PRIME COMPOSITE
# n=int(input("enter the value of the number>>>>>>......."))
# i=2
# while i<=n:
#     a=0
#     for x in range(2,i):
#         if i%x==0:
#             a=1
#             break   
#     if a==0:
#         if n%i==0:
#             print(i)
#     i=i+1
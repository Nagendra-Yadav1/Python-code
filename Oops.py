# make simple class
# class yadavji:
#     def sonu(self):
#         print(n)
#     def ramu(self):
#         print(m)
# n=input("Enter the sonu's behavior :-")
# m=input("Enter the ramu's behaviour :-")
# print("\n")
# nagendra=yadavji()
# nagendra.sonu()
# nagendra.ramu()



# making the class of the phone
# class phone:
#     def set_color(self):
#         print(color)
#     def set_cost(self):
#         print(cost)
#     def make_call(self):
#         print("making p a call")
#     def play_game(self):
#         print("playing  a game")
# color=input("Enter the name of the color :-")
# cost=int(input('Enter the cost of the color :-'))
# print("\n")
# p2=phone()
# p2.set_color()
# p2.set_cost()
# p2.make_call()
# p2.play_game()


# use the inti function
# class nagendra:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def show_nagendra_details(self):
#         print("Name of the user :-",self.name)
#         print("Age of the user  :-",self.age)
#         print("Salary of the user:-",self.salary)
# Name=input("Enter your name :-")
# age=int(input("Enter your age :-"))
# salary=int(input("Enter your salary :-"))
# print("\n")
# yadav=nagendra(Name,age,salary)
# yadav.show_nagendra_details()
# print("\n")


# parents and child class
# class vehicle:
#     def __init__(self,mileage,cost,model):
#         self.mileage=mileage
#         self.cost=cost
#         self.model=model
#     def details(self):
#         print("Mileage of the vehicle is :-",self.mileage)
#         print("cost of the vehicle is :-",self.cost)
#         print("Model of the vehicle is :-",self.model)
# mileage=int(input("Enter the mileage of th vehicle :-"))
# cost=int(input("Enter the cost of the vehicle :-"))
# model=int(input("Enter the model of the vehicle :-"))
# print("")
# v1=vehicle(mileage,cost,model)
# v1.details()
# class car(vehicle):
#     def details(self):
#         print("Mileagee of the car",self.mileage)
#         print("Cost of the car is",self.cost)
#         print("Model of the car is",self.model)
#         print("I am a car")
# c1=car(2000,4000,2018)
# c1.details()


# class vehicle:
#     def __init__(self,mileage,cost):
#         self.mileage=mileage
#         self.cost=cost
#     def details(self):
#         print("The mileage of the vehicle :- ",self.mileage)
#         print("The cost of the vehicle :-",self.cost)
# print()
# mileage=int(input("Enter the mileage of the vehicle :-"))
# cost=int(input("Enter the cost of the vehicle is :-"))
# v1=vehicle(mileage,cost)
# v1.details()


# class nagendra():
#     def __init__(self):
#         print("I am living in sangampur")
#     def yadav(self,x,y):
#         print(x+y)
# a=int(input("Enter the first vakue of the number :->"))
# b=int(input("Enter the value of the second number :->"))
# a1=nagendra()
# a1.yadav(a,b)


# simple inheritence
# class nagendra():
#     def sangampur(self):
#         print('I ma going to lucknow')
# class yadav(nagendra):
#     def sanjay(self):
#         print("I am going to sangampur")
# a1=yadav()
# a1.sangampur()
# a1.sanjay()


# Multilevel inheritence
# class A():
#     def x(self,m):
#         print(m)
# class B(A):
#     def y(self,n):
#         print(n)
# class C(B):
#     def z(self,o):
#         print(o)
# m=int(input("Enter the value of the first class :->"))
# n=int(input("Enter the value of the second class :->"))
# o=int(input("Enter the value of the thord class :->"))
# a=C()
# a.x(m)
# a.y(n)
# a.z(o) 





# Multiple inheritence
# class A():
#     def x(self,m):
#         print(m)
# class B():
#     def y(self,n):
#         print(n)
# class C(A,B):
#     def z(self,o):
#         print(o)
# m=input("Enter the value of the first class :->")
# n=input("Enter the value of the second class :->")
# o=input("Enter the value of the thord class :->")
# a=C()
# a.x(m)
# a.y(n)
# a.z(o) 


# Getter and setter method in class and object
# class student():
#     def __init__(self):
#         self.__name=""
#     def getname(self):
#         return self.__name
#     def setname(self,name):
#         self.__name=name
# obj=student()
# obj.setname("Testing")
# name=obj.getname()
# print(name)


# Encapsulation
# class student:
#     __name="Ravi"
#     def __init__(self):
#         print(self.__name)
#         self.__displayinfo()
#     def __displayinfo(self):
#         print("Welcome to Nagendra Yadav")
# obj=student()


# Polymorphism
# l=[10,20,30,40]
# print(len(l))
# s="Nagendra"
# print(len(s))


# function overloding
# class yadav():
#     def displayinfo(self,name=""):
#         print("Welcome to Nagendra Yadav"+name)
# obj=yadav()
# obj.displayinfo()
# obj.displayinfo(" in sangampur")



# function overiding
# class yadav():
#     def nagendra(self):
#         print("I am living in Sangampur")
# class IIp(yadav):
#     def nagendra(self):
#         super().nagendra()
#         print("My name is Nagendra Yadav")
# obj=IIp()
# obj.nagendra()


# # project of the bike
# class bikeshop():
#     def __init__(self,total):
#         self.total=total
#     def displaystock(self):
#         print("Total bike of the workshop :->",self.total)
#         print("")
#     def rentbike(self,q):
#         if q<=0:
#             print(" Choose postive option")
#         elif q>100:
#             print("Choose the quantity less than 100")
#             print("")
#         else:
#             print("Total prices  bike :->",q*self.total)
#             print("Total available stock  :-> ",self.total-q)
#             print("")
# obj=bikeshop(100)
# print("1 -> Display Stocks\n2 -> Rent Bike\n3 -> Exit")
# while True:
#     n=int(input('Choose Your Option :->'))
#     if n==1:
#         obj.displaystock()
#     elif n==2:
#         m=int(input("Enter the number of the bike :->"))
#         obj.rentbike(m)
#     elif n==3:
#         break
#     else:
#         print("Chose corect option")


# create Atm in the class and object
# class ATM:
#     def __init__(self,p,b):   
#          self.pin=p
#          self.balance=b
#     def create_pin(self,a):
#          self.pin=a
#          print("Insert Pin Successfully")
#     def deposit(self,a):
#         if a==self.pin:
#             amount=int(input("Enter the amount :-"))
#             self.balance=self.balance+amount
#             print("Deposite successful")
#         else:
#             print("Invalid Pin")
#     def withdraw(self,a):
#         if a==self.pin:
#             amount=int(input("Enter the amount :-"))
#             if amount<=self.balance:
#                 self.balance=self.balance-amount
#                 print("Operation successful")
#             else:
#                 print("Insufficient funds")
#         else:
#             print("Invalid Pin")
#     def check_balance(self,a):
#         if a==self.pin:
#             print("Your amount :->",self.balance)
#         else:
#             print("Invalid Pin")
# obj=ATM(1234,20000)
# print("""
#                     Hello,how would like to proceed
#                     1 :-> Enter 1 to change pin
#                     2 :-> Enter 2 to deposite
#                     3 :-> Enter 3 to withdraw
#                     4 :-> Enter 4 to check balance
#                     5 :-> Enter 5 to exit
#                     """)
# while True:
#     n=input("Choose Your Option :->")
#     if n=="1":
#            a=int(input("Enter your pin :->"))
#            obj.create_pin(a)
#     if n=="2":
#             a=int(input("Enter your pin :->"))
#             obj.deposit(a)
#     elif n=="3":
#             a=int(input("Enter your pin :->"))
#             obj.withdraw(a)
#     elif n=="4":
#             a=int(input("Enter your pin :->"))
#             obj.check_balance(a)
#     elif n=="5":
#          print("Exit")
#          break


# class fraction:
#     def __init__(self,m,n):
#         self.a=m
#         self.b=n
#     def __str__(self): 
#         return "{}/{}".format(self.a,self.b)
#     def __add__(self,other):
#         x=self.a*other.b+other.a*self.b
#         y=self.b*other.b
#         return "{}/{}".format(x,y)
#     def __sub__(self,other):
#         x=self.a*other.b-other.a*self.b
#         y=self.b*other.b
#         return "{}/{}".format(x,y)
#     def __mul__(self,other):
#         x=self.a*other.a
#         y=self.b*other.b
#         return "{}/{}".format(x,y)
#     def __truediv__(self,other):
#         x=self.a*other.b
#         y=self.b*other.a
#         return "{}/{}".format(x,y)
# a=int(input("Enter the first number :->"))
# b=int(input("Enter the first number :->"))
# c=int(input("Enter the first number :->"))
# d=int(input("Enter the first number :->"))
# x=fraction(a,b)
# y=fraction(c,d)
# print("                      First Fraction is :->",a,"/",b)
# print("                      Second Fraction is :->",c,"/",d)
# while True:
#     print("""                      Operation of the fraction
#                                 1 :-> Add
#                                 2 :-> Substract
#                                 3 :-> Multiply
#                                 4 :-> Divid
#                                 5 :-> Exit
#           """)
#     n=input("Choos Your Option :-")
#     if n=="1":
#         print(x+y)
#     elif n=="2":
#         print(x-y)
#     elif n=="3":
#         print(x*y)
#     elif n=="4":
#         print(x/y)
#     elif n=="5":
#         print("Exit")
#         break
#     else:
#         print("Choose the correct option")


# class Customer:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
# def greet(customer):
#     if customer.gender=="Male":
#         print("Hello",customer.name,"sir")
#     else:
#         print("Hello",customer.name,"ma'am")
#     cust2=Customer("Sanjeev","Male")
#     return cust2
# cust=Customer("Sonam","Female")
# print(cust.name)
# new_cust=greet(cust)
# print(new_cust.gender)


# class Customer:
#     def __init__(self,name):
#         self.name=name
# def greet(customer):
#     print(id(customer))
#     customer.name="Nagendra"
#     print(customer.name)
#     print(id(customer))
# cust=Customer("Sanjeev")
# greet(cust)
# print(id(cust))
# print(cust.name)

# def change(L):
#     print(id(L))
#     L.append(5)
#     print(id(L))
# l1=[1,2,3,4]
# print(id(l1))
# print(l1)
# change(l1)
# print(l1)


# def change(L):
#     print(id(L))
#     L=L+(5,6)
#     print(id(L))
# l1=(1,2,3,4)
# print(id(l1))
# print(l1)
# change(l1)
# print(l1)


# class customer:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def intro(self):
#         print("I am",self.name,"and I am",self.age)
# c1=customer("Nagendra",34)
# c2=customer("Nagendra",45)
# c3=customer("Nagendra",32)
# L=[c1,c2,c3]
# for i in L:
#     print(i.intro())


# class Customer:
#     def __init__(self,name,gender,address):
#         self.name=name
#         self.gender=gender
#         self.address=address
#     def edit_profile(self,new_name,new_city,new_pin,new_state):
#         self.name=new_name
#         self.address.change_address(self,new_city,new_pin,new_state)
# class Address:
#     def __init__(self,city,pincode,state):
#         self.city=city
#         self.pincode=pincode
#         self.state=state
#     def change_address(self,new_name,new_city,new_pin,new_state):
#         self.new_name=new_name
#         self.city=new_city
#         self.pincode=new_pin
#         self.state=new_state

# add=Address("Kolkata",700156,"WB")
# cust=Customer("Nagendrs","Male",add)
# cust.edit_profile("Sanjeev","Gurgaon",122011,"haryana")
# print(cust.address.city)
# print(cust.address.pincode)


# Abstraction
# from abc import ABC,abstractmethod
# class BankAPP(ABC):
#     def database(self):
#         print("Connected to database")
#     @abstractmethod
#     def secuirty(self):
#         pass
#     @abstractmethod
#     def secuirty(self):
#         pass

# class MobileApp(BankAPP):
#     def mobile_login(self):
#         print("Login into mobile")
#     def secuirty(self):
#         print("mobile secuirty")
#     def display(self):
#         print("display in the method")

# mob=MobileApp()
# mob.secuirty()
# mob.display()


#max of the three number
# class room:
#     def student(self,a,b,c,max,smax):
#         if a>b:
#             max=a
#             smax=b
#         if b>a:
#             max=b
#             smax=a
#         if max>c:
#             if smax>c:
#                 smax=smax
#             else:
#                 smax=c
#         else:
#             max=c
#             smax=max
#         return max
# a=int(input("Enter the first value of the number :->"))
# b=int(input("Enter the second value of the number :->"))
# c=int(input("Enter the third value of the number :->"))
# obj=room()
# result=obj.student(a,b,c,max=0,smax=0)
# print(result)


# check prime number]
# class prime():
#     def __init__(self,n):
#         self.n=n
#         count=0
#         for i in range(1,self.n+1):
#             if (self.n)%i==0:
#                 count+=1
#         if count==2:
#             print("Prime Number")
#         else:
#             print("Not prime number")
# n=int(input("Enter the value of the number :->"))
# obj=prime(n)


# class prime():
#     def Prime_number(self,n):
#         count=0
#         for i in range(1,n+1):
#             if (n)%i==0:
#                 count+=1
#         if count==2:
#             print("Prime Number")
#         else:
#             print("Not prime number")
# n=int(input("Enter the value of the number :->"))
# obj=prime()
# obj.Prime_number(n)


# class reverse():
#     def __init__(self,n):
#         self.n=n
#         b=self.n
#         c=self.n
#         rev=0
#         while c>0:
#             rev=rev*10+(c%10)
#             c//=10
#         if rev==b:
#             print("it is pllindrome")
#         else:
#             print("it is not pallindrome")
# n=int(input("enter the number>>"))
# obj=reverse(n)

# class reverse():
#     def pallindrome(self,n):
#         c=n
        
#         rev=0
#         while c>0:
#             rev=rev*10+(c%10)
#             c//=10
#         if rev==n:
#             return rev,True
#         else:
#             return rev,False
            
# n=int(input("enter the number>>"))
# obj=reverse()
# d=obj.pallindrome(n)
# print(d)



#check palidrom
# class Solution:
#     def isPalindrome(self, x):
#         rev=0
#         m=x
#         while(x>0):
#             rev=rev*10+(x%10)
#             x//=10
#         if rev==m:
#             return True
#         else:
#             return False
# n=int(input("Enter the number to checl Palidrom :->"))
# obj=Solution()
# palidrom=obj.isPalindrome(n)
# print(palidrom)



# Find the Gcd
# class Solution:
#     def GCD(self,array):
#         mi=min(array)
#         ma=max(array)
#         lcd=1
#         while True:
#             if (ma*lcd)%mi==0:
#                 lcd*=ma
#                 break
#             lcd+=1
#         return (ma*mi)//lcd
# arr=[]
# size=int(input("Enter the size of the array :->"))
# for i in range(size):
#     k=int(input("Enter the value of the list :->"))
#     arr.append(k)
# obj=Solution()
# gcd=obj.GCD(arr)
# print(gcd)


















































        

    







        









    





    





    



    


# with open("sample.txt","w") as f:
#     f.write("Hello world")

# try:
#     with open("sample1.txt","r") as f:
#         print(f.read())
# except:
#     print("sorry file not found")

# try:
#     f=open("sample.txt","r")
#     print(f.read())
#     print(m)
#     print(5/0)
#     l=[1,2,3,4,]
#     l[100]
# except FileNotFoundError:
#     print("File not found error")
# except NameError:
#     print("Variable not found")
# except ZeroDivisionError:
#     print("Can't divide by Zero")
# except Exception as e:
#     print(e)


# try:
#     f=open("sample1.txt",'r')
# except FileNotFoundError:
#     print("File nahi hai")
# except Exception:
#     print("Kuchh to lafra hai")
# else:
#     print(f.read())
# finally:
#     print("Ye to print hoga hi")



# RAISE Exceptin
# raise ModuleNotFoundError("Yese hi try kar raha hu")

# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount<0:
#             raise Exception("amount cannot be -ve")
#         if self.balance<amount:
#             raise Exception("Paise nahi hai tere pass")
#         self.balance=self.balance-amount

# obj=Bank(10000)
# try:
#     obj.withdraw(120000)
# except Exception as e:
#     print(e)
# else:
#     print(obj.balance)



# creating custom exception
# class MyException(Exception):
#     def __init__(self,message):
#         print(message)
# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount<0:
#             raise MyException("amount cannot be -ve")
#         if self.balance<amount:
#             raise MyException("Paise nahi hai tere pass")
#         self.balance=self.balance-amount

# obj=Bank(10000)
# try:
#     obj.withdraw(120000)
# except MyException as e:
#     pass
# else:
#     print(obj.balance)


# class SecurityError(Exception):
#     def __init__(self,message):
#         print(message)
#     def logout(self):
#         print("Logout")
# class Google:
#     def __init__(self,name,email,password,device):
#         self.name=name
#         self.email=email
#         self.password=password
#         self.device=device

#     def login(self,email,password,device):
#         if device !=self.device:
#             raise SecurityError("Teri to lag gayi")
#         if email==self.email and password==self.password:
#             print("Welcome")
#         else:
#             print("Login error")

# obj=Google("Nagendra Yadav","Nagendra22@navgurukul.org",1234,"android")
# try:
#     obj.login("Nagendra22@navgurukul.org",1234,"windows")
# except SecurityError as e:
#     e.logout()
# else:
#     print(obj.name)
# finally:
#     print("database connection closed")




# size=int(input("Enter th size of the list :->"))
# a=[]
# b=[]
# for i in range(size):
#     value=int(input("Enter the value of the list :->"))
#     a.append(value)
# k=int(input("Give the value :->"))
# for i in range(size-1,k-1,-1):
#     b.append(a[i])
# b.reverse()
# for i in range(k):
#     b.append(a[i])
# print(b)

























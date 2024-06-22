# f=open("myfile.txt","w")
# f.write("My name is nagendra Yadav.currently I am living in the Dharamshala")
# f.close()

# f=open("myfile.txt","a")
# f.write("\n I am fine")
# f.close()

# L=["Hello\n","how are you\n","I am fine"]
# f=open("myfile.txt","w")
# f.writelines(L)
# f.close()


# f=open("myfile.txt",'r')
# s=f.read(10)
# print(s)
# f.close()

# f=open("myfile.txt","r")
# print(f.readline())
# print(f.readline(),end="")
# f.close


# f=open("myfile.txt","r")
# while True:
#     data=f.readline()
#     if data==" ":
#         break
#     else:
#         print(data,end="")
# f.close()


# with open("myfile.txt","w") as f:
#     f.write("selman bhai")
# f.write("hello world")

# with open("Myfile.txt") as f:
#     print(f.read())

# with open("myfile.txt","r") as f:
#     print(f.read(20))
#     print(f.tell())
#     f.seek(11)
#     print(f.read(10))

# big_L=["hello world" for i in range(1000)]
# with open("big.txt",'w') as f:
#     f.writelines(big_L)

# with open("big.txt","r") as f:
#     chunk_size=10
#     while len(f.read(chunk_size)) >0:
#         print(f.read(chunk_size),end="***")
#         f.read(chunk_size)


# with open("myfile.txt","w") as f:
#     f.write("hello")
#     f.seek(0)
#     f.write("Xamp")


# serialization and deserialization
# import json
# l=[1,2,3,4,5,6]
# with open("demo.json",'w') as f:
#     json.dump(l,f)

# import json
# d={
#     'name':"nagendra",
#     "age":33,
#     "gender":"male"
# }

# with open("demo.json","w") as f:
#     json.dump(d,f,indent=4)


# import json
# d={
#     'name':"nagendra",
#     "age":33,
#     "gender":"male"
# }
# with open("demo.json","r") as f:
#     d=json.load(f)
#     print(d)

# import json
# t=(1,2,3,4)
# with open("demo.json","w") as f:
#     json.dump(t,f)

# import json
# d={
#     'name':"nagendra",
#     "marks":[12,13,1566,65],
#     "age":33,
#     "gender":"male"
# }
# with open("demo.json",'r') as f:
#     d=json.load(f)
#     print(d)

# class Person:
#     def __init__(self,fname,lname,age,gender):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#         self.gender=gender

# import json
# def show_object(person):
#     if isinstance(person,Person):
#         return "{} {} age -> {} gender ->{}".format(person.fname,person.lname,person.age,person.gender)
# with open("demo.json","w") as f:
#     json.dump(Person,f,default=show_object)



# import json
# def load_data():
#     try:
#         with open("data.json", "r") as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = {}
#     return data

# def save_data(data):
#     with open("data.json", "w") as file:
#         json.dump(data, file, indent=4)


# main_dict = load_data()
# print("Welcome To Crud Operation")

# while True:
#     print("1: Create\n2: Read\n3: Update\n4: Delete\n5: Break")
#     choose = int(input("Choose Your option: "))
    
#     if choose == 1:
#         name = input("Enter Your name: ")
#         email = input("Enter your Email: ")
#         mobile = input("Enter your mobile: ")
#         password = input("Enter Your strong password: ")
        
#         if (
#             (".com" in email or ".org" in email)
#             and "@" in email
#             and len(mobile) == 10
#             and mobile.isdigit()
#             and len(password) == 8
#             and any(char.isupper() for char in password)
#             and any(char.islower() for char in password)
#             and any(char.isdigit() for char in password)
#             and any(char in "~!@#$%^&*_" for char in password)
#         ):
#             main_dict[mobile] = {"name": name, "Email": email, "Password": password}
#             save_data(main_dict)  
#             print("Record created successfully")
#         else:
#             print("Invalid input, record not created")

#     elif choose == 2:
#         phone = input("Enter Your phone Number: ")
#         if phone in main_dict:
#             print(main_dict[phone])
#         else:
#             print("Record not found")

#     elif choose == 3:
#         print("Update Your account")
#         print("1: Name\n2: Email\n3: Password\n4: Mobile")
#         choose1 = int(input("Choose Your Option: "))
        
#         if choose1 == 1:
#             phone1 = input("Enter Your Phone number: ")
#             if phone1 in main_dict:
#                 new_name = input("Enter new name: ")
#                 main_dict[phone1]["name"] = new_name
#                 save_data(main_dict)  
#                 print("Name updated successfully")
#             else:
#                 print("Phone number is not found")

#     elif choose == 4:
#         phone1 = input("Enter Your Phone number: ")
#         if phone1 in main_dict:
#             del main_dict[phone1]
#             save_data(main_dict)  
#             print("Record deleted successfully")
#         else:
#             print("Phone number is not found")

#     elif choose == 5:
#         break

#     else:
#         print("Choose Correct Operation")




















































    
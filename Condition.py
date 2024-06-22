# a=int(input("enter the age>>>>....."))
# if a==18 and a<=100:
#     print("You can go to ARTO office to check up you can drive the bick")
# elif a>18 and a<=60:
#     print("You can drive the bick")
# else:
#     print ("you can not drive the bick")

# for x in range(1,11):
#     print("2 *",x ,"=", 2*x)


                          
# a=int(input("enter the number>>>..."))
# if a==1:
#     print("not a prime number:::")
# elif a==2:
#     print("this is a prime number:::")
# elif a==3:
#     print("this is a prime number:::")
# elif a%2==0 or a%3==0 or a%5==0 and a>3:
#     print("this is not a prime number")
# else:
#     print("this is a prime number")



# a=int(input("enter the number>>>>...."))
# if a==a:
#     print(a,"X 1","=",a*1)
#     print(a,"X 2","=",a*2)
#     print(a,"X 3","=",a*3)
#     print(a,"X 4","=",a*4)
#     print(a,"X 5","=",a*5)
#     print(a,"X 6","=",a*6)
#     print(a,"X 7","=",a*7)
#     print(a,"X 8","=",a*8)
#     print(a,"X 9","=",a*9)
#     print(a,"X 10","=",a*10)
# else: 
#     print("no table")




# a=int(input("enter the first number>>>>...."))
# b=int(input("enter the second number>>>....."))
# c=int(input("enter the third number>>>......"))
# max=0
# smax=0
# if(a>b):
#     max=a
#     smax=b
# if(b>a):
#     max=b
#     smax=a
# if(max>c):
#     if(smax>c):
#         smax=smax
#     else:
#         smax=c
# else:
#     smax=max
#     max=c
# print("Smax :-",smax)




# name=input("enter the character>>>>>...")
# b=len(name)
# c="ercnertyuins"
# d=len(c)
# if len(name)==len(c):
#     if (name[:3] in name and "_" in name) and(name[3:7] in name and 
#     "_" in name) and (name[6:11] in name ): 
#         print("valid")
#     else:
#         print("not valid")
# else:
#     print("not valid")




# amt=0
# num=int(input("enter the electricity unit"))
# if num<=100:
# 	amt=0
# if num>100 and num<=200:
# 	amt=(num-100)*5
# if num>200:
# 	amt=500+(num-200)*10
# print("Amount to pay :",amt)

# num=int(input("enter the value of number"))
# print("Last digit of number:" ,num%10)




#num=int(input("enter the value of number"))
#Last_Digit=num%10
#if Last_Digit%3==0:
#	print("last digit divisible by 3")
#else:
#	print("last digit not dividible by 3")




#a=input("enter the first value>>>>>>")
#b=input("enter the second value>>>>>")
 #print(str(int(a)//10).ljust(2)+" ".join(b))




#a=int(input("enter the side1>>>>"))
#b=int(input("enter the side2>>>"))
#c=int(input("enter thr side 3>>>"))
#if a+b>c or b+c>a or c+a>b:
#	print("valid triangle")
#else:
#	print("not valid trianglre")



# a=int(input("enter the current prize>>>"))
# b=int(input("enter the lost prize>>>>"))
# if a>b:
# 	print("profit")
# elif a==b:
# 	print("no profit no loss")
# else:
# 	print("loss")



# n=input("Enter the character>>>>...")
# if n and ( "ing" in n ):
#     print(n+"ly")
# elif ("ing" in n) and n:
#     print("ly"+n)
# else:
#     print(n+"ing")



#a= int(input("enter the marks>>>>>"))
#if a>90 and a<= 100 :
#	print("Grade A")
#else:
#	if a>80 and a<=90:
#		print("Grade B")
#	else:
#		if a>=60 and a<= 80:
#			print("Grade C")
#		else:
#			if a<60:
#				print("Grade D")
#			else:
#				print("percentage only 100 ke bee")



#tax=0
#per= int(input("enter the price of bike>>"))
#if per>100000:
#	tax=15/100*per
#elif per>50000 and per<=100000:
#	tax=10/100*per
#else:
#	tax=5/100*per
#print("tax to paid road",tax)




#year= int(input("enter the year>>>>"))
#if year%4==0 or year%100 and year%400:
#	print("year is leap year")
#else:
#	print("year is not leap year")




#a=int(input("enter the number is weak>>"))
#if a==1:
#	print("Sunday")
#else:
#	if a==2:
#		print("Monday")
#	else:
#       if a==3:
#			print("Tuesday")
#		else:
#			if a==4:
#				print("Wednesday")
#			else:
#               if a==5:
#					print("Thursday")
#				else:
#					if a==6:
#						print("Friday")
#					else:
#						if a==7:
#							print("Saturday")
#						else:
#							print("num of weak less 7")




#a=int(input("enter the month name>>>>>"))
#b=int(input("enter the year name>>>>>> "))
#if a==2 and b%4==0 or b%100==0 and b%400==0:
#			print("29 days")
#elif a==2:
#	print("28 days")
#elif a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
#					print("31 days")
#else:
#	print("30 days")


#if True:
#		print("101")
#else:
#	print("102")



#a=input("enter the city name>>>>>")
#if a=="Delhi":
#			print("Red Fort")
#elif a=="Aagra":
#					print("Taj Mahal")
#elif a=="Jaipur":
#					 print("Jal Mahal")
#else:
#	print("False")



#num1=int(input("enter any number>>>"))
#l=len(num1)
#if l !=3:
#	print("enter three digit number")
#else:
#	print("Middle digit is",(int(num1)%100//10))





#a=int(input("enter the total day of working day in the school>>>>>"))
#b=int(input("enter the day of absent in the school>>>>>"))
#per=(a-b)/a*100
#print(per,"%")
#if per<75:
#	print("not eligible for give the exam")
#else:
#	print("eligible for give the exam")




#bonus=0
#a=int(input("enter the year value"))
#if a>10:
#	bonus=10*a/100
#if a>=6 and a<=10:
#	bonus=8/100*a
#else:
#	bonus=5/100*a
#print("bonus of employer",bonus)



#a=int(input("enter the temperarure>>>>"))
#if a>=100:
#	print("boiling water")
#else:
#	print("no boiling water"))


#a="a","e","i","o","u"
#b="A","E","I","O","U"
#c=input("enter the alphabet>>>>...")
#if a==c or b==c:
#	print("vowel")
#else:
#	print("consonant")


#a=int(input("enter the first value>>>>.."))
#b=int(input("enter the second valuue"))
#c=a*b
#if c//b and c//a:
#	print(b,a)
#a=int(input("enter the number>>>..."))
#if a%2==0:
#	print(a,"is even number")
#else:
#	print(b,"odd number")




#a=input("enter the user name>>>...")	
#if (a>="a" and a<="z") or (a>="A" and a<="Z"):
#	print("user name>>>>:",a)
#	b=int(input("enter the password>>"))
#	if b>=0 or b<=934445667779987655566:
#		print("login")
#else:
#	print("user name not carrect")




#a=input("enter the character>>>>")

#a=int(input("enter the value>>>>..."))
#if a>=1:
#	print("positive")
#else:
#    print("negative")




#print("Fibonacci sequence")
#for i in range(10):
#	print(a,end=" ")
#	c=a+b
#	a=b
#	b=c.




#a= int(input("enter the number>>>.."))
#if a==1 :
#	print("not prime number")
#elif a==2:
#	print("prime number")
#elif  a%2==0 or a%3==0 or a%5==0 and a>3 :
#	print("not prime number")
#else:
#	print("prime number









# old_data={}

# import os
# import json

# # Specify the file path
# json_filename = "data.json"

# # Check if the file exists
# if os.path.isfile(json_filename):
#     # Open the JSON file for reading
#     with open(json_filename, "r") as json_file:
#         old_data = json.load(json_file)
    
#     # Now, old_data contains the data from the JSON file as a Python dictionary
#     print("Old Data:")
#     print(old_data)
# # else:
# #     print(f"The file '{json_filename}' does not exist.")



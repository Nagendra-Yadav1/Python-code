# for x in range(7):
# 		for y in range(6):
# 			if (y==0 and  (x>0 and x<6)) or (x==0 and y>1) or (x==6 and y>1):
# 				print("* ",end="")
# 			else:
# 				print(" ",end="")
# 		print("")


#for x in  range(7):
#		for y in range(5):
#			if (y==0 or y==4) or ((x==0 or x==6) and (y>0 and y<4)):
#				print("*",end=" ")
#			else:
#				print("    ",end="")
	#	print("")
	
	
#	
#for x in range(7):
#		for y in range(5):
#			if y==0 or (x==0 or x==3 or x==6)  or ((x==1 or x==2 or y==4 or x==5) and y==4):
#				print("*",end="")
#			else:
#				print("   ",end="")
#		print(" ")


#m=1
#for x in range(5):
#		for x in range(5):
#			print(m,end=" ")
#			if m=m+1:
#				print(m)
#		print(" ")
#	



#n=int(input("enter the value of the number>>>..."))
#sum=0
#i=1
#a=0
#count=1
#while count<=n:
#	if i%2==0:
#		sum=sum+i
#		count=count+1
#	else:
#		a=a+i
#	i=i+1
#print(a,sum)


#for x in range(7):
#	for y in range(5):
#		if y==0 or x==0 or x==6 or ((x==4 or x==5) and y==4) or (x==3 and y>=2):
#			print("*",end=" ")
#		else:
#			print("  ",end=" ")
#	print(" ")


#for x in range(7):
#   for y in range(5):
#   	if y==0 or y==4 or x==3:
#   		print("*",end=" ")
#   	else:
#   		print("   ",end="")
#   print(" ")


#for x in range(7):
#   	for y in range(8):
#   		if x==2 or x==4 or ((x==3) and (y==1 or y==7)) or ((x==0 or x==6) and y==4) or ((x==1 or x==5) and (y==3 or y==5)):
#   			print("* ",end=" ")
#   		else:
#   			print(" " ,end="  ")
#   	print(" ")

#n=int(input("enter the value of the nymber>>.."))
#while 



#m=1
#n=5
#N=int(input("enter the value of number>>.."))
#rev=0
#for x in range(N):
#	for y in range(N):
#		if x%2==0:
#			print(m,end=" ")
#		else:
#			rev=rev*10+y%10
#			print(m,end=" ")
#			y//=10
#		m=m+1
#	print(" ")


#n=int(input("enter the value of the number>>.."))
#sum=0
#rev=1
#while n>=1:
#	rev=n%10
#	sum+=(rev)**2
##	n//=10
#print(sum)


#n=int(input("enter the balue of the number>>.."))
#a=n+1
#if (a*.5)==int(a*.5):
#	print("yes")
#else:
#	print("no")

#a=int(input("enter the value of the number"))
#i=2
#while i<=a:
#		flag=0
#		for x in range(2,i):
#			if i%x==0:
#				flag=1
#				break
#		if flag==1:
#			print(i)
#		i=i+1



#a=input("enter the value of the number>>>>....").split()
#m=a.pop()
#b=" "
#for x in (a):
#	b+=str(x)+"  "
#print(m,b)




#n=[ ]
#a=int(input("enter the value of the number>>>>....."))
#for x in range(a):
#	m=int(input("enter the value od the number>>>>>>...."))
#	n.append(m)
#s=n
#for i in range(a):
#	 print(s[i],end="  ")



#list1 = [1,2,2,4,1, 2,5,3]
#list2 = list()
#l1 = [ ]
#i = 0
#while i < len(list1):
#    if list1[i] not in list2:
#        list2. append(list1[i])
#    i += 1
#j = 0 
#while j < len(list2):
#    list3 = list()
#    a = list1.count(list2[j])
#    if a > 1:
#        list3.append(a)
#        list3.append(list2[j])
#        l1.append(list3)
#    else :
#        l1.append(list2[j])
#    j += 1
#print (l1)


#b=[ ]
#a=[ ]
#size=int(input("Enter the size of list>>>.....:  :"))
#for x in range(size):
#		value=int(input("Enter the list elements>>>>>>>......::  ::"))
#		a.append(value)
#key=int(input("choose the list element>>>>.."))
#for i in range(size):
#	if a[i]==key:
#		print(a[i])
#	else:
#		b=a[i]
#print(b)


#a=1
#m=1
#n=int(input("Enter the value of the number>>>>>>....."))
#for i in range(2,n+1):
#	for x in range(1,i):
#		if i%2==0:
#		    print(m,end=" ")
#		else:
#			print(,end=" ")
#		m=m+1
#		a=m*
#	print




#a=int(input("Enter number>>>>"))
#i=1
#sum=0
#n=a
#while i<a:
#	if a%i==0:
#	    sum+=i
#	i=i+1
#if sum==n:
#		print("yes")
#else:
#	print("no")




#a=int(input("Enter the value of the nu>>>>"))
#sum=0
#n=a
#k=a
#count=0
#while a>0:
#    rem=a%10
#    count+=1
#    a//=10
#while(n>0):
#	sum=sum+(n%10)**count
#	n//=10
#print(sum)
#if sum==k:
#	print("armstrong")
#else:
#	print("not armstrong")



# sum=0
#n=int(input("enter the value of the number>."))
#for x in range(1,n+1,1):
#	if x%2==0:
#		sum=sum+x**2
#	else:
#		if x==1:
#		    sum=sum+x**2
#		else:
#			sum=sum-x**2
#print(sum)



#n=int(input("enter the  value of the number"))
#sum=0
#for x in range(1,n+1):
#			   sum=sum+x
#			   if sum==15 or  sum==20:
#			   	 print("20")

#L,R=map(int,input().split())
#for x in range(L,R):
#			if L==0:
#				break
#			else:
#				print(x)



#a="pyt"
#for x in range(len(a)+1):
#			for y in range(x):
#				print(a[y],end=" ")
#			print("")


#a="python"
#for x in range(len(a)+1):
#			for y in range(x):
#				print(a[y],end="  ")
#			print()


#for x in range(6):
#			for y in range(6-x):
#				print( "  *",end="")
#			for z in range(2*x-1):
#				print(z,end=" ")
#	…
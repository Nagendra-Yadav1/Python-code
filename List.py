# List=[ ]
# size_of_list=int(input("enter the value of the number>>>>>>......."))
# for x in range(size_of_list):
#     Number_of_list=int(input("enter the value of the number>>>>>>....."))
#     List.append(Number_of_list)
# m=List[0]
# print("list of=",List)
# for i in range(1,size_of_list):
#     List[i-1]=List[i]
# List[size_of_list-1]=m
# print("list of=",List)


# grocery_list=["flour","cheese","carrots"]
# a=len(grocery_list)
# for x in range(a):
#     print("#=>",x,":",grocery_list[x])


# a=[["g","f","g"],["i","s"],["b","e","s","t"]]
# b=a[0][0:]
# c=a[1][0:]
# d=a[2][0:]
# e=b+c+d
# for z in e:
#     print(z,end="")
# print("")


# c=[6,1,3,5,6,3,1]
# a=set(c)
# b=list(a)
# fact=1
# for i in b:
#     fact*=i
# print(fact)


# reverse a list
# list1=[100,200,300,400,500]
# list1.reverse()
# print(list1)

# a=[100,200,300,4000,500]
# print(a[::-1])


# add two list 
# list1=["m","na","i","ke"]
# list2=["y","me","s","lly"]
# print(list1+list2)
# a=[i+j for i,j in zip(list1,list2)]
# print(a)
# list1.extend(list2)
# print(list1)



# square of list
# a=[1,2,3,4,5,6,7]
# m=[]
# for x in a:
#     m.append(x*x)
# print(m)
# n=[i*i for i in a]
# print(n)



# concatenate two list
# a=[]
# list1=["Hello","Take"]
# list2=["Dear","Sir"]
# for x in list1:
#     for i in list2:
#         a=[x+i]
#         print(a,end="")
# m=[i+x for i in list1 for x in list2]
# print(m)


# list1=[10,20,30,40]
# list2=[100,200,300,400]
# for i,x in zip(list1,list2[::-1]):
#     print(i,x)


# len of the list
# a=[]
# size=int(input("Enter the size of the list>>>>>>>......"))
# for x in range(size):
#     value=int(input("Enter the value of the list>>>>>>>>>>......"))
#     a.append(value)
# print(len(a))


# max of the list
# a=[]
# size=int(input("Enter the size of the list>>>>>>>......"))
# for x in range(size):
#     value=int(input("Enter the value of the list>>>>>>>>>>......"))
#     a.append(value)
# print(min(a))


# max of the list
# a=[]
# size=int(input("Enter the size of the list>>>>>>>......"))
# for x in range(size):
#     value=int(input("Enter the value of the list>>>>>>>>>>......"))
#     a.append(value)
# print(max(a))


# append of the list
# a=[]
# size=int(input("Enter the size of the list>>>>>>>......"))
# for x in range(size):
#     value=int(input("Enter the value of the list>>>>>>>>>>......"))
#     a.append(value)
#     a.append("Nagendra")
# print(a)


# cmp in list
# a=[]
# size=int(input("Enter the size of the list>>>>>>>......"))
# for x in range(size):
#     value=input("Enter the value of the list>>>>>>>>>>......")
#     a.append(value)
# list1=a
# b=[]
# size=int(input("Enter the size of the list>>>>>>>......"))
# for x in range(size):
#     value=input("Enter the value of the list>>>>>>>>>>......")
#     b.append(value)
# list2=b
# k=[ i for i in zip(list1,list2)]
# print(k)


# count method in list
# a=[]
# size=int(input("Enter the size of the list>>>>>>>......"))
# for x in range(size):
#     value=int(input("Enter the value of the list>>>>>>>>>>......"))
#     a.append(value)
# m=any(a)
# print(m)


# sum of the number of the list
# a=[]
# size=int(input("Enter the size of the list>>>>>>>>......."))
# for x in range(size):
#     value=int(input("Enter the value of the size>>>>>>>......."))
#     a.append(value)
# sum=0
# for i in range(size):
#     sum=sum+a[i]
# print("sum of the value in list=",sum)


# count of even ad oddd
# a=[]
# size=int(input("Enter the size of the list>>>>>>>>......."))
# for x in range(size):
#     value=int(input("Enter the value of the size>>>>>>>......."))
#     a.append(value)
# even=0
# odd=0
# for i in range(size):
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print("even=",even,"odd=",odd)



# find the given number in list
# a=[]
# size=int(input("Enter the size of the list>>>>>>>>......."))
# for x in range(size):
#     value=int(input("Enter the value of the size>>>>>>>............."))
#     a.append(value)
# key=int(input("Search number in the list>>>>>>>>>>...... "))
# flag=0
# for i in range(size):
#     if key==a[i]:
#         flag=1
#         m=i+1
# if flag==1:
#     print("Number in present list=",m)



# input= [10,20,30,40,50,60,70,80]
# output=[30,40,50,60,70,80,10,20]
# a=[]
# size=int(input("Enter the size of list>>>>>>......."))
# for x in range(size):
#     value=int(input("Enter the element of the list>>>>>>>>>>>>>....."))
#     a.append(value)
# m=a[0]
# n=a[1]
# print("original list=",a)
# for i in range(2,size):
#     a[i-2]=a[i]
# # a[size-1]=n
# # a[size-2]=m
# print("sifting  list=",a)


# Element sifting
b=[]
a=[]
size=int(input("Enter the size of the list   :-"))
for x in range(size):
    value=int(input("Enter the value of the list  :-"))
    a.append(value)
print("original list    =",a)
n=int(input("choose the list element to sifting   :-"))
for i in range(n,size):
    b.append(a[i])
for m in range(n):
    b.append(a[m])
print("sifting list in n time=",b)


# store the armstrong number in the list
# N=int(input("Enter the valu of the number  :-"))
# a=[ ]
# i=1
# while i<=N:
#     j=i
#     m=i
#     count=0
#     while j>0:
#         rev=j%10
#         count+=1
#         j//=10
#     k=i
#     sum=0
#     while k>0:
#         rev=k%10
#         sum+=(rev**count)
#         k//=10
#     if sum==m:
#         a.append(sum)
#     i+=1
# print("Store the armstrong Number=",a)


# store the prime number in the list
# N=int(input("Enter the value of the number   :-"))
# a=[ ]
# i=1
# while i<=N:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         a.append(i)
#     i+=1
# print("Store the prime number=",a)


a=[]
size=int(input("Enter the size of the list   :-"))
for x in range(size):
    value=int(input("Enter the value of the list  -"))
    a.append(value)
print("original list    =",a)
i=0
while(i<size-1):
    j=i+1
    while j<size:
        if a[i]>a[j]:
            tem=a[i]
            a[i]=a[j]
            a[j]=tem
        j+=1
    i+=1
print("sorted array    =",a)
i=0
positive_arr=[]
lenP=0
lenN=0
negative_arr=[]
while i<size:
    if a[i]>0:
        positive_arr.append(a[i])
        lenP+=1
    else:
        negative_arr.append(a[i])
        lenN+=1
    i+=1
print("positive sorteed array  =",positive_arr)
print("Negative sorteed array  =",negative_arr)



# give the method of insert position
# a=[]
# size=int(input("Eter the size of the list  :- "))
# i=0
# while(i<size):
#     value=int(input("Enter the element of the list  :-"))
#     a.append(value)
#     i+=1
# print("Original list  ",a)
# key=int(input("ENter the value to insirt  :-"))
# pos=int(input("Give the position to enter the value  :-"))
# a.append(None)
# for i in range(size-1,pos-2,-1):
#     a[i+1]=a[i]
# a[pos-1]=key
# print("After inset list ",a)


# a=[2,4,7,0,5,8]
# b=[3,3,-1,7]
# c=len(a)
# d=len(b)
# i=0
# m=[]
# j=0
# while((i<c)and(j<d)):
#     if(i==j):
#         m.append(a[i]+b[j])
#     else:
#         m.append(a[i])
#     i+=1
#     j+=1
# print(m)


# list=[10,11,20,21,30,40,47,88,100,101,200,205]
# even=[]
# odd=[]
# for x in range(len(list)):
#     if list[x]%2==0:
#         even.append(list[x])
#         print(even)
#     else:
#         odd.append(list[x])
#         print(odd)


# list=[10,11,33,20,30,37,27,88,100,200,99,12,1]
# even=[]
# odd=[]
# for x in range(len(list)):
#     if list[x]%2==0:
#         even.append(list[x])
#     else:
#         odd.append(list[x])
# print("even number of list",even)
# print("odd number in list",odd)



# list=[10,11,20,21,30,40,47,88,100,101,200,205]
# even=[]
# odd=[]
# for x in range(len(list)):
#     if list[x]%2==0:
#         even.append(list[x])
#         print(even)
#     else:
#         odd.append(list[x])
#         print(odd)




# list=[10,11,33,20,30,37,27,88,100,200,99,12,1]
# even=[]
# odd=[]
# for x in range(len(list)):
#     if list[x]%2==0:
#         even.append(list[x])
#     else:
#         odd.append(list[x])
# print("even number of list",even)
# print("odd number in list",odd)


# find the mean and medium
# n=int(input("Enter the size of the list :-"))
# a=[]
# for i in range(n):
#     value=int(input("Enter the value of the list :-"))
#     a.append(value)
# print("Orginal list :-",a)
# k=0
# while k<n-1:
#     j=k+1
#     while j<n:
#         if a[k]>a[j]:
#             t=a[k]
#             a[k]=a[j]
#             a[j]=t
#         j+=1
#     k+=1
# print("Sorted array :-",a)
# sum=0
# i=0
# while i<n:
#     sum+=a[i]
#     i+=1
# if n%2==0:
#     medium=a[(n//2-1)]+a[(n//2+(1-1))]
#     print(medium/2)
# else:
#     medium=(n+1)//2
#     print(a[medium-1])
    
      



            









    













        



    
    

    
    






    
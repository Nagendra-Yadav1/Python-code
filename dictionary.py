# sor the dictionary in the python
# import operator
# dicti={100:'Nagendra',2:"Mohit",10:"Sarawan",4:"Ansh Gupta",6:"kamal"}
# a=sorted(dicti.items())
# print("Asending order to the dictionary  :->",dict(a))
# a.reverse()
# print("Desending order to the distionary  :->",dict(a))


#add the dictionary
# sample_dict={0:10,1:20}
# sample_dict.update({2:30})
# print(sample_dict)


# concate the dictionary
# m=[]
# n=[]
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# for i,j in (dic1.items(),dic2.items(),dic3.items()):
#     m.append(i)
#     m.append(j)
# print(dict(m))


# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# main_dict={}
# for i in (dic1,dic2,dic3):
#     main_dict.update(i)
# print(main_dict)


#key already exits
# d={1:10,2:20,3:30,4:40,5:50,6:60,7:70}
# Sample_key=int(input("Enter the key of the dictionary :->"))
# if Sample_key in d.keys():
#     print("Key is present in the dictionary")
# else:
#     print("Key is not present in the dictionary")



# main_dict={}
# while True:
#     print("1 :-> Input\n2 :->break")
#     choose=input("Choose your option :->")
#     if choose=="1":
#         key=input("Enter the key of the dictionar :->")
#         value=input("Enter the value of the dictionary :->")
#         main_dict.update({key:value})
#     elif choose=="2":
#         break
#     else:
#         print("choose correct option")
# print(main_dict)


# main_d={}
# n=int(input("Enter the value of the number :->"))
# for i in range(1,n+1):
#     main_d.update({i:i*i})
# print(main_d)


# a={"Name":"Nagendra","gender":"male","surname":"Yadav"}
# b={1:100,2:300,4:1000}
# main_dict=a.copy()
# main_dict.update(b)
# print(main_dict)

# a={"Name":"Nagendra","gender":"male","surname":"Yadav",1:100,2:300,4:1000}
# for i in a.items():
#     print(i)

# main={1:100,2:200,3:400,4:1000,5:500}
# print(sum(main.values()))

# main={1:100,2:200,3:400,4:1000,5:500}
# mult=1
# for i in main.values():
#     mult*=i
# print(mult)



# a={"Name":"Nagendra","gender":"male","surname":"Yadav",1:100,2:300,4:1000}
# del a[1]
# print(a)


# a=[1,2,3,4,5,6]
# b=["Nagendra","Hariom","Nasir","Sanjeev","Bhumesh","Tausif"]
# main_dict=dict(zip(a,b))
# print(main_dict)


# a={"Name":"Nagendra","gender":"male","surname":"Yadav",1:100,2:300,4:1000}
# for i in a:
#     print(i,a[i])

# a={1:100,2:200,3:300,4:400,5:500,6:600}
# print(min(a.keys()))


# class dict_obj:
#     def __init__(self):
#         self.name="Nagendra"
#         self.surname="Yadav"
#         self.gender="male"
# obj=dict_obj()
# print(obj.__dict__)



# student_data={1:{"name":"Nagendra yadav","Gender":"male","Class":"10th"},2:{"name":"Aniket Pandey","Gender":"male","class":"12th"},3:{"name":"Nagendra yadav","Gender":"male","Class":"10th"}}
# main_dict={}
# for i,j in student_data.items():
#     if j not in main_dict.values():
#         main_dict[i]=j
# print(main_dict)


# main_dict={"name":"Nagendra Yadav"}
# if bool(main_dict):
#     print("Dictionary is not empty")
# else:
#     print("Dictionary is empty")


# from collections import Counter
# a={1:100,2:200,3:300,4:400,5:600}
# b={"a":1100,"b":1200,"c":400}
# c=Counter(a)+Counter(b)
# print(c)

# Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# a=[]
# for i in Sample_Data:
#     for j in i.values():
#         a.append(j)
# print(set(a))


# a=[]
# dict_main={"1":["a","b"],"2":["c","d"]}
# for i in dict_main.values():
#     for j in i:
#         a.append(j)
# for m in range(2):
#     for k in range(2,len(a)):
#         print(a[m],a[k])


# a={10:100,1:2000,3:30,4:5000}
# from heapq import nlargest
# Largest=nlargest(3,a,key=a.get)
# print(Largest)



# main_data=[{"a":"b","sum":1200},{"a":"c","sum":1200},{"a":"b","sum":1200}]
# from collections import Counter
# result=Counter()
# for i in main_data:
#     result[i["a"]]+=i["sum"]
# print(result)


# string="w3resource"
# result=[]
# comb=[]
# for i in string:
#     if i not in result:
#         result.append(i)
#         m=string.count(i)
#         comb.append(m)
# c=dict(zip(result,comb))
# print(c)


# main_dict=[{"id":2000,"name":"Nasir","Success":True},{"id":10,"name":"Aniket","Success":False},{"id":100,"name":"Nagendra Yadav","Success":True}]
# print(sum(i["id"] for i in main_dict))
# print(sum(i["Success"] for i in main_dict))


# a=[1,2,3,4,5]
# b=main_dict={}
# for i in a:
#     main_dict[i]={}
#     main_dict=main_dict[i]
# print(b)


# List=[1,2,3,4,5,6,7,8]
# main_dictionary=main_dict={}
# for i in List:
#     main_dict.update({i:{}})
#     main_dict=main_dict[i]
# print(main_dictionar


# main_dict={"a1":[3,2,1],"a2":[6,5,4],"a3":[9,8,6]}
# for i in main_dict:
#     main_dict.update({i:sorted(main_dict[i])})
# print(main_dict)


# main_dict={"s 001":["math","science"],"s 002":["math","English"]}
# a={}
# for i in main_dict:
#     a.update({i.replace(" ",""):main_dict[i]})
# print(a)


# main_dict={"a":45.45,"b":50,"c":80,"d":200,"e":500,"f":5}
# from heapq import nlargest
# m=nlargest(3,main_dict,key=main_dict.get)
# for i in m:
#     print(i,main_dict[i])


# main_dict={1:10,2:20,3:30,4:40,5:50,6:60,7:70}
# print("keys values count")
# count=1
# for i in main_dict:
#     print(i,":->  ",main_dict[i]," ",count)
#     count+=1


# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for i in students:
#     print(i)
#     for j in students[i]:
#         print(j,students[i][j])


# main_dict={"name":"Nagendra Yadav","gender":"Male","School":"Navgurukul"}
# print(main_dict.keys() >= {"name","gender"})
# print(main_dict.keys()>= {"name","Nagendra"})
# print(main_dict.keys() >={"school","navgurukul"})




# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2',"shreyansh"]}
# count=0
# for i in dict:
#     for j in dict[i]:
#         count+=1
# print(count)
# print(sum(map(len,dict.values())))


# main_data={"Math":81,"Physics":83,"Chemistry":87}
# from collections import Counter
# m=Counter(main_data)
# print(m.most_common())


# l1=["Class-V","Class-VI","Class-VII","Class-VIII"]
# l2=[1,2,2,3]
# main_dict=dict(zip(l1,l2))
# for i in main_dict:
#     main_dict.update({i:{main_dict[i]}}) 
# print(set(main_dict))



# main_dict=[{"id":1,"subject":"math","V":70,"VI":82},
#            {"id":2,"subject":"math","V":73,"VI":74},
#            {"id":3,"subject":"math","V":75,"VI":86}]
# for i in main_dict:
#     n1=i.pop("V")
#     n2=i.pop("VI")
#     i["V+VI"]=(n1+n2)/2
# print(main_dict)


# main_dict1={"name":"Nagendra Yadav","gender":"male","class":"10th"}
# main_dict2={"name":"Nagendra Yadav","gender":"male","class":"12th","class":"10th"}
# for i in main_dict1:
#     if main_dict1[i]==main_dict2[i]:
#         print(i,":",main_dict1[i],"is present both dictionary")
# print("")


# import json
# main_data={'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# a=json.dumps(main_data,indent=5)
# with open("dictionary.json","w") as file:
#     file.write(a)
# with open("dictionary.json","r") as file:
#     a=json.load(file)
# print(type(a))


# main_dict=dict(x=list(range(11,20)),y=list(range(21,30)),z=list(range(31,40)))
# print(main_dict)
# print(main_dict["x"][4])
# print(main_dict["y"][4])
# print(main_dict["z"][4])
# for i,j in main_dict.items():
#     print(i,"has value",j)


# main_dict={"name":"Nagendra Yadav","gender":"male","class":None}
# main_dict={i:j for (i,j) in main_dict.items() if j is not None}
# print(main_dict)


# main_dict={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# main_dict={i:j for (i,j) in main_dict.items() if j>170 }
# print(main_dict)


# list1=['S001', 'S002', 'S003', 'S004']
# list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# list3=[85, 98, 89, 92]
# main_dict={}
# for i in range(len(list1)):
#     main_dict.update({list1[i]:{list2[i]:list3[i]}})
# print(main_dict)


# main_dict={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# result = {k:s for k, s in main_dict.items() if s[0] >=6.0 and s[1] >=70}
# print(result)


# main_dict={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# result=all(i==12 for i in main_dict.values())
# print(result)


# main_dict=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# main_dicti={}
# for i,j in main_dict:
#     main_dicti.setdefault(i,[]).append(j)
# print(main_dicti)


# main_dict={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# list1=[]
# for i in main_dict:
#     for j in main_dict[i]:
#         list1.append({i:j})
# print(list1)


# keys=main_dict.keys()
# vals=zip(*[main_dict[i] for i in keys])
# result=[dict(zip(keys,i)) for i in vals]
# print(result)


# main_dict={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# a=max(main_dict)
# b=min(main_dict)
# c=(a,b)
# print(c)


# main_dict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# a=[]
# for i in main_dict.values():
#     a.append(i)
# print(a)


# main_dict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# a=[]
# for i in main_dict:
#     a.append(i)
# print(a)


# main_dict={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# a=list(tuple(main_dict.items()))
# print(a)

# list1=['a', 'b', 'c', 'd', 'e', 'f']
# list2=[1, 2, 3, 4, 5]
# print(dict(zip(list1,list2)))


# main_dict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# a=[i for i,j in main_dict.items() if j==20]
# print(a)


# main_dict={'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
# main_dicti={}
# for i in main_dict:
#     main_dicti.update({i:main_dict[i]["age"]})
# print(main_dicti)


# main_dict=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# a=[i["age"] for i in main_dict]
# print(a)


# using json
# import json 
# main_dict={
# "student":"Nagendra Yadav",
#   "marks":[25,26,37,78],
#   "gendrer":"male"
#  }
# with open ("Nagendra.json","w") as file:
#     json.dump(main_dict,file)


# class Person:
#     def __init__(self,fname,lname,age,gender):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#         self.gender=gender
# person=Person("Nagendra","Yadav",18,"male")
# def show_object(person):
#     if isinstance(person,Person):
#         return "{} {} age -> {}-> gender ->{}".format("Nagendra","Yadav",18,"male")
# import json
# with open("Nagendra.json","w") as file:
#     json.dump(person,file,default=show_object)



# class Person:
#     def __init__(self,fname,lname,age,gender):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#         self.gender=gender
# person=Person("Nagendra","Yadav",18,"male")
# def show_object(person):
#     if isinstance(person,Person):
#         return{"name":person.fname +" "+person.lname,"age":person.age,"gender":person.gender}
# import json
# with open("Nagendra.json","w") as file:
#     json.dump(person,file,default=show_object,indent=4)

# import json
# with open("Nagendra.json","r") as file:
#     m=json.load(file)
#     print(m)
#     print(type(m))


# Pickling data type
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display_info(self):
#         print("Hi my name",self.name,"and I am",self.age,"years old")
# p=Person("Nagendra",18)

# import pickle
# with open("yadav.pkl","wb ") as f:
#     pickle.dump(p,f)

























    















































    




    
    



























        
           
        

        





        
















    

















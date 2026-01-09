# abc=[1,2,"Shailesh","Raj","Yash","Nishant"]

# print(abc[2:5])

# abc.append("AIPA")
# abc.insert(1,"NSTI")

# print(abc)


# x=(1,2,3,4,5)
# y=("Shailesh","Raj","Yash","Nishant")
# z=x+y
# print(z)
# y=list(x)
# y.append(6)
# print(y)

# students=("Shailesh","Raj","Yash","Nishant","BHavna","Vanshika","Shreya")

# for priya in students:
#     if priya == "Raj" or priya == "Yash" or priya == "Nishant":
#         continue
#     print(priya)
# print("Yash" in students)
# print(len(students ))

# x=(1,2,3,4,5)

# print(max(x))
# print(min(x))
# print(sum(x))

# z=[1,2,3,4,5,6,8]

# d=z.pop()

# print(d)
# # print(x)
# del x

# print(x)


# x=[1,2,3,4,5]
# z=x.pop(2)
# print(z)
# print(x)



#Set

# x={1,2,3,4,5}

# x.add("AIPA")
# x.update(["Shailesh","Raj","Yash","Nishant"])
# print(x)

# y={"AIPA","EM","COPA","DM"}
# z={"FDT","CSA","COPA"}
# print(y.union(z))
# print(y.intersection(z))
# print(y.difference(z))

# print(y.issubset(z))

#Dictionary

students={"name":"Priya","age":20,"Trade":"AIPA","Address":"Teliyarganj"}

#Accessing elements
# print(students["age"])
# print(students["name"])

# #adding new key and value 
# students["Marks"]=86
# students["Address"]="Teliyarganj"

#removing from dictionary

# students.pop("age")

# checking key in dataset
# print("age" in students)
# print("name" in students)
# print("Phone" in students)

# print(students)

#iterate over dictionary
# for key ,value in students.items():
#     if key == "Trade":
#         continue
#     print(key,":",value)   

#Merging Dictionary

# x={"name":"Shreya","age":"20"}
# y={"Trade":"AIPA","Address":"Prayagraj"}

# x.update(y)

# print(x)

# #nested dictionary

# students={
#     "AIPA":{"name":"Shailesh","age":20,"Trade":"AIPA","Address":"Teliyarganj"},
#     "COPA":{"name":"Raj","age":20,"Trade":"COPA","Address":"Prayagraj"},
#     "EM":{"name":"Yash","age":20,"Trade":"EM","Address":"Civil Lines"}
# }

# # print(students["EM"]["Address"])

# #copy dictionary
# students2=students.copy()

# print(students2)

# # clear dictionary

# students.clear()
# print(students)

# student = ('Rahul', (85, 90, 92))

# print(student[1][0])

# fruits = ('apple', 'banana', 'cherry')

# updated_fruit=list(fruits)

# updated_fruit[2]="Kiwi"

# print(updated_fruit)

#Students management

std_name=["Priya","Shipra","Shreya","Divyanshi","Komal","Pooja"]
trade=("CTS-AIPA")
subject={"Python","Computer Fundamentals","Database","AI","NLP"}
marks={
    "Priya":{"Python":70,"Computer Fundamentals":80,"Database":90,"AI":50,"NLP":60},
    "Shipra":{"Python":78,"Computer Fundamentals":89,"Database":99,"AI":63,"NLP":61},
    "Shreya":{"Python":70,"Computer Fundamentals":80,"Database":90,"AI":50,"NLP":60},
    "Divyanshi":{"Python":30,"Computer Fundamentals":20,"Database":50,"AI":60,"NLP":60},
    "Komal":{"Python":67,"Computer Fundamentals":90,"Database":100,"AI":45,"NLP":99},
    "Pooja":{"Python":77,"Computer Fundamentals":88,"Database":55,"AI":44,"NLP":33}
}

# print(std_name)
# print(trade)
# print(subject)
# print(marks)

# print("Priya" in std_name)

# std_name.append(input("Enter your name:"))
# std_name.insert(1,"akriti")
# std_name.remove("Shipra")

# marks["Soni"]=[40,50,66,70,80]
# marks["Rewati"]=[40,50,60,70,80]
# print(std_name)
# print(marks)

# print(marks["Komal"])


# print(marks)

# for key,value in marks.items():
#     print(key,":",value)

# a={1,2,3,2,1}
# print(len(a))


# x={"Priya","Shipra","Shreya","Divyanshi","Komal","Pooja"}

# x={
#     "priya":{"Maths":70,"Physics":80,"Chemistry":90,"Biology":50,"English":60},
#     "shipra":{"Maths":78,"Physics":89,"Chemistry":99,"Biology":63,"English":61},
#     "shreya":  {"Maths":70,"Physics":80,"Chemistry":90,"Biology":50,"English":60},
#     "divyanshi":[30,20,50,60],
#     "komal":[67,90,100,45,99],
#     "pooja":[77,88,55,44,33]    
# }

# print(x["shipra"]["Biology"])
# Dict=key:value
# x={"name":"Anamika","trade":"AIPA"}

# print(x["name"])

# x=["Sakshi","Shipra","Komal"]

# for i in x:
#     print(i)

# for key,value in x.items():
#     print(key,value)

# print(x)

# fruits=["apple","banana","cherry","Orange","Grapes"]

# print(fruits[-1])

# x=[1,2,3,4,5]

# x.pop(2)
# print(x)


# jj


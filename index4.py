#DICTIONARY AND SET

#Dictionaries are used to store data values i key : values pairs
#unordered, mutable(changeable), don't allow duplicates keys

# dict={
#     "name":"parvati",
#     "cgpa":8,
#     "marks":[98,89,95],
# }

# dict["name"]="lakshmi"   #possible
# print(dict)

# #null dictionary
# null_dict={}
# null_dict["name"]="paru"
# print(null_dict)

#Nested dictionary is possible in python
# student ={
#     "name":"parvati",
#     "subjects": {
#         "phy":98,
#         "chem":99,
#     }
# } 

# print(student["subjects"]["phy"])  #98

#DICTIONARY METHODS
#1. dict.keys()
#2. dict.values()
#3. dict.items()
#4. dict.get("name")
#5. dict.update({"city":"jaipur"})

#--------------------------------------------------
#SET:-set is the collection of unordered items
#each element in the set must be unique and immutable

#NOTE: set is mutable.......set ki values are immutable

num={1,2,3,4}
set2={1,2,2,2} #repeated elements stored only once....{1,2}
null_set=set()  #empty set syntax

#SET METHODS
#1. set.add(element)
#2. set.remove(element)
#3. set.clear()
#4. set.pop()
#5. set.union(set2)
#6. set.intersection(set2)

# WAPP to store values in dict
dictionary={
    "cat":"a small animal",
    "table":[" a piece of furniture","list of facts"],
}
print(dictionary)

#WAP 1 subject....1 classroom
subjects={
    "python","java","c++","python","c","c++","java","javascript"
}
print(len(subjects))    #5

#WAP enter 3 subjects marks store them in dictionary
marks={}
x=int(input("enter phy : "))
marks.update({"phy ": x})
x=int(input("enter chem : "))
marks.update({"chem ": x})
x=int(input("enter math : "))
marks.update({"math ": x})
print(marks)

#WAP to store 9 and 9.0 separate in set
values={9,"9.0"}
print(values)

val={("float",9.0),("int",9)}
print(val)


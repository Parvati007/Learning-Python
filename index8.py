#FILE INPUT AND OUTPUT

# 1. Opening a File
# Use open(filename, mode)
# Modes:

# "r" – read (default)
# "w" – write (overwrites)
# "a" – append
# "rb", "wb" – binary modes
# "r+" – read and write

# 2. Reading from a File

# file.read() → entire file
# file.readline() → one line
# file.readlines() → all lines in a list

# 3. Writing to a File

# file.write("text") → writes string
# file.writelines(list_of_strings)

# 4. Closing a File

# file.close() → releases resources

# with open("data.txt", "r") as f:
#     content = f.read()

#------------------------------------------------
#READING FROM THE FILE
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()
#-------------------------------------------------
# f=open("demo.txt","r")
# data= f.read(5)
# print(data)
# f.close()
#-----------------------------------------------
# f=open("demo.txt","r")
# data= f.read()
# print(data)
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()
#-----------------------------------------------------------------
#WRITING IN THE FILE
# f=open("demo.txt","w")     # w ovrewrite the file data
# f.write("hello world")
# f.close()

#--------------------------------------------------------------
# f=open("demo.txt","a")     # a add the file data at the end
# f.write("\ni am parvati")
# f.close()

#if file is not their by default it created then in folder inboth mode w and a.
#----------------------------------------------------------------------------------
#WITH syntax

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")    
#---------------------------------------
#DELETING A FILE
#using the os module
#module(like a code librar) is a file written by another programmer that generally has function we can use.

# import os
# os.remove("demo.txt")

#command to install external modules
#pip install tensorflow
#pip3 install tensorflow

#-----------------------------------------------------------------------
#PRACTICE QUESTIONS
#create a new fule practice.txt using python add following data
#hi everyone
#we are learning file i/o
#using java
#i like programming in java

# with open("practice.txt","w") as f:
#     f.write("hi everyone\nwe are learning java\n")
#     f.write("using java.\ni like programming in java.")

#-----------------------------------------------------------------------    
#now replace all occurence of java with python in above file

# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace('java','python')
# print(new_data)
# with open('practice.txt','w') as f:
#     f.write(new_data)

#------------------------------------------------------------------------   
# search if the word learning exist in file or not
word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")         
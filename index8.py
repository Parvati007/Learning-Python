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
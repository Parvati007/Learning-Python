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

f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))

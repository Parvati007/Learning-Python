#Strings: data type that store a sequence of characters
# Escape sequence character =\n,\t
# basic operations in strings
# 1.concatenation 
str1="hello"
str2="world"
print(str1+str2)  #helloworld

# 2.length of string
str="parvati kumari" # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
print(len(str))# 14

#3. Indexing
str3="paru"
print(str3[0]) #p
print(str3[2]) #r

#4. slicing              strting index is included but ending index is excluded
str4="aditi singh"
print(str4[2:4])  #it
print(str4[:6])   #aditi
print(str4[0:len(str4)])    #aditi singh

# 5. negative index slicing
# apple  -5 -4 -3 -2 -1
str5="apple"
print(str5[-3:-1])  #pl


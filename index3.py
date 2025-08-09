#LISTS

# A built-in data type that stores set of values
# can store diff types of elements
# NOTE : Strings are immutable and lists are mutabale

# marks=[87,64,33,95,88]
# student=["ajay",98,"delhi"]
# student[0]="jay" #lists are mutable
# print(student)
# # print(len(student))

# #list slicing is exactly same as strings slicing

# #LIST METHODS: not returns anything just modilfy the original lists

# list=[2, 1, 3]
# list.append(4)
# print(list)          #[2,1,3,4]
# list.sort()
# print(list)          #[1,2,3,4]
# list.sort(reverse=True)
# print(list)          #[4,3,2,1]
# list.reverse
# print(list)         #[4,3,2,1]
# list.insert(1,5)
# print(list)         #[4,5,3,2,1]

# list1=[2, 1, 3, 1]
# list1.remove(1)     #[2,3,1]
# print(list1)
# list1.pop(0)        #[3,1]
# print(list1)

#TUPLES
#a built-in data type that let us create immutable sequences of values
# tup=()
# tup1=(1,)
# print(type(tup1))   #tuple
# tup2=(1)
# print(type(tup2))   #int
# tup3=(1,2,3,4,5)
#tup3[0]=7           #this is not possible erroe will occur

#Tuples-methods
# tup4=(2,3,4,5,5,6,7)
# print(tup4.index(3))  #1
# print(tup4.count(5)) #2

#WAP for the palindrome
# code=["m","a","a","m"]
# copy_code=code.copy()
# copy_code.reverse()
# if(copy_code==code):
#     print("palindrome")
# else:
#     print("not a palindrome")

#WAP to enter 3 movies in list    
# movies=[]
# movies.append(input("Enter 1st movie name : "))
# movies.append(input("Enter 2nd movie name : "))
# movies.append(input("Enter 3rd movie name : "))
# print(movies)

#WAP to sort a list
grade=["A","D","C","P","A"]
grade.sort()
print(grade)                #A,A,C,D,P

#WAP to count a "A" in tuple
alpha=("A","A","A","P","A")
print(alpha.count("A"))              #4






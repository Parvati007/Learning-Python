#LISTS
# A built-in data type that stores set of values
# can store diff types of elements
# NOTE : Strings are immutable and lists are mutabale

# marks=[87,64,33,95,88]
# student=["ajay",98,"delhi"]
# student[0]="jay" #lists are mutable
# print(student)
# print(len(student))

#list slicing is exactly same as strings slicing

#LIST METHODS: not returns anything just modilfy the original lists

list=[2, 1, 3]
list.append(4)
print(list)          #[2,1,3,4]
list.sort()
print(list)          #[1,2,3,4]
list.sort(reverse=True)
print(list)          #[4,3,2,1]
list.reverse
print(list)         #[4,3,2,1]
list.insert(1,5)
print(list)         #[4,5,3,2,1]

list1=[2, 1, 3, 1]
list1.remove(1)     #[2,3,1]
print(list1)
list1.pop(0)        #[3,1]
print(list1)




#PROJECT

# Easy to Learn & Readable – Simple syntax close to English.
# Versatile – Used in web development, AI/ML, data science, automation, etc.
# Large Community Support – Huge libraries, frameworks, and active community.
# Cross-Platform – Works on Windows, macOS, Linux without major changes.
# Rapid Development – Speeds up prototyping and project completion.
# Strong Library Ecosystem – NumPy, Pandas, TensorFlow, Django, Flask, etc.
# High Demand – Popular in industry, increasing career opportunities.

#-----------------------------------------------------------------------------------
#GUESS THE NUMBER

# import random
# target =random.randint(1,100)
# while(True):
#     userChoice=input("Guess the target or Quit: ")
#     if(userChoice=="Quit"):
#         break
#     userChoice=int(userChoice)
#     if(userChoice==target):
#         print("Success : Correct Guess!! ")
#         break
#     elif(userChoice<target):
#         print("your number was too small.Take a bigger guess.")
#     else:
#         print('your number was too big.Take a smaller guess.')
# print('--------------------GAME OVER-------------------')            

#---------------------------------------------------------------------------------------
#RANDOM PASSWORD GENERATOR

import random
import string

pass_len=8
charValues = string.ascii_letters+ string.digits + string.punctuation

#list comprehension [function for i in range(n)]                                   #method 1
#password = "".join([random.choice(charValues) for i in range(pass_len)])

password =""                                                                      #method 2
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is : ",password)    
     


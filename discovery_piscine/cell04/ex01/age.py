#!/usr/bin/env python3


age = int(input("Please tell me your age: "))
print("You are currently " + str(age) + " years old.")
# print("In 10 years, you'll be " + str(age + 10) + " years old.")
# print("In 20 years, you'll be " + str(age + 20) + " years old.")
# print("In 30 years, you'll be " + str(age + 30) + " years old.")

for i in [10 , 20 , 30]:
    print("In 30 years, you'll be " + str(age + i) + " years old.")

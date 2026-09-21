#!/usr/bin/env python3

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

result = first * second

print(f"{first} x {second} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

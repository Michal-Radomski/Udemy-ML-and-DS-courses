# print("Hello World!")

# age = input("How old are you? ")
# print("You are: " + age + " years old!")

# * Fundamental data types
# int -> 3, 5, -2
# float -> 0.5
# complex
# str
# bool
# list
# tuple
# set
# dict
# None

# * Number and float
print(type(2 + 4))
print(type(2.5 + 4.5))
print(2 + 4)
print(type(2 - 4))
print(type(2 * 4))
print(2 / 4)
print(2.1 + 4.9)  # 7.0 -> float
print(2**4)
print(10 // 4)  # -> integer rounded down: 2 (Floor division operator)
print(10 % 4)  # -> modulo: 2

# * Math functions
print(round(3.1))
print(round(3.5))  # 4
print(abs(0))
print(abs(-3.1))
print(abs(3.1))

# * Bin()
number = 15
binary_representation = bin(number)
print("Binary of", number, "is", binary_representation)
# Output: Binary of 15 is 0b1111
print(int("0b1111", 2))  # 15

# * Variables
user_iq1 = 190
print(user_iq1)  # 190
user_age = user_iq1 / 4
print(user_age)  # 47.5

# * Constants
PI = 3.14  # only convention
print(PI)
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Exercise Augmented Assignment Operator
counter = 0
counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *= 2
print(counter)  # 6

# * Strings
first_name = "Michal"
last_name = "R"
full_name = first_name + " " + last_name
print(full_name)

long_string = """
WOW
0 0
---
"""
print(long_string)

# String Concatenation
print("hello" + " Michal")
print("hello " + str(5))
print("\n")

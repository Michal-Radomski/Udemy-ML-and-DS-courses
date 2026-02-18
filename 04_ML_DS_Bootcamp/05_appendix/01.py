from datetime import datetime

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

# Type Conversion
print(type(int(str(100))))

a = str(100)
b = int(a)
c = type(b)
print(c)
print("\n")


# Escape Sequences
weather = '\t It\'s "kind of" sunny \n Hope you have a good day!'
print(weather)
print("\n")

# Formatted Strings
name = "Johnny"
age = 55
print("Hi" + name + ". You are" + str(age) + " years old.")
print(f"Hi {name}. You are {age} years old.")  # f -> formatted string

# Python2 Formatted Strings
print("Hi {}. Your are {} years old.".format(name, age))
print("Hi {1}. You are {0} years old.".format(age, name))
print("Hi {new_name}. You are {age} years old.".format(new_name="Sally", age=100))
print("\n")

# String Indexes
# [start:stop:stepover (default->1)]
python = "I am PYTHON"
print(python[1:4])  # " am"
print(python[1:])  # " am PYTHON"
print(python[:])  # "I am PYTHON"
print(python[1:100])  # " am PYTHON"
print(python[-1])  # "N"
print(python[-4])  # " T"
print(python[:-3])  # "I am PYT"
print(python[-3:])  # "HON"
print(python[::-1])  # "NOHTYP ma I"
print("\n")

# * Strings are Immutable!
selfish = "01234567"
selfish = selfish + "8"
print(selfish)  # 012345678


# Built-In Functions + Methods
# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp
print(len("Helllooooo"))
quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find("be"))
print(quote.replace("be", "me"))
print(quote)  # "to be or not to be"


# * Boolean
is_cool = True
is_cool = False
print(bool(-0))  # False
print(bool(0))  # False
print(bool(1))  # True
print(bool(0.5))  # True
print(bool("0"))  # True
print(bool("True"))  # True
print(bool("False"))  # True
print(bool(False))  # False
print(bool("any random thing"))  # True

# * Exercise
current_year = datetime.now().year

birth_year = input("What year were you born?\n")  # input -> type:string!
age = current_year - int(birth_year)
print(f"Your age is {age} years.")

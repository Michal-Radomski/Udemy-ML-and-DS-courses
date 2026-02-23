# * For Loops
for item in "Zero to Mastery":
    print(item, end=" ")
print()

for item in [1, 2, 3, 4, 5]:
    print(item, end=" ")
print()

for item in {1, 2, 3, 4, 5}:
    print(item, end=" ")
print()

for item in (1, 2, 3, 4, 5):
    print(item, end=" ")
print(item)
print()

# Nested Loops
for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(
            item, x, end="\t"
        )  # 1 a	1 b	1 c	2 a	2 b	2 c	3 a	3 b	3 c	4 a	4 b	4 c	5 a	5 b	5 c

# * Iterable -> list, dictionary, tuple, set, string
user = {"age": 45, "name": "john", "size": 10}

for i in user:
    print(i)

for i in user.keys():
    print(i)

for i in user.values():
    print(i)

for (
    i
) in user.items():  # it stores each pair as tuple, in a list (in a dict_items class).
    print(i)

print(user.items())
print(type(user.items()))
print(list(user.items()))

for key, value in user.items():
    print(key, value)
# age 45
# name john
# size 10

for item in user.items():
    key, value = item
    print(key, value)
# age 45
# name john
# size 10

# Write a program to find the sum of items in the list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for item in my_list:
    counter += item

print(counter)  # 55


# * Range -> stop is omitted!
print(range(100))  # range(0, 100)
print(list(range(100)))  # [0, 1, ..., 99]

for _ in range(1, 5):
    print(_)  # 1 2 3 4

print("\n")
for _ in range(1, 10, 2):
    print(_)  # 1 3 5 7 9

print("\n")
for _ in range(10, 0, -1):
    print(_)  # 10 ... 1


# * Enumerate()
for i, char in enumerate("Hello"):
    print(i, char)
# 0 H
# 1 e
# 2 l
# 3 l
# 4 o

for i, char in enumerate([1, 2, 3]):
    print(i, char)

for i, char in enumerate(range(100)):
    if char == 50:
        print(f"index of 50 is: {i}")


# * While loops
i = 0
while i < 50:
    print(i, end="\t")
    i += 1
else:
    print("\nDone with all the work.")
print()

my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
# 1
# 2
# 3
print()

while True:
    response = input("Say Something: ")
    if response == "bye":
        break


# * Break, Continue, Pass
my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
print()
# 1
# 2
# 3

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break
print()
# 1

i = 0
while i < len(my_list):
    i += 1
    pass  # Does nothing!

print("No error")  # No error


# * Exercise!
# * Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# Answer:
for row in picture:
    for pixel in row:
        if pixel:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
#    *
#   ***
#  *****
# *******
#    *
#    *
#    *

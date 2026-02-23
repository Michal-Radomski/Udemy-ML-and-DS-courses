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

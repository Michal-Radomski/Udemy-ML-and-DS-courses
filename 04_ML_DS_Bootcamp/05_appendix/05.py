from functools import reduce


# * *args and **kwargs
def super_func(
    *args, **kwargs
):  # we can actually name these parameters anything we want, but its a good practice to give the same name only.
    print(args)  # (1, 2, 3, 4, 5)
    print(type(args))  # <class 'tuple'>
    print(*args)  # 1 2 3 4 5
    # print(type(*args)) 	# gives error

    print(kwargs)  # {'num1': 5, 'num2': 10}
    # print(**kwargs) 	# gives error
    print(kwargs.keys())  # dict_keys(['num1', 'num2'])
    print(kwargs.values())  # dict_values([5, 10])
    print(type(kwargs))  # <class 'dict'>

    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total  # sum() is build-in function!


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))  # 30

# Rules for the order of parameters
# positional parameters, *args, default parameters, **kwargs


# * Exercise
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))  # 10


# * Global keyword - Not good practice!
total = 0


def count():
    global total  # Use the global variable total
    total += 1  # here we are referenced total before assignment, hence we have declare 'global total' first
    return total


count()
count()
count()

print(total)  # 3


# * Nonlocal keyword - it is used to access parent variables - Not good practice!
def outer():
    x = "outer"

    def inner():
        nonlocal x  # this won't create a new variable 'x', and will modify the parent 'x' only.
        x = "inner"
        print("inner x: " + x)  # inner x: inner

    inner()
    print("outer x: " + x)  # outer x: inner


outer()


def outer2():
    x = "outer"

    def inner2():
        x = "inner"
        print("inner2 x: " + x)  # inner2 x: inner

    inner2()
    print("outer2 x: " + x)  # outer2 x: outer


outer2()


# * Pure Functions
def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item * 2)
    return new_li


print(multiply_by2([5, 6, 8]))  # [10, 12, 16]
"""
If we define 'new_li' outside the function, or print something inside the function, then it is no longer a pure function.
"""


# * Map()
def multiply_by2(item):
    return item * 2


my_list = [5, 8, 9]

# it returns a map object, which then we can convert to a list/tuple/set
print(map(multiply_by2, my_list))  # <map object at 0x7789e8f92cb0

# notice that we just write the function name without the curly braces
print(list(map(multiply_by2, my_list)))  # [10, 16, 18]
print(my_list)  # [5, 8, 9]

"""
notice that map is not modifying anything, and creating a new list.
it is also using separate data and function to work upon them.
it's a nice concept of Functional programming and pure function.
"""


# * Filter()
def only_even(item):
    return item % 2 == 0


my_list = [5, 8, 9, 2, 5, 6, 98, 56, 62]

print(filter(only_even, my_list))  # <filter object at 0x7a1c8378f130>
print(list(filter(only_even, my_list)))  # [8, 2, 6, 98, 56, 62]
print(
    list(map(only_even, my_list))
)  # [False, True, False, True, False, True, True, True, True]
print(my_list)  # [5, 8, 9, 2, 5, 6, 98, 56, 62]

# * Zip()
li1 = [1, 2, 3]
set1 = {4, 5, 6}
tuple1 = (7, 8, 9)

print(zip(li1, set1, tuple1))  # <zip object at 0x71e34d64b780>
print(
    list(zip(li1, set1, tuple1))
)  # combines the items sequence wise into a sequence of tuples -> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(li1, set1, tuple1)  # [1, 2, 3] {4, 5, 6} (7, 8, 9)


# * Reduce()
def accumulator(acc, item):
    print(f"acc: {acc}, item: {item}")
    return acc + item


my_list = [1, 2, 3, 4, 5]
print(reduce(accumulator, my_list))  # by default takes '0' as the 3rd argument -> 15
print(reduce(accumulator, my_list), 0)  # by default takes '0' as the 3rd argument -> 15
print(reduce(accumulator, my_list, 10))  # 25
print(my_list)  # [1, 2, 3, 4, 5]

"""
acc is nothing but the return of the last iteration.
"""

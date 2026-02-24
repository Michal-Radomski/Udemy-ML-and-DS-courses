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

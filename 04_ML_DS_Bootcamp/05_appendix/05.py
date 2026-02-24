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

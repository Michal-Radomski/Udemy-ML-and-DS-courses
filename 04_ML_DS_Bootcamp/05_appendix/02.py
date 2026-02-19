# * Lists (Array in JS/TS) -> ordered by index

li = [1, 2.5, "hello", True]
print(li)

amazon_cart = ["laptop", "book", "phone", "pen", "key"]
# start:stop:stepover
print(amazon_cart[0])  # laptop
print(amazon_cart[::-1])  # ['key', 'pen', 'phone', 'book', 'laptop']
print(amazon_cart[0:2])  # ['laptop', 'book']
print(amazon_cart)  # ['laptop', 'book', 'phone', 'pen', 'key']
# * List slicing makes a new copy of a list


# * Matrix
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
print(basket)
print(basket[1][1][0])  # Oranges


# * List Methods
# * Adding
print("\nappend")
li = [1, 2, 3, 4, 5]
new_li = li.append(100)
print(li)  # [1, 2, 3, 4, 5, 100] -> at the end
print(new_li)  # None

print("\ninsert")
new_li = li.insert(2, 2000)
print(li)  # [1, 2, 2000, 3, 4, 5, 100] -> index, object
print(new_li)  # None

print("\nextend")
new_li = li.extend([45, "hello"])
print(li)  # [1, 2, 2000, 3, 4, 5, 100, 45, 'hello'] -> iterable at the end
print(new_li)  # None

# * Removing
print("\npop")
new_li = li.pop()
print(
    li
)  # [1, 2, 2000, 3, 4, 5, 100, 45] -> remove at the index -1 (default) or given index!
print(new_li)  # hello

print("\npop")
new_li = li.pop(0)
print(
    li
)  # [2, 2000, 3, 4, 5, 100, 45] -> remove at the index -1 (default) or given index!
print(new_li)  # 1

print("\nremove")
new_li = li.remove(2000)
print(li)  # [2, 3, 4, 5, 100, 45]
print(new_li)  # None

print("\nclear")
new_li = li.clear()
print(li)  # []
print(new_li)  # None


li = ["a", "b", "c", "d", "e", "d"]
print(
    li.index("d")
)  # if that value is not there in the list, then it will throw an error and program will stop running. -> 3

# lookup:start:stop
print(li.index("d", 0, 5))  # 3


print("a" in li)  # we use this to avoid the error. -> True
print("x" in li)  # False
print(li.count("d"))  # 2


li2 = [1, 2, 5, 6, 7, 4, 56, 38, 0]
print(li2.sort())  # None
print(li2)  # [0, 1, 2, 4, 5, 6, 7, 38, 56]

print(li2.reverse())  # None
print(li2)  # [56, 38, 7, 6, 5, 4, 2, 1, 0

print("Sorted function")
print(
    sorted(li2)
)  # its a function which sort the list, but it does not modify the list permanently. -> # [0, 1, 2, 4, 5, 6, 7, 38, 56]
print(li2)  # [56, 38, 7, 6, 5, 4, 2, 1, 0]

new_li2 = li2.copy()  # same as doing new_li = li[:]
print(new_li2)  # [56, 38, 7, 6, 5, 4, 2, 1, 0]

print(list(range(1, 100)))

words = ["Hello", "world", "from", "Python"]
result = " ".join(words)
print(result)  # Hello world from Python

# List Unpacking
a, b, c, *other, d = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
]  # this will work with set, tuple and normal (as in 1,2,3,4,5) also. and it always store the variables as list, if more than one item, otherwise as int.

print(type(a))
print(b)  # 2
print(c)  # 3
print(other)  # [4, 5, 6, 7, 8, 9]
print(type(other))
print(d)  # 0

# * None
weapons = None
print(weapons)  # None -> null in JS/TS


# Dictionaries -> unordered key-value pair
my_dict = {"a": [1, 2, 3], "b": "hello", "c": True}
print(type(my_dict))  # <class 'dict'>

my_list = [
    {"a": [1, 2, 3], "b": "hello", "c": True},
    {"a": [4, 5, 6], "b": "bye", "c": False},
]

print(my_dict["a"])  # [1, 2, 3]
print(my_dict["a"][1])  # 2
print(my_list[1]["a"][2])  # 6

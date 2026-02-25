# * List Comprehensions
my_list = []

for item in "hello":
    my_list.append(item)

print(my_list)  # ['h', 'e', 'l', 'l', 'o']

my_list1 = [item for item in "Saurabh"]
print(my_list1)  # ['S', 'a', 'u', 'r', 'a', 'b', 'h']

my_list2 = [num**2 for num in range(1, 11)]
print(my_list2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# * Set and Dictionary Comprehension
# only even squares
my_set = {num**2 for num in range(1, 11) if num**2 % 2 == 0}
print(my_set)  # {64, 100, 4, 36, 16}
# remember that set don't contain duplicate values

my_dict = {num: num**2 for num in range(1, 11)}
print(my_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


random_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

my_new_dict = {k: v**2 for k, v in random_dict.items()}
print(my_new_dict)  # {'a': 1, 'b': 4, 'c': 9, 'd': 16}

my_new_dict2 = {k: v**2 for k, v in random_dict.items() if v % 2 == 0}
print(my_new_dict2)  # {'b': 4, 'd': 16}


x = 5
print(x)
x = int(5)
print(x)

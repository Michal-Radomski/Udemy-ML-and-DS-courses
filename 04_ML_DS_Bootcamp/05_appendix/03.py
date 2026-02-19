from decimal import Decimal
from fractions import Fraction

# * Conditional Logic
a = True
b = False

if a and b:
    print("Both a and b are true")
elif a:
    print("Only a is true")
elif b:
    print("Only b is true")
else:
    print("Both a and b are false")

is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You are old enough to drive, and you have a license!")
else:
    print("You are not of age!")


# *  Truthy vs Falsy
print(bool("hello"))  # True
print(bool(5))  # True
print(bool(""))  # False
print(bool())  # False

# * All values are considered "truthy" except for the following, which are "falsy":
# None
# False
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
#     obj.__bool__() returns False
#     obj.__len__() returns 0


zero_dec = Decimal(0)
print(zero_dec)  # Decimal('0')
print(zero_dec == 0)  # True [web:11]

zero_frac = Fraction(0, 1)
print(zero_frac)  # 0
print(float(zero_frac))  # 0.0 [web:11]


# * Ternary Operator
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)  # message allowed

# * Short Circuiting
is_friend = True
is_user = True
print(is_friend and is_user)  # True
print(is_friend or is_user)  # True

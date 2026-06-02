# 1) Create variables to store different types of values:

# - `name` as text (string)

name = "Penguin"

# - `age` as a whole number (integer)
age=15
# - `is_student` as True/False (boolean)
is_student=True
# - `weight` as a decimal number (float)
weight=40.5
# 2) Print each variable’s value.
print("Age:",age)
# 3) Print the datatype of each variable using `type()`.
print("Data type of Age is",type(age))
print("Name :", name)

print("Data Type of Name is", type(name))

# 4) Show a message that type casting will happen next.
print("we will do typecasting now")
# 5) Convert `age` from an integer to a string and store it back in `age`.

age = str(age)

print(age)

# 6) Print `age` and print its datatype again to confirm it changed.

# 7) Convert `weight` from a float to an integer and store it back in `weight`.
weight=int(weight)
# 8) Print `weight` and print its datatype again to confirm it changed.
print("weight" ,weight)
print("Data type of weight is",type(weight))
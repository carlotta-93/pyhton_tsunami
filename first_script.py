import math


def say_hi():
    print("Hi")


say_hi()

x = 100
another_variable = 1
print(another_variable + x)

print("I have", x, "DKK")

y = x * 2

# Formatted values

first = "Carlotta"
last = "Porcelli"

name = "First Name: {}, Last Name: {}".format(first, last)
name2 = f"First Name: {first}, Last Name: {last}"

print(name)
print(name2)

decimal = 12.56345634534
integer = int(decimal)
print(integer)

a = '12'
float(a)

# get input from user
value1 = input("Please enter the first value:\n")
value1 = int(value1)

value2 = input("Please enter the second value:\n")
value2 = int(value2)

print(f'You entered {value1} and {value2} \n the multiplication is: {value1 * value2}')

print(f'You entered {value1} and {value2} \n the squares of the numbers are : {value1 ** 2} and '
      f'{value2 ** 2}')

print(math.sqrt(25))


# define random_things
random_things = ["string", 1, 2.0, 3]
print(random_things)
# define ints
ints = list(range(1, 100))
print(ints)

friends = ["Ashley", "Matt", "Michael"]
print(friends[0])
print(friends[2])
print(friends[1])  # IndexError

print("NEGATIVE indexes")
friends = ["Ashley", "Matt", "Michael"]
print(friends[-1])
print(friends[-3])
print(friends[-2])  # IndexError

print("Check if value is in list")
friends = ["Ashley", "Matt", "Michael"]
print("Ashley" in friends)
print("Jason" in friends)

# for loops for lists
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)

# while loop

numbers = [1, 2, 3, 4]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# mutate lists
# DON'T TOUCH THIS PLEASE!
people = ["Petre", "Joanna", "Louis", "Angie", "Monika", "george"]
# DON'T TOUCH THIS PLEASE!
# Change "Petre" to "Peter"
people[0] = "Peter"
# Change "Monika" to "Monica"
people[4] = "Monica"
# Change "george" to "George" (capitalize it)
people[5] = people[5].capitalize()

print(people)

# append method
first_list = [1, 2, 3, 4]

first_list.append(5)
print(first_list)

# add multiple elements
correct_list = [1, 2, 3, 4]
correct_list.extend([5, 6, 7, 8])
print(correct_list)

# insert element in the middle of the list
first_list = [1, 2, 3, 4]
first_list.insert(2, 'Hi!')
print(first_list)

first_list.insert(-1, 'The end!')
print(first_list)

# clear
first_list = [1, 2, 3, 4]
first_list.clear()
print(first_list)

# pop
first_list = [1, 2, 3, 4]
last_item = first_list.pop()
print(last_item)
second_item = first_list.pop(1)
print(second_item)

# remove
first_list = [1, 2, 3, 4, 4, 4]
first_list.remove(2)
print(first_list)
first_list.remove(4)
print(first_list)

# del
first_list = [1, 2, 3, 4]
del first_list[3]
print(first_list)
del first_list[1]
print(first_list)

# index
numbers = [5, 6, 7, 8, 9, 10, "nino"]
print(numbers.index(6))
print(numbers.index(9))
print(numbers.index("nino"))

numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]

print(numbers.index(5))
# find first 5 starting from position at index 1
print(numbers.index(5, 1))
# find first 5 starting from position at index 2
print(numbers.index(5, 2))
# find first 8 from position starting at index 6 and before index 8
print(numbers.index(8, 6, 8))

# count
numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]

print(numbers.count(2))
print(numbers.count(21))
print(numbers.count(3))

# reverse
first_list = [1, 2, 3, 4]
first_list.reverse()
print(first_list)

# sort
another_list = [6, 4, 1, 2, 5]
another_list.sort()
print(another_list)

# join
words = ['Coding', 'Is', 'Fun!']
' '.join(words)

# Exercise
print("This is the Exercise")
# Create a list called instructors
instructors = list()
# Add the following strings to the instructors list
# "Marc"
# "Rita"
# "Henry"

instructors.extend(["Marc", "Rita", "Henry"])
# Remove the last value in the list
instructors.pop(-1)
print(instructors)
# Remove the first value in the list
instructors.pop(0)
print(instructors)

# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")

# Print to make sure you did this right
print(instructors)

# slice
first_list = [1, 2, 3, 4, 5, 6]

first_list[1::2]  # [2, 4, 6]

first_list[::2] # [1, 3, 5]
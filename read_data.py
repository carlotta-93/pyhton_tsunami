# Import data

import csv

filepath = "./data/sample.txt"

# with open(filepath, 'r') as reader:
#    print(reader.read())

# "/Users/qbp693/Dropbox/PhD documentation/PythonTsunami/PythonTsunami-intro/data/sample.csv"
# "/Users/qbp693/Dropbox/PhD documentation/PythonTsunami/PythonTsunami-intro/data/iris.tsv"

# with open(filepath, 'r') as reader:
#   print(reader.readline())


# with open(filepath, 'r') as reader:
#    print(reader.readlines())

# with open(filepath, 'r') as reader:
#    for line in reader.readlines():
#        print("New line:", line)

filepath2 = 'data/sample.csv'
my_lines = []

# with open(filepath2, 'r') as reader:
# for line in reader:
# line_list = line.split(',')
# my_lines.append(line_list)
#        print(line)
# print("this is the result")
# print(my_lines)


# with open(filepath2, 'r') as myFile:
#    lines = csv.reader(myFile, delimiter=',')
#   for line in lines:
#       print(line)

# how to write data

# with open('./data/my_file.txt', 'w') as output:
#    output.write("my new file content\n")


# with open("./data/iris.tsv", 'r') as iris_file:
#     lines = iris_file.read()
#     print(lines)

# with open("./data/iris.tsv", 'r') as iris_file:
#     lines_2 = csv.reader(iris_file, delimiter=',')
#     print(lines_2)

with open("./data/iris.tsv", 'r') as iris_file:
    my_line = iris_file.readlines()
    for line in my_line:
        print(line)

with open('./data/sample.txt', "a") as out:
    out.write("Denmark/Zealand\n")

with open('./data/sample.txt', "r") as out:
    dk_line = out.read()
    print(dk_line)



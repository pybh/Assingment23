#  5 Write a Python program to read last n lines of a file
# Get the number of lines to read from user input
n = int(input(" Enter the no of line from last :  "))
# Open the file "bhagya.txt" in read mode ("r")
file = open("bhagya.txt", "r")
# read all lines from file and store it into a variable j 
j = file.readlines()
# Read and print the  last specified number of lines from the file
for line in j[-n:]:
    # print The last specified Lines from "python.txt"
    print(line, end="")
    # closing The file
file.close()
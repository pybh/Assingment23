#  4 Write a Python program to read first n lines of a file.
# Get the number of lines to read from user input
n = int(input("Enter The lines : "))
# Open the file "bhagya.txt" in read mode ("r")
file = open("bhagya.txt", "r")
# Read and print the specified number of lines from the file
for i in range(n):
    # read And print the lines 
    print(file.readline(), end="")
# closing The File
file.close()
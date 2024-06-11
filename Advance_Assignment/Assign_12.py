# 12 Write a Python program to copy the contents of a file to another file. 

# Open the file "main.txt" in read mode ("r")
file = open("main.txt","r")


# we created a variable "k"
k=""
# we get the data of file using loop into a "j" variable
for j in file:
    # now append or add the data into "k" Name variable
    k+=j
    # print the k
print(k)
# closing  The File
file.close()
# Open the file "bhagya.txt" in append mode ("a")
file=open("bhagya.txt","a")
# writing in the file "python.txt"
file.write("\n")
file.write(k)
# closing The file
file.close()
# Open the file "bhagya.txt" in read mode ("r")
file=open("bhagya.txt","r")
# print and read lines from python.txt
print(file.readlines())
# closing The File
file.close()
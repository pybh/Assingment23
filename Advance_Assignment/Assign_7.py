# 7 Write a Python program to read a file line by line store it into a variable.
# Open the file "bhagya.txt" in read mode ("r")
file =open("bhagya.txt","r")
# taking a variable name "h"
h=""
# taking all the data from the file using loop and store it into j 
for j in file:
    # now append or add the data in h
    h+=j
#   print the "h"
print(h)
# closing The file
file.close()

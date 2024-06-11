# 2 Write a Python program to read an entire text file
# open a bhagya.txt file in write mode ("w")
file=open("bhagya.txt","w")
# Writing anything in file or text
file.write("Python is very easy to use")
file.write("\n")
# Closing the file 
file.close()
# open a bhagya.txt file in read mode ("r")
file=open("bhagya.txt","r")
# Reading And Printing the content of the file
print(file.readlines())
# closing the file
file.close()
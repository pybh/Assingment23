#  3 Write a Python program to append text to a file and display the text.

# Open the file "bhagya.txt" in append mode ("a")
file=open("bhagya.txt","a")
# writing in the file "python.txt"
file.write("python is very useful language")
# closing The file
file.close()

# Open the file "bhagya.txt" in append mode ("r")
file=open("bhagya.txt","r")
# reading And printing lines in "python.txt"
print(file.readlines())
# closing The File
file.close()
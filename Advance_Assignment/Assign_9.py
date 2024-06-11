# Write a Python program to count the number of lines in a text file. 
# Open the file "bhagya.txt" in read mode ("r")
file = open("bhagya.txt","r")
# now we take a count variable which is equal to 0
count=0
# we get the value of file through loop in variable "j"
for j in file:
    # we make a condition of if 
    if j.split("."):
        # if condition satisfies the count is incremented by 1
        count+=1
# print the Count
print(count)
# closing The file
file.close()
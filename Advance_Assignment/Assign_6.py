# 6 Write a Python program to read a file line by line and store it into a list
# Open the file "bhagya.txt" in read mode ("r")
file =open("bhagya.txt","r")
# taking a "h" blank list
h=[]
# now start a loop which can store all the data in j variable
for j in file:
    # now we append all the data in h name list which created
    h.append(j)
    # print the list 
print(h)
# closing the file
file.close()
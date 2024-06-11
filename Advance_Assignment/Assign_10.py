# 10 Write a Python program to count the frequency of words in a file.

# Open the file "bhagya.txt" in read mode ("r")
file =open("bhagya.txt","r")
# now take a variable "l"
l=""
# now we have initiated a loop which get the value in file to a variable "f"
for f in file:
    # now append or add the data into variable "l"
    l+=f
    # now we split the data of l and store it into "j"
j=l.split()
# now  we take user input from user that which word have to take for count the frequency
n=input("enter The word : ")
# now take count variable which equal to 0
count=0
# now we take a another loop which store the value of "j" into the "v" variable
for v in j:
    #  now we take condition that when v equal to n
    if v==n:
        # increment The count value
        count+=1
# print the count
print(count)
# closing The File
file.close()

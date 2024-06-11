# 8 Write a python program to find the longest words. 
# Open the file "bhagya.txt" in read mode ("r")
file = open("bhagya.txt", "r")
# take a variable "j"
j=""
# now using loop take all the data from bhagya.txt file in variable m
for m in file:
    # add or append the data in j
    j+=m
    
# now we make a variable l which split the "j"
l = j.split()

# now we take a empty  list "b"
b = []
# we take a variable length have value = zero
length = 0
# first we get the data from l in variable name word through for
for word in l:
    # now we strip the data we recieve from word
    word = word.strip()
    # now we take len(word) to a new variable word_length
    word_length = len(word)
#    now we can put a condition word_length > length 
    if word_length > length:
        # we create a variable b which store word
        b = [word]
        # length = word_length
        length = word_length
# print the resultant variable b
print(b)
# closing The file
file.close()
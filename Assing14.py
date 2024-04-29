b = int(input(" enter the no of line from last :  "))
file = open("python.txt", "r")
j = file.readlines()
for line in j[-b:]:
     print(line, end="")
file.close()
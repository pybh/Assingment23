file=open("file1.txt","w")
file.write("this is a text file !!!")
file.close()

file=open("file1.txt","r")
print(file.readline())
file.close()

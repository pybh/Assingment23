file=open("file1.txt","a")
file.write("this is a text file 2 !!!")
file.close()

file=open("file1.txt","r")
print(file.readlines())
file.close()

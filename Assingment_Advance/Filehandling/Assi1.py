file1=open("demo1.txt","w")
file1.write("thios is a demo file ")
file1.close()

file1=open("demo1.txt","r")
print(file1.readlines())
file1.close()

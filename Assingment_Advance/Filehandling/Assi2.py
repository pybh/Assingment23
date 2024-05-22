file1=open("demo1.txt","a")
file1.write("\n")
file1.write("this is a demo file 2 ")
file1.close()


file1=open("demo1.txt","r")
for i in file1:
    print(i)
file1.close()


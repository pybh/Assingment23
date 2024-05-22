file3=open("demo2.txt","w")
file3.write("india is a big country in the world and many people are move in india.")
file3.write("\n")
file3.write(" india is a famous in the world. ")
file3.close()

n=int(input("enter a read first line :"))
file3=open("demo2.txt","r")
first=file3.readline()
for i in range(n):
         print(first)
file3.close()


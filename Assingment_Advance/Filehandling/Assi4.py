n=int(input("enter a read last line :"))
file3=open("demo2.txt","r")
last=file3.readlines()
for i in last[-n:]:
      print(i,end="")
file3.close()
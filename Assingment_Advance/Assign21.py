l=["Python is very easy and useful Language and very important to use "]
for j in l:
     print(j)
file=open("harsh.txt","w")
file.write(j)
file.close
file=open("harsh.txt","r") 
print(file.readlines())
file.close()
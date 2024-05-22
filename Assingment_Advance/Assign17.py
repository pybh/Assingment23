file=open("harsh.txt","r")
k=""
for j in file:
    k+=j
print(k)
file.close()
file=open("python.txt","a")
file.write("\n")
file.write(k)
file.close()
file=open("python.txt","r")
print(file.readlines())
file.close()
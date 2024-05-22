file =open("python.txt","r")
h=[]
for j in file:
    h.append(j)
print(h)
file.close()
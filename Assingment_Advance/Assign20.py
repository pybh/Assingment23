file =open("python.txt","r")
l=""
for f in file:
    l+=f
j=l.split()
n=input("enter The word : ")
count=0
for v in j:
    if v==n:
        count+=1
print(count)
file.close()

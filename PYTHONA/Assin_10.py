strr="hello world"
for i in strr:
    count=0
    for j in strr:
        if(j==i):
             count+=1
    print("count of characters '{}' is '{}'".format(i,count))
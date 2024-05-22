# 1. first method 

strr=["Anadimuktam","india","python"]
x=len("Anadimuktam")
tmp="india" + "python"
if(x > 0 ):
       print("len :",x)
else:
       print("len :",tmp)

#2. second method
def my_1(strr):                                             # return length of longest word
    for i in strr:
        if(len(i) > 8):
            x=len(i)
    return x
strr=["Anadimuktam","india","python"]
print(my_1(strr))  
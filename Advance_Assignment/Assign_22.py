# How to Define a Class in Python? What Is Self? Give An Example Of 
# A Python Class 

class demo:
     def my(self):#==> self is a parameter it is used in class to access a variable
          strr=(input("enter a name :"))
          strr1=(input("enter a surname :"))
          tmp=strr+" "+strr1
          print(tmp)
obj=demo()
obj.my()

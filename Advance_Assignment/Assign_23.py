# Write a Python class named Rectangle constructed by a length and 
# width and a method which will compute the area of a rectangle

# taking a class name Rectangel
class Rectangel:
    # define a function func
    def func(self,l,b):
        # taking values from the function
        self.l=l
        self.b=b
        # printing the values
        print("length : ",l)
        print("breadth : ",b)
        # define a function for the computation of area
    def func2(self):
        # printing the string or function
        print("area of Rectangle : ",self.l*self.b)

# object created of rct
obj=Rectangel()
# object called By . operator and passing values of the function
obj.func(10,20)
obj.func2() 

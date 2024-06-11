# Explain Inheritance in Python with an example? What is init? Or What 
# Is A Constructor In Python? 


# Explain Inheritance in Python with an example? What is init? Or What 
# Is A Constructor In Python? 

# inheritance Is Simply A heirarchy of class or Simply called realtion Between the Classes Or Simply The Concept of Heritance Ex you grandfather have propertt so it will give you to your father and after That it will given to you so this will also happens in the classes

# creating class of Car
class Car:
    # creating a function
    def func(self):
        # printing The String
        print("Xuv-700")
# creating class of Model and inheritate Car
class Model(Car):
    # creating a function
    def func2(self):
        # printing The String
        print("SUV")
# creating class of colour and inheritate Model  and Car    
class colour(Model,Car):
    # creating a function
    def Func3(self):
        # printing The String
        print("Black")

# now creating a object of colour because in colour the Model and Car inheritated
obj=colour()
# object called by .operator
obj.func()
obj.func2()
obj.Func3()
print()

# this are answer of the above theory question

# The Init is Simply A constructor Means It will execute When The Object is Created 


# The Constructor is Simply When there is a website started or at the start When The object Is Created it will started or executed 

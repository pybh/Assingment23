# Write a Python class named Circle constructed by a radius and two 
# methods which will compute the area and the perimeter of a circle

# taking a class name circle
class Circle:
    # creating a function for taking values from function
    def func(self,r):
        # taking value of passed value and printing the value
        self.r=r
        print("Radius : ",r)
        #  Now function for area
    def func2(self):
        # printing the formula and value 
        print("area of Circle : ",3.14*self.r*self.r)
        # now function for perimeter
    def func3(self):
        # printing the formula and value
        print("Perimeter of Circle : ",2*3.14*self.r)

# Now object of circle is created
obj=Circle()
# object called by .operator to print and get the area and perimeter of circle
obj.func(10)
obj.func2()
obj.func3()
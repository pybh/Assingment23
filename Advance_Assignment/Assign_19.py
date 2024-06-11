# How Do You Handle Exceptions With Try/Except/Finally In Python? 
# Explain with coding snippets. 

try:
    num=int(input("enter a number :"))
    print(num)
except ValueError:
    print("please enter only numeric value not a string")
finally:
    print("this block is executed !!!")
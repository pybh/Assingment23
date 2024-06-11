# Write python program that user to enter only odd numbers, else will 
# raise an exception. 

try:
    num=int(input("enter a number :"))
    if(num%2!=0):
      print("odd:",num)
    else:
       raise ValueError("please enter only odd number ")

except ValueError as e:
     print(e)
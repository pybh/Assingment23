try:
    num=int(input("enter a number :"))
    if(num%2!=0):
      print("odd:",num)
    else:
       raise ValueError("please enter only odd number ")
except ValueError as e:
     print(e)
    

    


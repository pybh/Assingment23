try:
    num=int(input("enter a number :"))
    print(num)
except ValueError:
    print("please enter only numeric value not a string")
finally:
    print("this block is executed !!!")
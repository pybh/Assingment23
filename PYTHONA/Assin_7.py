num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
num3=int(input("enter a number :"))
sum=num1+num2+num3
if(num1==num2) or (num2==num3) or (num1==num3):
    print(0) 
else:
    print("sum :",sum)

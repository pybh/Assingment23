num1=int(input("Enter a number :"))
num2=int(input("Enter a number :"))
def my(num1,num2):
    if(num1==num2) or abs (num1-num2)==5 or (num1+num2)==5:
        return True
    else:
        return False
print(my(num1,num2))

# return true if the two given integer values are equal or their sum or difference is 5
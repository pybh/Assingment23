while True : 
         menu=   """
                            WELCOME TO PYTHON BANK MANAGMENT SYSTEM 
         
         select your role

         1) Banker 
         2)Customer
         3)Exit

"""
         print(menu)
         choice=int(input("choose your role : "))
         if(choice==1):
                 print("Welecome to banker App ")
                 x="Operations Menu"
                 print(x.center(50))
                 tmp="""              
                 1) Add Customer
                 2) View Customer 
                 3) Search Customer 
                 4) View all Customer
                 5) Total Amount in Bank"""
                 print(tmp.center(50))
                
                 while True:
                   choice=int(input("Enter your operation which you perform :"))
                   if(choice==1):
                    Account_no=int(input("Enter Account no :"))
                    Customer_name=str(input("Enter Customer name :"))
                    Opening_balance=int(input("Enter opening balance :"))

                    Account_no1=int(input("Enter Account no :"))
                    Customer_name2=str(input("Enter Customer name :"))
                    Opening_balance3=int(input("Enter opening balance :"))
                    #file=open("As1.txt","x")
                    file=open("As1.txt","w")
                    file.write(Account_no)
                    file.write("\n")
                    file.write(Customer_name)
                    file.write("\n")
                    file.write(Opening_balance)
                    file.write("\n")
                    file.write(Account_no1)
                    file.write("\n")
                    file.write(Customer_name2)
                    file.write("\n")
                    file.write(Opening_balance3)
                    file.write("\n")
                    file.close()
                   elif(choice==2):
                     file=open("As1.txt","r")
                     for i in file:
                         print(i)
                   elif(choice==3):
                        str1=str(input("enter a customer name :"))
                        if str1=="bhagya" :
                            print("Account no :",Account_no)
                            print("Opening balance :",Opening_balance)
                        elif str1=="harsh":
                            print("Account no :",Account_no1)
                            print("Opening balance :",Opening_balance3)
                   elif(choice==4):
                         file=open("As1.txt","r")
                         for i in file:
                           print(i)
                   elif(choice==5):
                       str1=str(input("enter a customer name :"))
                       if str1=="bhagya" :
                           print("Opening balance :",Opening_balance)
                       elif str1=="harsh":
                           print("Opening balance :",Opening_balance3)
                       break
         elif(choice==2):
                   print("Welecome to customer App ")
                   x="Operations Menu"
                   print(x.center(50))
                   tmp="""              
                             1) Deposit Amount
                             2) Withdraw Amount 
                             3) View Balance1
                             
                          """
               
                   print(tmp.center(50))
                   while True:
                     choice=int(input("Enter your operation which you perform :"))
                     if(choice==1):
                       DepositAmount=int(input("enter a Deposit_Amount :"))
                    #file=open("As1.txt","x")
                       sum=Opening_balance+DepositAmount
                       print(sum)
                     elif(choice==2):
                       withdraw_Amount=int(input("enter a withdraw Amount :"))
                     
                       if(withdraw_Amount > sum):
                            print("please check you are enter more amount ")

                       elif(withdraw_Amount < sum):
                                sub=sum-withdraw_Amount
                                print(sub)
                     elif(choice==3):
                            print(sub)
                

        
                
                
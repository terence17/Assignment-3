class Account:
   def __init__(self, pin = 1234, balance = 1000): 
        self.balance = balance
        self.pin = pin
     
   def login(self):
       count = 0
       while count < 3:
           atm_pin = int(input("enter your pin to proceed: "))
           if atm_pin == self.pin :
               print("Welcome To Terrybank: ") 

               print("""Choose your transaction:
                    1. withdraw money
                    2. deposit
                    3. quit
                    \n
               """)

               option = int(input("Enter transaction: "))

               if option == 1:
                   print("Balance £", self.balance)
                   Withdraw = float(input("Enter Withdraw amount £"))
                   if Withdraw>self.balance:
                       print("Insufficient funds in account")
                   elif Withdraw>0:
                       forewardbalance=(self.balance-Withdraw)
                       print("£", Withdraw, "Withdrawn")
                       print("Current Balance: £",forewardbalance)
                   else:
                       print("None withdraw made")

               elif option == 2:
                   print("Balance £", self.balance)
                   Deposit=float(input("Enter deposit amount £ "))
                   if Deposit>0:
                       forewardbalance=(self.balance+Deposit)
                       print("Current balance £",forewardbalance)
                   else:
                       print("No deposit made")
                             
               elif option == 3:
                   quit_1 = input("type yes to quit! ")
                   if quit_1 == "yes":
                       print("quit")
                       break
                   else:
                       continue      
                       print("Choose any transaction: ")      
          
           else:
               print("wrong pin!, try again")
               count += 1    
    
   
        


a2 = Account()
a2.login()

    


    
        

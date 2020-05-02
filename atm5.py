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
                    3. mobile_money
                    4. quit
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
                   print("Welcome to mobile money, your balance is: ¢ ", self.balance)
                   print("""Choose option:
                    1. Cash in
                    2. Cash out
                    3. Check balance
                    4. Buy airtime
                    5. Transfer Money
                    \n
                   """)

                   MoMo_option = int(input("Choose option: "))

                   if MoMo_option == 1:
                       print("Balance ¢ ", self.balance)
                       Cash_in = float(input("Enter cash in amount ¢ "))
                       if Cash_in > 0:
                           Momo_balance=(self.balance + Cash_in)
                           count = 0
                           while count < 3:
                               atm_pin = int(input("enter your pin to proceed: "))
                               if atm_pin == self.pin :
                                   print("Current Balance: ¢ ",Momo_balance)
                                   break
                               else:
                                   print("wrong pin!, try again")
                                   count += 1
                       else:
                           print("No deposit made")

                   elif MoMo_option == 2:
                       Cash_out = input("Allow cash out: ")
                       if Cash_out == "yes":  
                           print("Balance ¢ ", self.balance)
                           Cash_out = float(input("Enter cash in amount ¢ "))
                           count = 0
                           while count < 3:
                               atm_pin = int(input("enter your pin to proceed: "))
                               if atm_pin == self.pin :
                                   if Cash_out > self.balance:
                                       print("Not enough funds to perform this transaction")
                                   elif Cash_out > 0:
                                       MoMo_balance=(self.balance - Cash_out)
                                       print("Cash out: ","¢" ,Cash_out)
                                       print("Current Balance: ¢",MoMo_balance)
                                       break
                               else:
                                   print("wrong pin!, try again")
                                   count += 1

                           else:
                                print("No cash out made")
                                   
                       else:
                           print("Cash out not allowed")
                   
                   elif MoMo_option == 3:
                       count = 0
                       while count < 3:
                           atm_pin = int(input("enter your pin to proceed: "))
                           if atm_pin == self.pin :
                               print("Balance ¢",self.balance)
                               break
                           else:
                               print("wrong pin!, try again")
                               count += 1
                           

                   elif MoMo_option == 4:
                       print("Balance ¢",self.balance)
                       Airtime = float(input("Enter Amount: ¢"))
                       count = 0
                       while count < 3:
                           atm_pin = int(input("enter your pin to proceed: "))
                           if atm_pin == self.pin :
                               break
                           else:
                                print("wrong pin!, try again")
                                count += 1

                       if Airtime > self.balance:
                           print("Not enough funds to perform transaction") 

                       elif Airtime > 0:
                           MoMo_balance = (self.balance - Airtime)
                           print("Payment of ¢", Airtime, "has been completed")
                           print("Your new balance: ¢",MoMo_balance)
                       else:
                           print("Invalid amount")
                                 
                   elif MoMo_option == 5:
                       print("Balance ¢ ", self.balance)
                       Transfer=float(input("Enter Amount to transfer: ¢"))
                       count = 0
                       while count < 3:
                           atm_pin = int(input("enter your pin to proceed: "))
                           if atm_pin == self.pin :
                               print("Balance ¢",self.balance)
                               break
                           else:
                               print("wrong pin!, try again")
                               count += 1
                               
                       if Transfer > self.balance:
                            print("Not enough funds to perform transaction")
                       elif Transfer > 0:
                            MoMo_balance=(self.balance-Transfer)
                            print("Transfer made to: +233240532745")
                            print("Current Balance: ","¢",MoMo_balance)
                       else:
                            print("No transfer made")
                            
                           
                   
           else:
               print("wrong pin!, try again")
               count += 1    
    
   
        


a2 = Account()
a2.login()

    


    
        

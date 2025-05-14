import sys
class Bank:
    BankName = "RBI BANK"
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def withdraw(self,amt):
        if self.balance<amt:
            print("insufficient balance not valid!!!")
            sys.exit()
        else:
            self.balance = self.balance - amt
            print("balance after withdraw = $",self.balance)
    def deposit(self,amt):
            self.balance = self.balance + amt
            print("balance after deposit = $",self.balance)
print("----------- WELCOME TO OUR",Bank.BankName,"------------")
name = input("Enter your Name : ")
b = Bank(name)
while True:
    print("D - Deposit\nW - Withdraw\n E - Exit\n")
    choice = input("Enter Your Choice : ")
    if choice == 'd' or choice == 'D':
        print("{} , your current balance = {}".format(name,b.balance))
        amt = float(input("Enter Amount to Deposit : "))
        b.deposit(amt)
    elif choice == 'w' or choice == 'W':
        amt = float(input("Enter Amount to withdraw : "))
        b.withdraw(amt)
    elif choice == 'e' or choice == 'E':
        print("Thanks For Visit Our Bank") 
        sys.exit()
    else:
        print("invalid Choice please re enter choice!!!")
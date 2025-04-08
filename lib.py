import random

uName = ""
uPass = ""
logged_in = []

class Account:
    count = 0
    accounts = []
    def __init__(self, name, password, accountnum):
        self.name = name
        self.password = password
        self.accountnum = accountnum
        self.balance = 0
        self.wHistory = []
        self.dHistory = []
        Account.count += 1

    @classmethod
    def ViewBalance(cls):
        print(f"Your current balance is Php {logged_in.balance}\n")
        return

    @classmethod
    def Deposit(cls):
        print("[Deposit]\n")
        try:
            d_amount = int(input("How much would you like to Deposit?\n"
                                 ": "))
        except:
            if not type(d_amount) is int:
                print("Error! Please enter a numerical value!")
        if d_amount <0:
            space()
            print("Transaction failed. What, you're trying to donate your money or something? This ain't charity, boy.  ")
        logged_in.balance = logged_in.balance + d_amount
        space()
        print("[Transaction Successful!]\n"
              f"Your current balance is Php {logged_in.balance}!\n")
        logged_in.dHistory.append(f"[You have deposited Php {d_amount}. Your balance is now Php {logged_in.balance}.]")

    @classmethod
    def Withdraw(cls):
        print("[Withdraw]\n")
        try:
            w_amount = int(input("How much would you like to Withdaw?\n"
                                 ": "))
        except:
            if not type(w_amount) is int:
                print("Error! Please enter a numerical value!")
            if w_amount > logged_in.balance:
                space()
                print("Transaction failed. Insufficient balance!\n")
                return
        if w_amount <0:
            space()
            print("Transaction failed. You tryna us now?\n")
        logged_in.balance = logged_in.balance - w_amount
        space()
        print("[Transaction Successful!]\n"
              f"Your current balance is Php {logged_in.balance}!\n")
        logged_in.wHistory.append(f"[You have withdrawn Php {w_amount}. Your remaining balance is {logged_in.balance}]")

    @classmethod
    def TransactionHistory(cls):
        print("[Transaction History]\n\n")
        print("[Deposits]")
        for deposit in logged_in.dHistory:
            print(deposit)
        print("\n[Withdrawals]")
        for withrawal in logged_in.wHistory:
            print(withrawal)
        input("Press enter to continue\n")
        space()

    @classmethod
    def Login(cls):
        global uName
        global uPass
        global logged_in

        print("[Log in]\n\n"
              'Enter "0" to cancel this action\n')
        uName = str(input("Username: "))

        if uName == "0":
            space()
            return 0
        uPass = str(input("Password: "))
        for account in cls.accounts:
            if account.name == uName and account.password == uPass:
                space()
                print("Login Successful!\n")
                logged_in = account
                return account
        space()
        print("Error! Wrong Userame or Password!\n")
        Account.Login()

    @classmethod
    def Test(cls):
        for account in cls.accounts:
            print(f"[Name: {account.name}]\n"
                  f"[Password: {account.password}]\n"
                  f"[Balance: {account.balance}]\n\n")


def AccountCreation():
    while True:
        print("[Account Creation!]\n\n"
              'Enter "0" to cancel this action.\n')
        fName = str(input("First Name: "))
        if fName == "0":
            return 0
        lName = str(input("Last Name: "))
        if lName == "0":
            return 0
        pass1 = str(input("Create Password: "))
        if pass1 == "0":
            return 0
        pass2 = str(input("Confirm Password: "))
        if pass2 == "0":
            return 0
        if pass1 != pass2:
            space()
            print("Error! Password do not match!")
            continue
        while True:
            accnum = random.randint(100000000, 999999999)
            if any(account.accountnum == accnum for account in Account.accounts):
                continue
            break
        name = fName + " " + lName
        new_account = Account(name, pass1, accnum)
        Account.accounts.append(new_account)
        space()
        print("Account creation successful!\n")
        break



def space():
    print("\n"*10)

admin = Account("admin", "1", 100000000)
Account.accounts.append(admin)
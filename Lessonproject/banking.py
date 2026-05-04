class bank:
    accounts = {} #kept a data inside this by using variable = {} MIGHT AS WELL USE DICTIONARY

    def __init__(self, name, acc_id, money):
         self.name = name
         self.acc_id = acc_id
         self.money = money
         bank.accounts[name.lower()] = self

    def deposit(self):
        target_name = input("Enter name to deposit: ").lower()
        target_account = bank.accounts.get(target_name)
        if target_account: # print the target_account variable 
            add_value = int(input("Enter balance to deposit: "))
            target_account.money += add_value
            print(f"\nThis is your final record\nName: {target_account.name}\nID: {target_account.acc_id}\nBalance: {target_account.money}")
            return 
        else:
            print("Account Not Found!!")

    def withdraw(self):
        target_name = input("Enter name to withdraw: ").lower()
        target_account = bank.accounts.get(target_name)
        if target_account: # print the target_account variable 
            take_value = int(input("Enter balance to withdraw: "))
            if target_account.money >= take_value:
                target_account.money -= take_value
                print(f"\nThis is your final record\nName: {target_account.name}\nID: {target_account.acc_id}\nBalance: {target_account.money}")
                return 
            else:
                print(f"Insufficient, you only have {target_account.money}!!")
        else:
            print("Account Not Found!!")

    def status(self):
        target_name = input("Enter name to check status: ").lower()
        # give a variable name(exp. target_account) for the bank.accounts.get(target_name)
        target_account = bank.accounts.get(target_name)
        if target_account: # print the target_account variable 
            print(f"Name: {target_account.name}\nID: {target_account.acc_id}\nBalance: {target_account.money}")
            return 
        else:
            print("Account Not Found!!")

banking = bank("Jason", 67, 100)
banking = bank("Jamal", 69, 100)
banking = bank("Jordan", 68, 100)
while True:
    display_choice = ["Deposit\t\t\t\t┃", 
                      "Withdraw\t\t\t\t┃",
                      "Status\t\t\t\t┃", 
                      "Exist [Q]\t\t\t\t┃"] # Box use this ┏  ┓ ┗ ┛ ━ ┃ ┣ ┫
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n┃ Type out following display to select  ┃\n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    for i, display in enumerate(display_choice, start=1):
        print(f"┃{i}. {display}")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    user_choice = input("Enter choice: ").lower()
    if user_choice == "deposit":
        banking.deposit()
    elif user_choice == "withdraw":
        banking.withdraw()
    elif user_choice == "status":
        banking.status()
    elif user_choice == "q":
        break
    else:
        print("Inavlid choice!!")
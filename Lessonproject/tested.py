import os
import json

class bank:
    def __init__(self): 
        self.file_path = "accs.json"
        self.accs = []

    def deposit(self, acc_name, acc_id, password, acc_balance):
        new_entry = {
                    "name": acc_name,
                    "id": acc_id,
                    "pass": password, 
                    "balance": acc_balance,
                    }
    
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.accs = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.accs = []
        else:
            self.accs = []

        self.accs.append(new_entry)

        try:
            with open(self.file_path, "w") as f:
                json.dump(self.accs, f, indent=4) 
            print(f"Account for {acc_name} saved successfully!")
        except IOError as e:
            print(f"Unable to write files! {e}")
    
    def withdraw(self):
        pass
    
    def administrator(self):
        try:
            user_choice = int(input("Enter choice:"))
            if user_choice == 1:
                new_entry = {
                    "name": acc_name,
                    "id": acc_id,
                    "pass": password,
                    "balance": acc_balance,
                    }
    
                if os.path.exists(self.file_path):
                    try:
                        with open(self.file_path, "r") as f:
                            self.accs = json.load(f)
                    except (json.JSONDecodeError, FileNotFoundError):
                        self.accs = []
                else:
                    self.accs = []

                self.accs.append(new_entry)

                try:
                    with open(self.file_path, "w") as f:
                        json.dump(self.accs, f, indent=4) 
                    print(f"Account for {acc_name} saved successfully!")
                except IOError as e:
                    print(f"Unable to write files! {e}")
            elif user_choice == 2:
                print("Type account ID and Name to remove account")

            else:
                print("Invalid input!")
        except ValueError:
            print("Key in numbers only!")

    def status(self):
        try:
            user_choice = int(input("Enter choice write or read?: "))
            if user_choice == 1:
                new_entry = {
                        "name": acc_name,
                        "id": acc_id,
                        "pass": password,
                        "balance": acc_balance,
                        }
                acc_name = input("Enter Account name:")
                acc_id = input("Enter Account_id:")
                password = input("Enter password:")
                acc_balance = input("Enter acc_balance:")

                with open("self.file_path", "w") as f: # open a file name with a variable like = file_path 
                    json.dump(new_entry, f, indent=4) #indent=4 so it make it easier for uesr to read

            elif user_choice == 2:
                pass

            else:
                print("Please enter only 1 - 2!!")
        except ValueError:
            print("Please enter a valid number!!")



bk = bank()
def menu_choice():
    while True:
        label = ["Check status\t\t\t\t┃",
                "Deposit\t\t\t\t\t┃",
                "Withdraw\t\t\t\t\t┃",
                "Exit \t\t\t\t\t┃",
                "Administrator\t\t\t\t┃"
                ] 
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")# Box use this ┏  ┓ ┗ ┛ ━ ┃ ┣ ┫
        print("┃   Press a number in the following to enter!   ┃\n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
        for i, labeled in enumerate(label, start= 1):
            print(f"┃{i}. {labeled}")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        try:
            user_choice = int(input("Enter number choice >> "))
            if user_choice == 1:
                bk.status
            elif user_choice == 2:
                #for i in new_entry:
                    bk.deposit(input("Enter account name: "), input("Enter account ID: "), 450)
            elif user_choice == 3:
                bk.withdraw
            elif user_choice == 4:
                break
            elif user_choice == 5:
                for i in range(1, 4, 1):
                    try:
                        password = int(input(f"Enter admin password >> "))
                        if password == 5201314:
                            print("Access granted!")
                            bk.administrator()
                            break
                        else:
                            if i == 3:
                                print("Access denied!!!")
                            else:
                                print(f"Attempt {i} failed. try again")
                    except ValueError:
                        print("Key in numbers only!")
            else:
                print("Invalid number input!")
        except ValueError:
            print("Please key in numbers only!")
 
if __name__ == "__main__":
    menu_choice()
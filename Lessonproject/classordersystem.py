class order_system:
    def __init__(self):
        self.person_name = [{"name": "Jason", "wallet": 100.0},
                            {"name": "Jamal", "wallet": 100.0},
                            {"name": "John", "wallet": 100.0}
                            ]

    def top_up(self, target_name, new_amount):
        for person in self.person_name:
            if person["name"].lower() == target_name.lower():
                person["wallet"] += new_amount
                print(f"Update complete! {target_name}'s wallet is now {person['wallet']}")
                print()
                return

    def buy_teh_tarik(self, target_name):

        for person in self.person_name:
            if person["wallet"] >= 2.5 and person["name"].lower() == target_name.lower(): 
                person["wallet"] -= 2.5
                print("Enjoy your drink!!\n")

            else:
                print("insufficient balance\n")
                return

    def show_status(self, target_name=None):

        if target_name == None:
            print("=========Name List=========")
            for person in self.person_name:  
                print(f"{person['name']}: RM {person['wallet']}")
        else:
            for target_person in self.person_name:
                if target_person["name"].lower() == target_name.lower():
                    print("\nFinal Search")
                    print(f"{target_name}: RM {target_person['wallet']}\n")
                    return

order = order_system()
def choice_1():
    while True:
        print("1. Topup\n2. Buy Teh Tarik\n3. Show Status\n4. Exist")
        user_choice = input("Enter choice: ")
        if user_choice == "1":
            order.top_up(input("Enter name: "), float(input("Enter amount: ")))
        elif user_choice == "2":
            order.buy_teh_tarik(input("Enter name to order: "))
        elif user_choice == "3":
            print("1. Show All detial\n2. Manual Search")
            user_choice = int(input("Enter choice: "))
            if user_choice == 1:
                order.show_status()
            elif user_choice == 2:
                order.show_status(input("Enter name: "))
            else:
                print("Key in number only 1-4!")

        elif user_choice == "4":
            print("Exiting...")
            break
        else:
            print("Key in number only 1-4!")
            break







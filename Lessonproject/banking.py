class bank:
    def __init__(self, name, acc_id):
         self.name = name
         self.acc_id = acc_id

    def deposit(self):
        print("YOU WON RM 1 Million")

    def withdraw(self):
        pass


banking = bank("Jason", 67)
banking.deposit()
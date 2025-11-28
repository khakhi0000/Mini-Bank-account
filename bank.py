# # Creating a mini bank account
#
# class BankAccount:
#     def __init__(self,name,balance=0):     #Constructor
#         self.name    = name
#         self.balance = balance
#
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"{amount} Added successfully! \nYour new balance is {self.balance}")
#
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient Balance!")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdrawn successfully! \nNew Balance: {self.balance}")
#
#     def display(self):
#         print(f"Account Holder: {self.name}")
#         print(f"Balance: {self.balance}")
#
# # Main program
#
# account = BankAccount(input("Enter your name: "))
#
#
# while True:
#     print("\n1:Deposit")
#     print("2:Withdraw ")
#     print("3:Check Balance")
#     print("4:Exit! ")
#
#     choice = input("Enter your choice(1-4): ")
#     if choice == '1':
#         amount = int(input("Enter deposit amount: "))
#         account.deposit(amount)
#     elif choice == '2':
#         amount = int(input("Enter withdraw amount: "))
#         account.withdraw(amount)
#     elif choice == '3':
#         account.display()
#     elif choice == '4':
#         print('Good bye Rajab')
#         break
#     else:
#         print("Invalid choice! ")
class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def verify_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                attempts -= 1
                print(f"Wrong PIN! Attempts left: {attempts}")

        print("❌ Too many wrong attempts! Withdrawal blocked.")
        return False

    def withdraw(self, amount):
        if self.verify_pin():
            if amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                print(f"Withdrawn: {amount}. New Balance: {self.balance}")

    def display(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Balance: {self.balance}\n")


# Main Program
name = input("Enter your name: ")
pin = input("Set your 4-digit PIN: ")
account = BankAccount(name, pin)

while True:
    print("\n===== BANK MENU =====")
    print("1: Deposit")
    print("2: Withdraw")
    print("3: Check Balance")
    print("4: Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Input!")


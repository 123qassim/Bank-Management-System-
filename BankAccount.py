
#create a parent class bank account which represents a bank account with its respective attributes
#create a deposit method that manages the deposit actions
#create a withdrawal method which manages withdrawal actions
#create a bank fees method that applies bank fees percentage of 5% on the balance in account
#create display method to display account details
#NB:ensure the parent class has at least 2 child classes


# import datetime
#
#
# class BankAccount:
#     def __init__(self, account_holder, account_number, password, balance=0.0):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.password = password
#         self.balance = balance
#         self.loan_balance = 0.0
#         self.loan_limit = 5000.0
#         self.loan_deadline = None
#         self.savings_balance = 0.0
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount:.2f}. New balance is: ${self.balance:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if amount > 0:
#             if self.balance >= amount:
#                 self.balance -= amount
#                 print(f"Withdrew ${amount:.2f}. New balance is: ${self.balance:.2f}")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Withdrawal amount must be positive.")
#
#     def apply_bank_fees(self):
#         fee = self.balance * 0.05
#         self.balance -= fee
#         print(f"Bank fee of 5% applied. Fee amount: ${fee:.2f}. New balance is: ${self.balance:.2f}")
#
#     def display_account_details(self):
#         print("\n--- Account Details ---")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Current Balance: ${self.balance:.2f}")
#         print(f"Loan Balance: ${self.loan_balance:.2f}")
#         print(f"Loan Deadline: {self.loan_deadline if self.loan_balance > 0 else 'No active loan'}")
#         print(f"Savings Balance: ${self.savings_balance:.2f}")
#         print("------------------------\n")
#
#     def check_password(self, input_password):
#         return self.password == input_password
#
#     def borrow_loan(self, amount):
#         if amount > 0:
#             if self.loan_balance + amount <= self.loan_limit:
#                 self.loan_balance += amount
#                 self.balance += amount
#                 self.loan_deadline = datetime.datetime.now() + datetime.timedelta(days=30)
#                 print(f"Loan of ${amount:.2f} borrowed. Loan balance: ${self.loan_balance:.2f}")
#                 print(f"New balance after loan: ${self.balance:.2f}")
#                 print(f"Loan repayment deadline: {self.loan_deadline.date()}")
#             else:
#                 print(f"Loan limit exceeded. You can borrow up to ${self.loan_limit - self.loan_balance:.2f} more.")
#         else:
#             print("Loan amount must be positive.")
#
#     def save_money(self, amount):
#         if amount > 0:
#             if self.balance >= amount:
#                 self.savings_balance += amount
#                 self.balance -= amount
#                 print(f"Saved ${amount:.2f}. Savings balance: ${self.savings_balance:.2f}")
#                 print(f"New balance after savings: ${self.balance:.2f}")
#             else:
#                 print("Insufficient funds to save.")
#         else:
#             print("Savings amount must be positive.")
#
#
# class SavingsAccount(BankAccount):
#     def __init__(self, account_holder, account_number, password, balance=0.0, interest_rate=0.02):
#         super().__init__(account_holder, account_number, password, balance)
#         self.interest_rate = interest_rate
#
#     def apply_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         print(
#             f"Interest of {self.interest_rate * 100}% applied. Interest amount: ${interest:.2f}. New balance is: ${self.balance:.2f}")
#
#
# class CheckingAccount(BankAccount):
#     def __init__(self, account_holder, account_number, password, balance=0.0, overdraft_limit=100.0):
#         super().__init__(account_holder, account_number, password, balance)
#         self.overdraft_limit = overdraft_limit
#
#     def withdraw(self, amount):
#         if amount > 0:
#             if self.balance + self.overdraft_limit >= amount:
#                 self.balance -= amount
#                 print(f"Withdrew ${amount:.2f}. New balance is: ${self.balance:.2f}")
#             else:
#                 print("Insufficient funds, even with overdraft.")
#         else:
#             print("Withdrawal amount must be positive.")
#
#
# # Main program
# def main():
#     print("Welcome to the Bank Account Management System!")
#
#     accounts = [
#         BankAccount("Charles Otaha", "12345678", "Otaha@03", 1000.0),
#         SavingsAccount("Cynthia Njeri", "87654321", "Njeri@03", 2000.0),
#         CheckingAccount("Qassim Juma", "13579111", "Juma@03", 500.0)
#     ]
#
#     account_number = input("Please enter your account number: ")
#
#     account = next((acc for acc in accounts if acc.account_number == account_number), None)
#
#     if account:
#         password = input("Please enter your account password: ")
#
#         if account.check_password(password):
#             # Successful login, show menu
#             while True:
#                 print("\nPlease choose an option:")
#                 print("1. Deposit")
#                 print("2. Withdraw")
#                 print("3. Apply Bank Fee")
#                 print("4. Display Account Details")
#                 print("5. Loan and Savings Options")
#                 print("6. Exit")
#
#                 choice = input("Enter your choice (1-6): ")
#
#                 if choice == "1":
#                     amount = float(input("Enter the amount to deposit: "))
#                     account.deposit(amount)
#
#                 elif choice == "2":
#                     amount = float(input("Enter the amount to withdraw: "))
#                     account.withdraw(amount)
#
#                 elif choice == "3":
#                     account.apply_bank_fees()
#
#                 elif choice == "4":
#                     account.display_account_details()
#
#                 elif choice == "5":
#                     print("\n--- Loan and Savings Options ---")
#                     print("1. Borrow Loan")
#                     print("2. Save Money")
#                     sub_choice = input("Enter your choice (1-2): ")
#
#                     if sub_choice == "1":
#                         amount = float(input("Enter the loan amount to borrow: "))
#                         account.borrow_loan(amount)
#                     elif sub_choice == "2":
#                         amount = float(input("Enter the amount to save: "))
#                         account.save_money(amount)
#                     else:
#                         print("Invalid choice. Please try again.")
#
#                 elif choice == "6":
#                     print("Thank you for using the Bank Account Management System. Goodbye!")
#                     break
#
#                 else:
#                     print("Invalid choice. Please try again.")
#         else:
#             print("Incorrect password. Access denied.")
#     else:
#         print("Account number not found. Please try again.")
#
#
# if __name__ == "__main__":
#     main()

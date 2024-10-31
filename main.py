class Student:
    first_name = "Annastacia"
    last_name = "Mutheu"
    gener = "Female"
    age = 24

class Person:
    def __init__(self,name,gender,marital_status,occupation):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation


# animal.py

class Animal:

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def info(self):
        return f"{self.name} is a {self.species} and is {self.age} years old."



class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def display_name(self):
        return f"{self.name} is {self.age} years old"


class Manager(Employee):
    def __init__(self, name, age, salary,gender, education_level):
        super().__init__(name,age,salary,gender)
        self.educational_level = education_level

class Developer(Employee):
    def __init__(self, name, age, salary,gender, prog_lang):
        super().__init__(name,age,salary,gender)
        self.prog_lang = prog_lang

class SalaryEmployee(Employee):
    def __init__(self, name, age, salary,gender, monthly_salary):
        super().__init__(name,age,salary,gender)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary + self.salary

class HoursEmployee(Employee):
    def __init__(self, name, age, salary,gender, hours_worked, hourly_rate):
        super().__init__(name,age,salary,gender)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payment(self):
        return (self.hours_worked * self.hourly_rate) + self.salary

class CommissionEmployee(SalaryEmployee):
    def __init__(self, name, age, salary, gender, monthly_salary, commission):
        super().__init__(name,age, salary, gender,monthly_salary,)
        self.commission = commission

    # def calculate_payroll(self):
    #     fixed = super()






#create a parent class bank account which represents a bank account with its respective attributes

# class BankAccount:
#     def __init__(self, account_holder, account_number, balance=0.0):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance
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
#     def display_balance(self):
#         print("\n--- Account Details ---")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Current Balance: ${self.balance:.2f}")



#create a parent class bank account which represents a bank account with its respective attributes
#create a deposit method that manages the deposit actions
#create a withdrawal method which manages withdrawal actions
#create a bank fees method that applies bank fees percentage of 5% on the balance in account
#create display method to display account details
#NB:ensure the parent class has at least 2 child classes




# class BankAccount:
#     def __init__(self, account_holder, account_number, balance=0.0):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance
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
#         # print("------------------------\n")
#
# # SavingsAccount
# class SavingsAccount(BankAccount):
#     def __init__(self, account_holder, account_number, balance=0.0, interest_rate=0.02):
#         super().__init__(account_holder, account_number, balance)
#         self.interest_rate = interest_rate
#
#     def apply_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         print(f"Interest of {self.interest_rate * 100}% applied. Interest amount: ${interest:.2f}. New balance is: ${self.balance:.2f}")
#
# # CheckingAccount
# class CheckingAccount(BankAccount):
#     def __init__(self, account_holder, account_number, balance=0.0, overdraft_limit=100.0):
#         super().__init__(account_holder, account_number, balance)
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




class Device:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Device Information:\nBrand: {self.brand}\nYear: {self.year}")


# Phone subclass that inherits from Device and adds specific phone attributes
class Phone(Device):
    def __init__(self, brand, year, model, operating_system):
        super().__init__(brand, year)
        self.model = model
        self.operating_system = operating_system

    def display_info(self):
        super().display_info()
        print(f"Model: {self.model}\nOperating System: {self.operating_system}")





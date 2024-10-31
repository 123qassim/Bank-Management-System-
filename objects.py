
from main import Student, Developer, Manager
from main import Person
from main import Animal
from main import Employee
from main import CommissionEmployee
from main import SalaryEmployee
from main import HoursEmployee
from main import Phone


student1 = Student()
print(student1.first_name)
print(student1.last_name)
print(student1.gener)
print(student1.age)

student2 = Student
print(student2.first_name)
print(student2.last_name)
print(student2.gener)
print(student2.age)

person1 = Person("Jane", "Female", "Single", "Pilot")
person2 = Person("Alex", "Male", "Married", "Nurse")
person3 = Person("June", "Female", "Divorced", "Driver")

print(person1.name)
print(person1.marital_status)
print(person1.gender)
print(f"Name: {person2.name}, Gender: {person2.gender}, Marital_status: {person2.marital_status}, Occupation: {person2.occupation}")

# create a class that enables instatiation(creating objects) of varieties of animals,
# create 4 objects(animals) from it

animal1 = Animal("Tiger", "Panthera tigris", 5)
animal2 = Animal("Giraffe", "Giraffa camelopardalis", 8)
animal3 = Animal("Kangaroo", "Macropus rufu", 3)
animal4 = Animal("Wolf", " Canis lupus", 2)

print(animal1.info())
print(animal2.info())
print(animal3.info())
print(animal4.info())


employee1 = Employee("jane", "23", "20000", "Female")
manager1 = Manager("Jones", "34", "20000","Female", "Doctorate")
developer1 = Developer("Patrick", "23", "20000", "Female", "Kotlin")
salaryemployee1 = SalaryEmployee("Victor", "25", "35000", "Female", "45000")
hoursemployee1 = HoursEmployee("John", "34", "55000", "Male", "4500", "1000")
commissionemployee = CommissionEmployee("Gillian", "21", "Male", "Male", "23000", "5%")


# print(manager1.display_name())
# print(developer1.display_name())
# print(salaryemployee1.display_name())
# print(hoursemployee1.display_name())
#
# print(salaryemployee1.calculate_salary())
# print(hoursemployee1.calculate_payment())

# print(commissionemployee.calculate_payroll())





#create a parent class bank account which represents a bank account with its respective attribute



#
# account1 = BankAccount("Alice Johnson", "12345678", 1000.0)
# account2 = BankAccount("Bob Smith", "87654321", 500.0)
# account3 = BankAccount("Charlie Brown", "13579135", 750.0)
# account4 = BankAccount("Diana Prince", "24682468", 1200.0)
#
# print(account1.deposit(250.0))
# print(account1.withdraw(100.0))
# print(account1.display_balance())
#
# print(account2.deposit(300.0))
# print(account2.withdraw(1000.0))
# print(account2.display_balance())
#
# print(account3.deposit(500.0))
# print(account3.withdraw(250.0))
# print(account3.display_balance())
#
# print(account4.deposit(100.0))
# print(account4.withdraw(150.0))
# print(account4.display_balance())





# account = BankAccount("Charles Otaha", "123F45G67E8", 10000.0)
# savings_account = SavingsAccount("Cynthia Njeri", "876S54B32Y1", 15000.0)
# checking_account = CheckingAccount("Ramlah Zainab", "13K57H91Z35", 5000.0)
#
# #  BankAccount
# print(account.deposit(2000.0))
# print(account.withdraw(1000.0))
# print(account.apply_bank_fees())
# print(account.display_account_details())
#
# #  SavingsAccount
# print(savings_account.deposit(5000.0))
# print(savings_account.withdraw(2000.0))
# print(savings_account.apply_interest())
# print(savings_account.apply_bank_fees())
# print(savings_account.display_account_details())
#
# # CheckingAccount
# print(checking_account.deposit(3000.0))
# # Overdraft Services
# print(checking_account.withdraw(9000.0))
# print(checking_account.apply_bank_fees())
# print(checking_account.display_account_details())



phone = Phone("Apple", 2020, "iPhone 12", "iOS")
print(phone.display_info())




# lists
employees = ['John', 'Smith', 'David', 'peter', '766']
print(employees)
print(employees[0])
print(employees[1])
print(employees[1:4])
employees[2] = 'Andrew'
print(employees)
employees.append('Susan')
print(employees)
employees.insert(2,'Joseph')
print(employees)
employees.extend(['Njue', 'Tom', 'Peter'])
print(employees)
# tuples
languages = ('Python', 'Java', 'Kotlin')
print(languages)
print(languages[1])
print(languages[1:4])
# languages[2] = 'Php'
print(languages)
marks = (234, 286, 564, 765)
print(marks)
print(max(marks))
print(min(marks))
print(sum(marks))
# sets
students = {'John', 'Ann', 'Carol', 'Jovial'}
print(students)
if 'John' in students:
    print('John is present in students')
else:
    print('Not present in students')
if 'Peter' in students:
    print('Peter is present in students')
else:
    print('Not present in students')
students.add('Vivian')
print(students)
students.update(['Dan', 'Alex'])
print(students)
students.remove('Dan')
print(students)
# dictionary
books = {
    'title': 'The Book',
    'author': 'Joe Doe',
    'publisher': 'Kenya institute',
    'year published': 2000
}
print(books)
print(books['publisher'])
books['cover_color'] = 'blue'
print(books)

if 'cover_color' in books:
    print(books['cover_color'])
else:
    print('Not present')



# Creating a dictionary with more than 5 items
furniture = {
    "tables": 10,
    "chairs": 15,
    "cupboards": 20,
    "stools": 25,
    "locker": 30,
    "beds": 35,
    "etc": 0
}
print(furniture)
item_to_check = "booked"
if item_to_check in furniture:
    print("'booked' exists in the dictionary with a value of [10].")
else:
    print("'booked' does not exist in the dictionary.")





# Taking  user inputs
input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
input3 = int(input("Enter the third number: "))
input4 = int(input("Enter the fourth number: "))

# Perform logical 'and' operation to compare if all inputs are even numbers
if input1 % 2 == 0 and input2 % 2 == 0 and input3 % 2 == 0 and input4 % 2 == 0:
    print("All inputs are even numbers.")
else:
    print("At least one of the inputs is an odd number.")



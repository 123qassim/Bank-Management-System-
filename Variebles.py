print("Hello Charles")
print(345)
# variables
age = 36
print(age)

mark = 67.2
print(mark)

name = "Charles"
print(name)

# data types
# integers
a = 23
# strings
b = "Please press any button to continue"
# float
c = 1.2
# boolean
is_male = True
is_female = False
# Input from user
first_name = input("What is your name? ")
print(first_name)

my_age = input("How old are you? ")
print(my_age)

weight = input("What is your weight? ")
print("Your weight is " + weight)
height = input("How tall are you? ")
print("Your height is " + height + " inches tall")
# type conversion
num1 = input("What is your first number? ")
num2 = input("What is your second number? ")
num3 = int(num1) + int(num2)
print("Total:" + str(num3))


weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI: weight (kg) / (height (m))^2
bmi = weight / (height ** 2)

# Display the result
print("Your BMI is: {:.2f}".format(bmi))

# Provide interpretation based on BMI categories
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")




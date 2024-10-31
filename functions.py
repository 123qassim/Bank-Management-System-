def add_numbers(num1, num2):
    result = num1 + num2
    print("The sum of {} and {} is: {}".format(num1, num2, result))

add_numbers(23, 27.5)


def add_numbers():
    try:
        # Prompt the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the sum
        result = num1 + num2

        # Display the result
        print("The sum of {} and {} is: {}".format(num1, num2, result))

        # Return the result
        return result

    except ValueError:
        print("Invalid input! Please enter numerical values.")


def multiply(num7, num8):
    multiplier = num7 * num8
    return multiplier

print(multiply(10,20))


def age_calc(current_age):
    new_age = current_age - 10
    return new_age

print(age_calc(21))

def school(name, age):
    if 5 <= age <= 10:
        return f"{name} you are {age} years old. You belong to lower primary"
    elif 10 <= age <= 15:
        return f"{name} you are {age} years old. You belong to upper primary"
    elif age > 15:
        return f"{name} you are {age} years old. You belong to senior primary"
    else:
        return f"{name} you are {age} years old, and you are underage"

print(school("joseph",13))
print(school("alex",9))
print(school("ann",4))



# FIND THE MAXIMUM NUMBER
def find_max(num4, num5, num6):
    maximum = max(num4, num5, num6)
    return maximum

num4 = float(input("Enter the first number: "))
num5 = float(input("Enter the second number: "))
num6 = float(input("Enter the third number: "))

# Display the maximum value
print("The maximum of the three numbers is:", find_max(num4, num5, num6))




 # SUM OF THE NUMBERS IN A LIST
def sum_list(numbers):
    total = sum(numbers)
    return total

numbers = [11, 22, 13, 41, 15]
print("The sum of the list is:", sum_list(numbers))



# PERSONALIZED GREETINGS
def greet(name):
    if name == "Alice":
        return f"Hello, {name}! Nice to see you again!"
    elif name == "Bob":
        return f"Hey, {name}! How have you been?"
    else:
        # General greeting for other names
        return f"Hello, {name}! Welcome to our program."

# Get name input from the user
user_name = input("Enter your name: ")

print(greet(user_name))


def greet(name):
    # Check if the name is Alice or Bob
    if name == "Alice":
        return f"Hello, {name}! Nice to see you again!"
    elif name == "Bob":
        return f"Hey, {name}! How have you been?"
    else:
        # General greeting for other names
        return f"Hello, {name}! Welcome to our program."

# Get name input from the user
user_name = input("Enter your name: ")

print(greet(user_name))




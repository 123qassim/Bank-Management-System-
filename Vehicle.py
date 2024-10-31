class Vehicle:
    def start(self):
        print("Vehicle is starting.")


# Car subclass that overrides the start method
class Car(Vehicle):
    def start(self):
        print("Car is starting with a roar!")


# Bike subclass that overrides the start method
class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a rev!")

if __name__ == "__main__":
    my_car = Car()
    my_bike = Bike()

    my_car.start()
    my_bike.start()



# class Vehicle:
#     def __init__(self, fuel_level=100, max_speed=120):
#         self.fuel_level = fuel_level
#         self.max_speed = max_speed
#         self.speed = 0
#         self.engine_status = False
#
#     def start(self):
#         if not self.engine_status:
#             self.engine_status = True
#             print(f"{self.__class__.__name__} engine has started.")
#         else:
#             print(f"{self.__class__.__name__} engine is already running.")
#
#     def stop(self):
#         if self.engine_status:
#             self.engine_status = False
#             self.speed = 0
#             print(f"{self.__class__.__name__} engine has stopped.")
#         else:
#             print(f"{self.__class__.__name__} engine is already off.")
#
#     def accelerate(self, increase_by):
#         if self.engine_status and self.fuel_level > 0:
#             self.speed += increase_by
#             if self.speed > self.max_speed:
#                 self.speed = self.max_speed
#             self.fuel_level -= increase_by * 0.1  # Fuel consumption model
#             print(f"{self.__class__.__name__} is accelerating. Current speed: {self.speed} km/h, Fuel level: {self.fuel_level:.2f}%")
#         elif not self.engine_status:
#             print("Start the engine first!")
#         else:
#             print("Not enough fuel to accelerate.")
#
#     def brake(self, decrease_by):
#         if self.speed > 0:
#             self.speed -= decrease_by
#             if self.speed < 0:
#                 self.speed = 0
#             print(f"{self.__class__.__name__} is braking. Current speed: {self.speed} km/h")
#         else:
#             print(f"{self.__class__.__name__} is already stopped.")
#
#     def refuel(self, amount):
#         if amount > 0:
#             self.fuel_level += amount
#             if self.fuel_level > 100:
#                 self.fuel_level = 100
#             print(f"{self.__class__.__name__} refueled. Fuel level: {self.fuel_level:.2f}%")
#         else:
#             print("Refuel amount must be positive.")
#
#
# # Car subclass with a unique acceleration style
# class Car(Vehicle):
#     def __init__(self, fuel_level=100, max_speed=180):
#         super().__init__(fuel_level, max_speed)
#
#     def start(self):
#         print("Starting the car with a push-button ignition...")
#         super().start()
#
#     def accelerate(self, increase_by):
#         if self.speed < self.max_speed * 0.8:  # Sports mode up to 80% max speed
#             increase_by *= 1.5  # Boost acceleration
#         super().accelerate(increase_by)
#
#
# # Bike subclass with its own acceleration style
# class Bike(Vehicle):
#     def __init__(self, fuel_level=100, max_speed=100):
#         super().__init__(fuel_level, max_speed)
#
#     def start(self):
#         print("Kick-starting the bike...")
#         super().start()
#
#     def accelerate(self, increase_by):
#         if self.speed < 30:  # Faster acceleration at low speeds
#             increase_by *= 1.2
#         super().accelerate(increase_by)
#
#
# # User interaction for choosing options
# def user_menu(vehicle):
#     while True:
#         print("\nPlease choose an option:")
#         print("1. Start the vehicle")
#         print("2. Stop the vehicle")
#         print("3. Accelerate")
#         print("4. Brake")
#         print("5. Refuel")
#         print("6. View vehicle status")
#         print("7. Exit")
#
#         choice = input("Enter your choice (1-7): ")
#
#         if choice == "1":
#             vehicle.start()
#         elif choice == "2":
#             vehicle.stop()
#         elif choice == "3":
#             amount = float(input("Enter the speed increase amount: "))
#             vehicle.accelerate(amount)
#         elif choice == "4":
#             amount = float(input("Enter the speed decrease amount: "))
#             vehicle.brake(amount)
#         elif choice == "5":
#             amount = float(input("Enter the refuel amount (0-100): "))
#             vehicle.refuel(amount)
#         elif choice == "6":
#             print(f"Vehicle status - Type: {vehicle.__class__.__name__}, Fuel Level: {vehicle.fuel_level}%, Current Speed: {vehicle.speed} km/h, Engine Status: {'On' if vehicle.engine_status else 'Off'}")
#         elif choice == "7":
#             print("Exiting the menu.")
#             break
#         else:
#             print("Invalid choice, please select a valid option.")
#
# if __name__ == "__main__":
#     print("Welcome! Please select the vehicle type:")
#     print("1. Car")
#     print("2. Bike")
#
#     vehicle_choice = input("Enter your choice (1 or 2): ")
#
#     if vehicle_choice == "1":
#         vehicle = Car()
#     elif vehicle_choice == "2":
#         vehicle = Bike()
#     else:
#         print("Invalid choice. Defaulting to Car.")
#         vehicle = Car()
#
#     # Run the user menu for interacting with the vehicle
#     user_menu(vehicle)

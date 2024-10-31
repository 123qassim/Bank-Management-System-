# Base Device class
# class Device:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
# # Phone subclass that inherits from Device and adds a model attribute
# class Phone(Device):
#     def __init__(self, brand, year, model):
#         super().__init__(brand, year)  # Calls the initializer of the parent Device class
#         self.model = model
#
# # Test the Phone class
# phone = Phone("Apple", 2020, "iPhone 12")
#
# # Print all attributes
# print("Brand:", phone.brand)
# print("Year:", phone.year)
# print("Model:", phone.model)




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


# Test the Phone class by creating an instance
phone = Phone("Apple", 2020, "iPhone 12", "iOS")

phone.display_info()

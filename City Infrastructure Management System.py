'''
Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

- Code Example: Provide a basic structure for the Vehicle class without methods.

    class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
- Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script showing the creation of Vehicle objects and updating their owners.


'''


# Task 1: Vehicle Registration System
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

# Creating vehicle instances
car1 = Vehicle(reg_num="ABC123", vehicle_type="Car", owner="Alice")
car2 = Vehicle(reg_num="XYZ789", vehicle_type="SUV", owner="Bob")

# Initial owner information
print(f"Car 1 owner: {car1.owner}")
print(f"Car 2 owner: {car2.owner}")

# Updating owners
car1.update_owner(new_owner="Carol")
car2.update_owner(new_owner="David")

# Updated owner information
print(f"Car 1 new owner: {car1.owner}")
print(f"Car 2 new owner: {car2.owner}")

'''
Task 2: Event Management System Enhancement

- Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

- Code Example: Basic Event class without participant tracking.

    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
'''

# Task 2: Event Management System Enhancement
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count

# Creating an event instance
my_event = Event(name="Conference", date="2024-08-01")

# Adding participants
my_event.add_participant()
my_event.add_participant()
my_event.add_participant()

# Retrieving participant count
print(f"Participant count for {my_event.name}: {my_event.get_participant_count()}")
# Expected Output: Participant count for Conference: 3
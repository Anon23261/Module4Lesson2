# Task 1: Vehicle Registration System
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        """Updates the owner of the vehicle."""
        self.owner = new_owner

# Task 2: Event Management System Enhancement
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count

    def add_participant(self):
        """Increments the participant count by one."""
        self.participant_count += 1

    def get_participant_count(self):
        """Returns the current participant count."""
        return self.participant_count

# Demonstration Code
# Task 1 Demo
vehicle1 = Vehicle("ABC123", "Car", "Alice")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Bob")

print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

vehicle1.update_owner("Charlie")
print("\nAfter updating the owner:")
print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")

# Task 2 Demo
event = Event("City Marathon", "2024-12-01")
event.add_participant()
event.add_participant()
event.add_participant()

print(f"\nEvent: {event.name} on {event.date}")
print(f"Current Participant Count: {event.get_participant_count()}")

City Infrastructure Management System
This project demonstrates the concepts of Object-Oriented Programming (OOP) in Python by simulating a City Infrastructure Management System. The system is organized into various components to manage different aspects of a city, such as vehicles and events. Each component is designed as a class, featuring methods that allow interaction with city data.

Project Structure
This project is divided into two primary tasks:

Task 1: Vehicle Registration System
Task 2: Event Management System Enhancement
Each task has its own class and methods to represent and manage city infrastructure elements.

Task 1: Vehicle Registration System
Objective
To manage city vehicle registrations by creating a Vehicle class with attributes for each vehicle’s details. A method is included to update the owner of a vehicle.

Class Details
Vehicle Class: Represents a vehicle with the following attributes:

registration_number: The vehicle's unique registration number.
type: The type of vehicle (e.g., Car, Motorcycle).
owner: The owner of the vehicle.
Methods:

update_owner(new_owner): Updates the vehicle's owner to new_owner.
Usage Example
# Create instances of Vehicle
vehicle1 = Vehicle("ABC123", "Car", "Alice")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Bob")

# Display initial owner details
print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Update the owner of vehicle1
vehicle1.update_owner("Charlie")
print("\nAfter updating the owner:")
print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")

Task 2: Event Management System Enhancement
Objective
To enhance an event management system by adding participant tracking. This includes methods to add participants and retrieve the participant count for each event.

Class Details
Event Class: Represents a city event with the following attributes:

name: The name of the event.
date: The event date.
participant_count: Tracks the number of participants (initialized to 0).
Methods:

add_participant(): Increments the participant count by one.
get_participant_count(): Retrieves the current participant count.
Usage Example
# Create an instance of Event
event = Event("City Marathon", "2024-12-01")

# Add participants
event.add_participant()
event.add_participant()
event.add_participant()

# Display the participant count
print(f"Event: {event.name} on {event.date}")
print(f"Current Participant Count: {event.get_participant_count()}")


Here's a sample README for your City Infrastructure Management System project. This README is designed to be clear and informative for anyone viewing your project on GitHub.

City Infrastructure Management System
This project demonstrates the concepts of Object-Oriented Programming (OOP) in Python by simulating a City Infrastructure Management System. The system is organized into various components to manage different aspects of a city, such as vehicles and events. Each component is designed as a class, featuring methods that allow interaction with city data.

Project Structure
This project is divided into two primary tasks:

Task 1: Vehicle Registration System
Task 2: Event Management System Enhancement
Each task has its own class and methods to represent and manage city infrastructure elements.

Task 1: Vehicle Registration System
Objective
To manage city vehicle registrations by creating a Vehicle class with attributes for each vehicle’s details. A method is included to update the owner of a vehicle.

Class Details
Vehicle Class: Represents a vehicle with the following attributes:

registration_number: The vehicle's unique registration number.
type: The type of vehicle (e.g., Car, Motorcycle).
owner: The owner of the vehicle.
Methods:

update_owner(new_owner): Updates the vehicle's owner to new_owner.
Usage Example
python
Copy code
# Create instances of Vehicle
vehicle1 = Vehicle("ABC123", "Car", "Alice")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Bob")

# Display initial owner details
print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Update the owner of vehicle1
vehicle1.update_owner("Charlie")
print("\nAfter updating the owner:")
print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
Task 2: Event Management System Enhancement
Objective
To enhance an event management system by adding participant tracking. This includes methods to add participants and retrieve the participant count for each event.

Class Details
Event Class: Represents a city event with the following attributes:

name: The name of the event.
date: The event date.
participant_count: Tracks the number of participants (initialized to 0).
Methods:

add_participant(): Increments the participant count by one.
get_participant_count(): Retrieves the current participant count.
Usage Example
python
Copy code
# Create an instance of Event
event = Event("City Marathon", "2024-12-01")

# Add participants
event.add_participant()
event.add_participant()
event.add_participant()

# Display the participant count
print(f"Event: {event.name} on {event.date}")
print(f"Current Participant Count: {event.get_participant_count()}")
Running the Code
To run the project code, ensure you have Python installed. Simply open the project file in your editor and execute it. The code will create instances of Vehicle and Event, demonstrating the features described above.

Expected Output
The expected output for each task is shown in the code examples above. This output will display initial details, updated owner information for Vehicle, and participant counts for Event.

Project Goals
This project is designed to:

Showcase fundamental OOP concepts like classes, objects, attributes, and methods.
Provide hands-on practice with managing class instances and methods in Python.
Simulate a simple city management system.

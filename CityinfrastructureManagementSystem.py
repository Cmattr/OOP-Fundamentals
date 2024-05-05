class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.registration_number = registration_number
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of the vehicle {self.type} has been updated to {new_owner}.")

car1 = Vehicle("000123", "Mazda RX-7", "Matt")
car2 = Vehicle("000456", "Ford GT40", "Bailey")

print(f"Original owner of the vehicle: {car1.owner}")
car1.update_owner("Jilianne")
print(f"New owner of the vehicle: {car1.owner}")

print(f"Original owner of the vehicle: {car2.owner}")
car2.update_owner("Everly")
print(f"New owner of the vehicle: {car2.owner}")


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_guest(self):
        self.participant_count += 1

    def get_count(self):
        return self.participant_count
    

new_event = Event("Auto Show", '10-01')
print(f"\nThe event of {new_event.name}\n on the date of {new_event.date}")

new_event.add_guest()
new_event.add_guest()

print(f"the number of guest is: {new_event.get_count()}")
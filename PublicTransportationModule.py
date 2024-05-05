class bus:
    city = 'city_name'
    fare = 2.50
    bus_nubmer = 1

    def __init__(self, route_number, passenger_capacity):
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return f'{self.route_number} in {self.city_name} with capacity for {self.passenger_capacity} passengers.'
    
bus.city_name = 'Louisville'
bus.base_fare = 3.00
bus.bus_number = 10

bus1 = bus("route-66", 20)

print(f"Bus: {bus.bus_number}, {bus1} \n Fare: ${bus.base_fare} ")
print()

counts_commute_week = [2, 2, 3, 2, 2, 4, 0]
total = 0
for count in counts_commute_week:
    total += count
print(total)

class Vehicle:
    def __init__(self, name, capacity):
        self.name = name

def copy_vehicle_names_bad(vehicles_blue, vehicles_green):
    for vehicle_blue, vehicle_green in zip(vehicles_blue, vehicles_green):
        vehicle_blue.name = vehicle_green.name
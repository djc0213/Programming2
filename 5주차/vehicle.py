class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_num_passengers = 0

    def is_full(self):
        return self.current_num_passengers == self.capacity
    
    def load(self, count):
        print(f'{count} passengers are trying to get on.')
        if self.is_full():
            print(f'{self.name} is full. Take next one.')
            return
        if self.current_num_passengers + count <= self.capacity:
            self.current_num_passengers += count
            print(f'{self.name} loaded {count} passengers.')
        else:
            loading_count = self.capacity - self.current_num_passengers
            self.current_num_passengers = self.capacity
            print(f'{self.name} loaded {loading_count} passengers.')
            print(f'{count - loading_count} passengers should take next one.')

    def __str__(self):
        return f'{self.name}: {self.current_num_passengers} / {self.capacity}'
    
class Bus(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.buzzer_status = False
    
    def press_buzzer(self):
        print('zzzzzzzz! Stopping at the next stop.')
        self.buzzer_status = True

    def unload(self, count):
        self.buzzer_status = False
        assert self.current_num_passengers > count
        self.current_num_passengers -= count
        print(f'{self.name} unloaded {count} passengers.')

    def buzzer_is_on(self):
        return self.buzzer_status
    
    def __str__(self):
        return super().__str__() + f', buzzer_status={self.buzzer_status}'
    
class Taxi(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.destination = 'not set'

    def set_destination(self):
        self.destination = input('destination?')

    def get_destination(self):
        return self.destination
    
    def load(self, count):
        super().load(count)
        self.set_destination()

    def __str__(self):
        return super().__str__() + f', destination={self.destination}'
    
    def unload(self):
        print(f'{self.name} unloading {self.current_num_passengers} passengers.')
        self.current_num_passengers = 0
        self.destination = 'not set'

if __name__ == '__main__':
    bus_272_1 = Bus('272_1234', 20)
    bus_272_2 = Bus('272_2345', 25)
    taxi_1 = Taxi('orange_taxi', 4)
    taxi_2 = Taxi('white_taxi', 4)
    bus_272_1.load(15)
    bus_272_1.press_buzzer()
    print(bus_272_1)
    bus_272_1.unload(5)
    print(bus_272_1)
    bus_272_1.load(20)
    print(bus_272_1)
    bus_272_1.unload(10)
    print(bus_272_1)
    taxi_1.load(5)
    print(taxi_1)
    taxi_1.unload()
    print(taxi_1)
    bus_272_2.load(10)
    bus_272_2.press_buzzer()
from animal import Animal, Manager, Zebra, Lion
import random
import os

def print_TODO(todo):
    print(f'<<<NOT IMPLEMENTED: {todo} >>>')

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.occupancy = [[False for _ in range(world_size)]
                          for _ in range(world_size)]
        print_TODO('get random empty coordinates')
        self.num_zebras = num_zebras
        self.num_lions = num_lions
        self.world_size = world_size
        self.zebras = [Zebra(0, 0) for _ in range(num_zebras)]
        self.lions = [Lion(0, 0) for _ in range(num_lions)]
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')
        self.manager = Manager(world_size=self.world_size, num_zebras=self.num_zebras, num_lions=self.num_lions)
        self.grid = self.manager.generate_grid()

    def display(self):
        os.system('cls')
        print(f'Clock: {self.timestep}')
        print(f'Zebras: {self.num_zebras}\nLions:{self.num_lions}')
        self.manager.display_grid(self.grid)
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def move_animals(self):
        for zebra in self.manager.zebras:
            zebra.move(self.grid)
        for lion in self.manager.lions:
            lion.move(self.grid)

    def breed_animals(self):
        for zebra in self.manager.zebras:
            zebra.increase_counters(self.grid)
            if zebra.breed_counter == zebra.BREED_INTERVAL:
                zebra.breed_counter = 0  # Reset the breed counter
                new_zebra = zebra.zebra_breed(self.grid)
                self.manager.zebras.append(new_zebra)



    def run(self, num_timesteps=100):
        os.system('cls')
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.move_animals()
            self.breed_animals()
            self.display()
 

if __name__ == '__main__':
    safari = CircleOfLife(7, 5, 2)
    safari.run(1000)

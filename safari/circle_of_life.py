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
        self.zebras = [Animal(0, 0) for _ in range(num_zebras)]
        self.lions = [Animal(0, 0) for _ in range(num_lions)]
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')
        self.manager = Manager(world_size=self.world_size, num_zebras=self.num_zebras, num_lions=self.num_lions)
        self.grid = self.manager.generate_grid()
       # Manager(world_size=self.world_size,num_zebras=self.num_zebras,num_lions=self.num_lions)
        #self.grid = Manager.generate_grid(self)
        
    def move_animal(self, animal_type, animal_index):
        if animal_type == 'Zebra':
            animals = self.zebras
            coords = self.zebras_coords
        elif animal_type == 'Lion':
            animals = self.lions
            coords = self.lions_coords
        else:
            return
        
        animal = animals[animal_index]
        x, y = coords[animal_index]
        new_x, new_y = self.get_random_neighbor(x, y)
        
        if self.is_valid_move(new_x, new_y):
            self.grid[x][y] = ' '
            self.grid[new_x][new_y] = animal_type[0]
            animal.x = new_x
            animal.y = new_y
            coords[animal_index] = (new_x, new_y)
    
    def get_random_neighbor(self, x, y):
        directions = [
            (x-1, y),   # Up
            (x+1, y),   # Down
            (x, y-1),   # Left
            (x, y+1)    # Right
        ]
        random.shuffle(directions)
        for neighbor_x, neighbor_y in directions:
            if self.is_valid_move(neighbor_x, neighbor_y):
                return neighbor_x, neighbor_y
        return x, y
    
    def is_valid_move(self, x, y):
        return 0 <= x < self.world_size and 0 <= y < self.world_size and self.grid[x][y] == ' '

    def display(self):
        os.system('cls')
        print(f'Clock: {self.timestep}')
        self.manager.display_grid(self.grid)
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()
        
    def step_breed(self):
        print_TODO('step_breed()')
        for animal in self.zebras + self.lions:
            print_TODO('get empty neighbor')
            x, y = 0, 0
            animal.breed(x, y)

    def run(self, num_timesteps=100):
        os.system('cls')
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.display()
            

if __name__ == '__main__':
    safari = CircleOfLife(20, 100, 2)
    safari.run(6)

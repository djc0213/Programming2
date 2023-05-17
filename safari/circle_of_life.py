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
        self.manager.display_grid(self.grid)
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()
        
    def step_breed(self):
        new_grid = [[' '] * self.world_size for _ in range(self.world_size)]  # Create a new empty grid

        # Move zebras
        for zebra in self.zebras:
            x, y = zebra.x, zebra.y
            zebra.move(self.grid)
            new_x, new_y = zebra.x, zebra.y
            new_grid[new_x][new_y] = 'Z'  # Update the new position in the new grid

        # Move lions
        for lion in self.lions:
            x, y = lion.x, lion.y
            lion.move(self.grid)
            new_x, new_y = lion.x, lion.y
            new_grid[new_x][new_y] = 'L'  # Update the new position in the new grid

        self.grid = new_grid  # Update the grid with the new positions

    def run(self, num_timesteps=100):
        os.system('cls')
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_breed()  # Move zebras and lions to new positions
            self.display()        

if __name__ == '__main__':
    safari = CircleOfLife(20, 10, 2)
    safari.run(20)
from animal import Animal, Manager,Zebra,Lion

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.manager = Manager(world_size, num_zebras, num_lions)
        self.grid = self.manager.generate_grid()
        self.zebras = [Zebra(x, y) for x in range(world_size) for y in range(world_size) if self.grid[x][y] == 'Z']
        self.lions = [Lion(x, y) for x in range(world_size) for y in range(world_size) if self.grid[x][y] == 'L']
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')

    def display(self):
        print(f'Clock: {self.timestep}')
        self.manager.display_grid(self.grid)
        key = input('Enter [q] to quit:')
        if key == 'q':
            exit()
    
    def step_move(self):
        for zebra in self.zebras:
            zebra.move(self.grid)
            self.grid[zebra.x][zebra.y] = 'Z'
        for lion in self.lions:
            lion.move(self.grid)
            self.grid[lion.x][lion.y] = 'L'

    def step_breed(self):
        for animal in self.zebras + self.lions:
            x, y = animal.x, animal.y
            new_animal = animal.breed(x, y)
            if new_animal:
                self.grid[x][y] = 'Z' if isinstance(new_animal, Zebra) else 'L'
                self.zebras.append(new_animal) if isinstance(new_animal, Zebra) else self.lions.append(new_animal)

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()

if __name__ == '__main__':
    safari = CircleOfLife(20, 100, 5)
    safari.run(2)

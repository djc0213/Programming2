import random

class Manager:
    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.num_zebras = num_zebras
        self.num_lions = num_lions
        self.animals = []

    def generate_animals(self):
        self.animals = []
        for _ in range(self.num_zebras):
            x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
            zebra = Zebra(x, y)
            self.animals.append(zebra)

        for _ in range(self.num_lions):
            x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
            lion = Lion(x, y)
            self.animals.append(lion)

    def move_animals(self):
        for animal in self.animals:
            animal.move(self.world_size)

    def display_grid(self):
        grid = [[' '] * self.world_size for _ in range(self.world_size)]

        for animal in self.animals:
            grid[animal.x][animal.y] = animal.symbol

        horizontal_line = '+' + '-' * (self.world_size * 3 - 1) + '+'
        print(horizontal_line)
        for row in grid:
            row_str = '| ' + ' | '.join(row) + ' |'
            print(row_str)
            print(horizontal_line)

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = ' '

    def move(self, world_size):
        directions = ['left', 'right', 'up', 'down']
        direction = random.choice(directions)

        if direction == 'left' and self.y > 0:
            self.y -= 1
        elif direction == 'right' and self.y < world_size - 1:
            self.y += 1
        elif direction == 'up' and self.x > 0:
            self.x -= 1
        elif direction == 'down' and self.x < world_size - 1:
            self.x += 1

class Zebra(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = 'Z'

class Lion(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = 'L'

# Create a Manager instance with a grid size of 10, 10 zebras, and 2 lions
manager = Manager(10, 10, 2)

# Generate the animals
manager.generate_animals()

# Display the initial grid
manager.display_grid()

# Move the animals
manager.move_animals()

# Display the updated grid
manager.display_grid()

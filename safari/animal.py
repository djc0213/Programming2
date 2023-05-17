import random

class Manager:
    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.num_zebras = num_zebras
        self.num_lions = num_lions
        self.zebras = []
        self.lions = []

    def generate_grid(self):
        grid = [[' '] * self.world_size for _ in range(self.world_size)]
        
        # Assign zebras to the grid
        zebra_count = min(self.num_zebras, self.world_size * self.world_size)
        zebra_symbols = random.sample(['Z'] * self.num_zebras, zebra_count)
        
        for zebra in zebra_symbols:
            x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
            while grid[x][y] != ' ':
                x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
            grid[x][y] = zebra
            self.zebras.append(Zebra(x,y))
        # Assign lions to the grid
        lion_count = min(self.num_lions, self.world_size * self.world_size - zebra_count)
        lion_symbols = random.sample(['L'] * self.num_lions, lion_count)
        
        for lion in lion_symbols:
            x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
            while grid[x][y] != ' ':
                x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
            grid[x][y] = lion
            self.lions.append(Lion(x,y))
        return grid

    def display_grid(self, grid):
        max_width = max(len(cell) for row in grid for cell in row)
        
        # Create the horizontal line
        horizontal_line = "+" + "+".join(["-" * (max_width + 2)] * len(grid[0])) + "+"

        print(horizontal_line)
        for row in grid:
            cells = [cell.center(max_width + 2) for cell in row]
            print("|" + "|".join(cells) + "|")
            print(horizontal_line)


class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0

    def move(self, grid):
        empty_neighbors = self.get_empty_neighbors(grid)
        if empty_neighbors:
            new_coordinate = empty_neighbors[random.randint(0,int(len(empty_neighbors)-1))]
            new_x = new_coordinate[0]
            new_y = new_coordinate[1]
            grid[self.x][self.y] = ' '  # Clear current cell 
            self.x = new_x
            self.y = new_y
            grid[self.x][self.y] = 'Z' if isinstance(self, Zebra) else 'L'

    def get_empty_neighbors(self, grid):
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # Right, Left, Down, Up, Diagonals
        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if self.is_valid_position(new_x, new_y, grid) and grid[new_x][new_y] == ' ':
                neighbors.append((new_x, new_y))
        return neighbors

    def is_valid_position(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])


    def breed (self, x, y):
        return Animal(x, y)
    
class Zebra(Animal):
    def breed(self, x, y):
        print('<<<NOT IMPLEMENTED>>>')


class Lion(Animal):
    def breed(self, x, y):
        print('<<<NOT IMPLEMENTED>>>')



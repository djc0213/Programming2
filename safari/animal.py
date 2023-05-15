import random

class Manager:
    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.num_zebras = num_zebras
        self.num_lions = num_lions

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
        
        # Assign lions to the grid
        lion_count = min(self.num_lions, self.world_size * self.world_size - zebra_count)
        lion_symbols = random.sample(['L'] * self.num_lions, lion_count)
        
        for lion in lion_symbols:
            x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
            while grid[x][y] != ' ':
                x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
            grid[x][y] = lion
        
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


# Define the grid size
#GRID_SIZE = 20

# Create a Manager instance with initial zebra count of 100 and initial lion count of 5
#manager = Manager(GRID_SIZE, 100, 5)

# Generate and display the grid
#grid = manager.generate_grid()
#manager.display_grid(grid)


# Display the updated grid
#print("\nAfter moving an animal:\n")
#manager.display_grid(grid)


class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
    
    def move(self, occupancy_grid):
        directions = ['left', 'right', 'up', 'down', 'diagonal_up_left', 'diagonal_up_right', 'diagonal_down_left', 'diagonal_down_right']
        direction = random.choice(directions)
        
        new_x, new_y = self.x, self.y

        if direction == 'left':
            new_y -= 1
        elif direction == 'right':
            new_y += 1
        elif direction == 'up':
            new_x -= 1
        elif direction == 'down':
            new_x += 1
        elif direction == 'diagonal_up_left':
            new_x -= 1
            new_y -= 1
        elif direction == 'diagonal_up_right':
            new_x -= 1
            new_y += 1
        elif direction == 'diagonal_down_left':
            new_x += 1
            new_y -= 1
        elif direction == 'diagonal_down_right':
            new_x += 1
            new_y += 1

        if 0 <= new_x < len(occupancy_grid) and 0 <= new_y < len(occupancy_grid[0]):
            self.x = new_x
            self.y = new_y


    def breed (self, x, y):
        return Animal(x, y)
    
class Zebra(Animal):
    def breed(self, x, y):
        print('<<<NOT IMPLEMENTED>>>')


class Lion(Animal):
    def breed(self, x, y):
        print('<<<NOT IMPLEMENTED>>>')
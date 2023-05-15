import random

class Manager:
    def __init__(self, size, num_animals):
        self.size = size
        self.num_animals = num_animals

    def generate_grid(self):
        grid = [[' '] * self.size for _ in range(self.size)]
        
        # Assign animals randomly to the grid
        animal_count = min(self.num_animals, self.size * self.size)
        animal_symbols = random.sample(ANIMALS, animal_count)
        
        for animal in animal_symbols:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            while grid[x][y] != ' ':
                x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            grid[x][y] = animal
        
        return grid

    def display_grid(self, grid):
        # Calculate the maximum symbol width in the grid
        max_symbol_width = max(len(cell) for row in grid for cell in row)
        
        # Create the horizontal line
        horizontal_line = "+" + "+".join(["-" * (max_symbol_width + 2)] * len(grid[0])) + "+"

        print(horizontal_line)
        for row in grid:
            cells = [cell.center(max_symbol_width + 2) for cell in row]
            print("|" + "|".join(cells) + "|")
            print(horizontal_line)

    def move_animal(self, grid, x1, y1, x2, y2):
        animal = grid[x1][y1]
        
        # Check if the target position is within the grid and empty
        if x2 >= 0 and x2 < self.size and y2 >= 0 and y2 < self.size and grid[x2][y2] == ' ':
            # Move the animal to the target position
            grid[x1][y1] = ' '
            grid[x2][y2] = animal
            return True
        
        return False

# Define the grid size
GRID_SIZE = 20

# Define the animal symbols
ANIMALS = ['L', 'Z', 'G', 'F', 'D', 'C', 'B', 'P', 'S', 'T']

# Create a Manager instance
manager = Manager(GRID_SIZE, len(ANIMALS))

# Generate and display the grid
grid = manager.generate_grid()
manager.display_grid(grid)

# Example: Move the animal at position (0, 0) to (2, 2)
manager.move_animal(grid, 0, 0, 2, 2)

# Display the updated grid
print("\nAfter moving an animal:\n")
manager.display_grid(grid)

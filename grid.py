import random

# Define the grid size
GRID_SIZE = 20

# Define the animal symbols
ANIMALS = ['L', 'Z', 'G', 'F', 'D', 'C', 'B', 'P', 'S', 'T']

def generate_grid(size, num_animals):
    grid = [[' '] * size for _ in range(size)]
    
    # Assign animals randomly to the grid
    animal_count = min(num_animals, size * size)
    animal_symbols = random.sample(ANIMALS, animal_count)
    
    for animal in animal_symbols:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        while grid[x][y] != ' ':
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[x][y] = animal
    
    return grid

def display_grid(grid):
    # Calculate the maximum symbol width in the grid
    max_symbol_width = max(len(cell) for row in grid for cell in row)
    
    # Create the horizontal line
    horizontal_line = "+" + "+".join(["-" * (max_symbol_width + 2)] * len(grid[0])) + "+"

    print(horizontal_line)
    for row in grid:
        cells = [cell.center(max_symbol_width + 2) for cell in row]
        print("|" + "|".join(cells) + "|")
        print(horizontal_line)

def move_animal(grid, x1, y1, x2, y2):
    animal = grid[x1][y1]
    
    # Check if the target position is within the grid and empty
    if x2 >= 0 and x2 < GRID_SIZE and y2 >= 0 and y2 < GRID_SIZE and grid[x2][y2] == ' ':
        # Move the animal to the target position
        grid[x1][y1] = ' '
        grid[x2][y2] = animal
        return True
    
    return False

# Calculate the number of animals based on the grid size
num_animals = min(len(ANIMALS), GRID_SIZE * GRID_SIZE)

# Generate and display the grid
grid = generate_grid(GRID_SIZE, num_animals)
display_grid(grid)

# Example: Move the animal at position (0, 0) to (2, 2)
move_animal(grid, 0, 0, 2, 2)

# Display the updated grid
print("\nAfter moving an animal:\n")
display_grid(grid)

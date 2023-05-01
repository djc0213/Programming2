def process(input_list):
    list1 = []
    for x in input_list:
        if x[0] == 4:
            list1.append(x)
    return list1

TYPE_INDICATOR = 0
GRASS = 4
def get_grass_cells(grid):
    grass_cells = []
    for cell in grid:
        if cell[TYPE_INDICATOR] == GRASS:
            grass_cells.append(cell)
    return grass_cells

class Cell:
    def __init__(self, species, count, age):
        self.species = species
        self.count = count
        self.age = age

def get_grass_cells_better(grid):
    grass_cells = []
    for cell in grid:
        if cell.species == 'grass':
            grass_cells.append(cell)
    return grass_cells
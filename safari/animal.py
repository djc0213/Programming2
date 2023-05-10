import pandas as pd

class Manager:
    def plot_dataframe(self):
        df = pd.DataFrame({"x": range(10), "y": range(10)})
        ax = df.plot(x="x", y="y", grid=True, color='gray')

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
    
    def move(self, direction):
        print(f'moving to {direction}. <<<NOT IMPLEMENTED YET >>>')

    def breed (self, x, y):
        return Animal(x, y)

class Zebra(Animal):
    def move(self,occupancy_grid):
        print('<<<NOT IMPLEMENTED>>>')

    def breed(self,x, y):
        print('<<<NOT IMPLEMENTED>>>')
        
class Lion(Animal):
    def move(self):
        print('<<< NOT IMPLEMENTED >>>')

manager = Manager()
manager.plot_dataframe()
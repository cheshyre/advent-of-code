from typing import Sequence


class PeriodicGrid:
    
    def __init__(self, grid_data: Sequence[str]):
        self.grid_data = grid_data
        if self.grid_data:
            self.grid_width = len(self.grid_data[0])
            self.grid_height = len(self.grid_data)
    
    def is_tree(self, x: int, y: int) -> bool:
        return self.grid_data[y % self.grid_height][x % self.grid_width] == "#"

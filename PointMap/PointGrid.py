"""
A PointGrid is a column of PointRows that are vertically aligned.
"""

from PointMap.PointRow import PointRow

class PointGrid:
  def __init__(self, start_x, start_y, cell_size, cells_per_row, rows_per_grid):
    self.grid = []
    current_y = start_y
    for i in range(0, rows_per_grid):
      self.grid.append(
        PointRow(start_x, current_y, cell_size, cells_per_row)
      )
      current_y += cell_size
    pass

  def render(self):
    for row in self.grid:
      row.render()
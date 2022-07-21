"""
A PointRow is a row of PointCells that are aligned horizontally.
"""
from PointMap.PointCell import PointCell

class PointRow:
  def __init__(
    self,
    start_x,
    start_y,
    cell_size,
    cells_per_row
  ):
    self.row = []
    current_x = start_x
    for i in range(0, cells_per_row):
      self.row.append(
        PointCell(current_x, start_y, cell_size)
      )
      current_x += cell_size

  def render(self):
    for cell in self.row:
      cell.render()

from Blob import Blob

class Player(Blob):
  def __init__(
    self,
    pos_x,
    pos_y,
    start_radius,
    color,
    speed
  ):
    super().__init__(
      pos_x,
      pos_y,
      start_radius,
      color
    )
    self.speed = speed 
  
  def update(self, mouse_pos):
    distance = self.pos.distance_to(mouse_pos)
    procentual = ((self.speed / distance) * 100) * 0.01
    if procentual > 0 and procentual < 1:
      self.pos.update(self.pos.lerp(mouse_pos, procentual))

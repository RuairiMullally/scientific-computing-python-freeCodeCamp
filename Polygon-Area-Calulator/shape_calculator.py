class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    string = f"Rectangle(width={self.width}, height={self.height})"
    return string

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perim = 2 * self.width + 2* self.height
    return perim

  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    
    if self.height > 50 or self.width > 50:
      return("Too big for picture.")
    else:
      masterstring = ''
      topbar = '*' * self.width +'\n'
      masterstring += topbar * self.height
      return masterstring

  def get_amount_inside(self, shape):
    amount = (self.width // shape.width) * (self.height // shape.height)
    return amount
    



class Square(Rectangle):
  def __init__(self, length):
    Rectangle.__init__(self, length, length)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, side):
    Rectangle.set_height(self, side)
    Rectangle.set_width(self, side)

  def set_width(self, side):
      Rectangle.set_height(self, side)
      Rectangle.set_width(self, side)
  
  def set_height(self, side):
      Rectangle.set_height(self, side)
      Rectangle.set_width(self, side)




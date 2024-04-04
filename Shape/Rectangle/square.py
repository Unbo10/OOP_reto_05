from os.path import dirname, realpath
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.Rectangle.rectangle import Rectangle
from Shape.Edge.vertex import Vertex

class Square(Rectangle):
   def __init__(self, *args) -> None:
      super().__init__(*args)
      self._perimeter = self._compute_perimeter()
      self._area = self._compute_area()
      # print(self.get_area())
      # print(self.get_perimeter())
   
   def _compute_perimeter(self) -> float:
      return round(self._edges[0].length * 4, 2)
   
   def _compute_area(self) -> float:
      return round(self._edges[0].length**2, 2)
   
def test_default() -> None:
   """Function to test the creation of a random square."""
   print("Square default test")
   vertices = [Vertex(0, 0), Vertex(0, 5), Vertex(5, 0), Vertex(5, 5)]
   square = Square(vertices)
   print("The square is regular:", square._is_regular)
   print("Vertices of the square: ", end = "")
   square.get_shape_vertices()
   print("Edges of the square: ", end = "")
   square.get_shape_edges()
   print("Inner angles of the square:", square.get_inner_angles())
   print("Perimeter of the square:", square._perimeter)
   print("Area of the square:", square._area)

def test_user_input() -> None:
   """Function to test the creation of a square with user input."""
   print("Square user input test")
   print("Enter the vertices of a square")
   x1 = float(input("Enter the x coordinate of the first vertex: "))
   y1 = float(input("Enter the y coordinate of the first vertex: "))
   x2 = float(input("Enter the x coordinate of the second vertex: "))
   y2 = float(input("Enter the y coordinate of the second vertex: "))
   x3 = float(input("Enter the x coordinate of the third vertex: "))
   y3 = float(input("Enter the y coordinate of the third vertex: "))
   x4 = float(input("Enter the x coordinate of the fourth vertex: "))
   y4 = float(input("Enter the y coordinate of the fourth vertex: "))
   vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3), Vertex(x4, y4)]
   square = Square(vertices)
   print("The square is regular:", square._is_regular)
   print("Vertices of the square: ", end = "")
   square.get_shape_vertices()
   print("Edges of the square: ", end = "")
   square.get_shape_edges()
   print("Inner angles of the square:", square.get_inner_angles())
   print("Perimeter of the square:", square._perimeter)
   print("Area of the square:", square._area)

if __name__ == "__main__":
   test_default()
   print()
   test_user_input()
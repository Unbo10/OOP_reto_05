from os.path import dirname, realpath
import math
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.Triangle.triangle import Triangle, NotTriangleError
from Shape.Edge.vertex import Vertex, enter_coordinate
from Shape.Edge.edge import Edge

class NotEquilateralError(NotTriangleError):
   def __init__(self, message="The vertices do not form an equilateral triangle") -> None:
      super().__init__(message)

class Equilateral(Triangle):
   def __init__(self, *args) -> None:
      super().__init__(*args)
      self._perimeter = self._compute_perimeter()
      self._area = self._compute_area()
      # print(self.get_area())
      # print(self.get_perimeter())
   
   def _compute_perimeter(self) -> float:
      return round(self._edges[0].length * 3, 2)

   def _compute_area(self) -> float:
      return round((math.sqrt(3)/4)*(self._edges[0].length**2), 2)
   
def test_default() -> None:
   """Function to test the creation of a random equilateral triangle."""
   print("Equilateral triangle default test")
   vertices = [Vertex(0, 0), Vertex(2, math.sqrt(12)), Vertex(4, 0)]
   equilateral = Equilateral(vertices)
   print("The equilateral triangle is regular:", equilateral._is_regular)
   print("Vertices of the equilateral triangle: ", end = "")
   equilateral.get_shape_vertices()
   print("Edges of the equilateral triangle: ", end = "")
   equilateral.get_shape_edges()
   print("Inner angles of the equilateral triangle:", equilateral.get_inner_angles())
   print("Perimeter of the equilateral triangle:", equilateral._perimeter)
   print("Area of the equilateral triangle:", equilateral._area)

def test_user_input() -> None:
   """Function to test the creation of an equilateral triangle with user input."""
   print("Equilateral triangle user input test")
   print("Warning: Any square root must be entered as a floating-point number with at least four (4) decimal places") 
   print("Enter the vertices of an equilateral triangle")
   e1: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
   e2: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
   e3: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
   length: float = 0
   valid_input: bool = False

   x1: float = enter_coordinate("x coordinate of the first vertex")
   y1: float = enter_coordinate("y coordinate of the first vertex")
   while valid_input == False:
      try:
         x2: float = enter_coordinate("x coordinate of the second vertex")
         y2: float = enter_coordinate("y coordinate of the second vertex")
         if ((x1 == x2) and (y1 == y2)):
            raise AssertionError
      except AssertionError:
         print("The vertices must be different")
      else:
         e1 = Edge(Vertex(x1, y1), Vertex(x2, y2))
         length = round(e1.length, 4)
         valid_input = True
   
   valid_input = False
   while valid_input == False:
      try:
         x3: float = enter_coordinate("x coordinate of the third vertex")
         y3: float = enter_coordinate("y coordinate of the third vertex")
         e2 = Edge(Vertex(x2, y2), Vertex(x3, y3))
         e3 = Edge(Vertex(x3, y3), Vertex(x1, y1))
         if (round(e2.length, 4) != length) or (round(e3.length, 4) != length):
            # print(length, round(e2.length, 4), round(e3.length, 4))
            raise NotEquilateralError
      except NotEquilateralError as e:
         print(e)
      else:
         valid_input = True

   vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3)]
   equilateral = Equilateral(vertices)
   print("The equilateral triangle is regular:", equilateral._is_regular)
   print("Vertices of the equilateral triangle: ", end = "")
   equilateral.get_shape_vertices()
   print("Edges of the equilateral triangle: ", end = "")
   equilateral.get_shape_edges()
   print("Inner angles of the equilateral triangle:", equilateral.get_inner_angles())
   print("Perimeter of the equilateral triangle:", equilateral._perimeter)
   print("Area of the equilateral triangle:", equilateral._area)

if __name__ == "__main__":
   try:
      test_default()
      print()
      test_user_input()
   except KeyboardInterrupt:
      print("\n\nProgram stopped by the user")
   finally:
      print("Thank you for using the program!", end="")
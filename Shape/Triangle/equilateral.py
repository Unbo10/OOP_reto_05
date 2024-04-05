from os.path import dirname, realpath
import math
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.Triangle.triangle import Triangle
from Shape.Edge.vertex import Vertex

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
   print("Warning: Any square root must be entered with at least four (4) decimal places") 
   print("Enter the vertices of an equilateral triangle")
   x1 = float(input("Enter the x coordinate of the first vertex: "))
   y1 = float(input("Enter the y coordinate of the first vertex: "))
   x2 = float(input("Enter the x coordinate of the second vertex: "))
   y2 = float(input("Enter the y coordinate of the second vertex: "))
   x3 = float(input("Enter the x coordinate of the third vertex: "))
   y3 = float(input("Enter the y coordinate of the third vertex: "))
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
   test_default()
   print()
   test_user_input()
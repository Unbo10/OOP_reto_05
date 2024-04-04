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

class Scalene(Triangle):
   def __init__(self, *args) -> None:
      super().__init__(*args)
      self._semi_perimeter = self._compute_semi_perimeter()
      self._perimeter = self._compute_perimeter() * 2
      self._area = self._compute_area()
      # print(self.get_area())
      # print(self.get_perimeter())

   def _compute_semi_perimeter(self) -> float:
      sum_of_edge_lengths = 0
      for i in self._edges:
         sum_of_edge_lengths += i.length
      return sum_of_edge_lengths / 2

   def _compute_area(self) -> float:
      """This method calculates the area of the triangle using Heron's formula"""

      return round(math.sqrt(self._semi_perimeter * (self._semi_perimeter - self._edges[0].length) * (self._semi_perimeter - self._edges[1].length) * (self._semi_perimeter - self._edges[2].length)), 2)

def test_default() -> None:
    """Function to test the creation of a random scalene triangle."""
    print("Scalene triangle default test")
    vertices = [Vertex(0, 0), Vertex(3, 0), Vertex(2, 3)]
    scalene = Scalene(vertices)
    print("The scalene triangle is regular:", scalene._is_regular)
    print("Vertices of the scalene triangle: ", end = "")
    scalene.get_shape_vertices()
    print("Edges of the scalene triangle: ", end = "")
    scalene.get_shape_edges()
    print("Inner angles of the scalene triangle:", scalene.get_inner_angles())
    print("Perimeter of the scalene triangle:", scalene._perimeter)
    print("Area of the scalene triangle:", scalene._area)

def test_user_input() -> None:
    """Function to test the creation of a scalene triangle with user input."""
    print("Scalene triangle user input test")
    print("Enter the vertices of an scalene triangle")
    x1 = float(input("Enter the x coordinate of the first vertex: "))
    y1 = float(input("Enter the y coordinate of the first vertex: "))
    x2 = float(input("Enter the x coordinate of the second vertex: "))
    y2 = float(input("Enter the y coordinate of the second vertex: "))
    x3 = float(input("Enter the x coordinate of the third vertex: "))
    y3 = float(input("Enter the y coordinate of the third vertex: "))
    vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3)]
    scalene = Scalene(vertices)
    print("The scalene triangle is regular:", scalene._is_regular)
    print("Vertices of the scalene triangle: ", end = "")
    scalene.get_shape_vertices()
    print("Edges of the scalene triangle: ", end = "")
    scalene.get_shape_edges()
    print("Inner angles of the scalene triangle:", scalene.get_inner_angles())
    print("Perimeter of the scalene triangle:", scalene._perimeter)
    print("Area of the scalene triangle:", scalene._area)

if __name__ == "__main__":
   test_default()
   print()
   test_user_input()
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

class RightTriangle(Triangle):
   def __init__(self, *args) -> None:
      super().__init__(*args)
      self._perimeter = self._compute_perimeter()
      self._area = self._compute_area()
      # print(self.get_area())
      # print(self.get_perimeter())

   def _compute_perimeter(self) -> float:
      return super()._compute_perimeter() # * No special way of doing it so it just adds the edges' lengths

   def _compute_area(self) -> float:
      self.edges = sorted(self._edges, key = lambda edge: edge.length) # * Guarantees the hypothenuse is the last edge, so the other two will be the legs (catetos)
      return round((self._edges[0].length * self._edges[1].length) / 2, 2)

def test_default() -> None:
    """Function to test the creation of a random right triangle."""
    print("Right triangle default test")
    vertices = [Vertex(0, 0), Vertex(3, 0), Vertex(0, 4)]
    right_triangle = RightTriangle(vertices)
    print("The right triangle is regular:", right_triangle._is_regular)
    print("Vertices of the right triangle: ", end = "")
    right_triangle.get_shape_vertices()
    print("Edges of the right triangle: ", end = "")
    right_triangle.get_shape_edges()
    print("Inner angles of the right triangle:", right_triangle.get_inner_angles())
    print("Perimeter of the right triangle:", right_triangle._perimeter)
    print("Area of the right triangle:", right_triangle._area)

def test_user_input() -> None:
    """Function to test the creation of a right triangle with user input."""
    print("Right triangle user input test")
    print("Enter the vertices of a right triangle")
    x1 = float(input("Enter the x coordinate of the first vertex: "))
    y1 = float(input("Enter the y coordinate of the first vertex: "))
    x2 = float(input("Enter the x coordinate of the second vertex: "))
    y2 = float(input("Enter the y coordinate of the second vertex: "))
    x3 = float(input("Enter the x coordinate of the third vertex: "))
    y3 = float(input("Enter the y coordinate of the third vertex: "))
    vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3)]
    right_triangle = RightTriangle(vertices)
    print("The right triangle is regular:", right_triangle._is_regular)
    print("Vertices of the right triangle: ", end = "")
    right_triangle.get_shape_vertices()
    print("Edges of the right triangle: ", end = "")
    right_triangle.get_shape_edges()
    print("Inner angles of the right triangle:", right_triangle.get_inner_angles())
    print("Perimeter of the right triangle:", right_triangle._perimeter)
    print("Area of the right triangle:", right_triangle._area)

if __name__ == "__main__":
   test_default()
   print()
   test_user_input()
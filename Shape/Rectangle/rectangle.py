from os.path import dirname, realpath
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.shape import Shape
from Shape.Edge.vertex import Vertex

class Rectangle(Shape):
   def __init__(self, *list_of_vertices) -> None:
      super().__init__(*list_of_vertices)
      self._ordered_edges = sorted(self._edges, key = lambda edge: edge.length) # * Guarantees the smallest pair of edges are the first two
      # self.get_shape_edges()
      self._perimeter = self._compute_perimeter()
      self._area = self._compute_area()

   def _compute_perimeter(self) -> float:
      return round((self._ordered_edges[0].length * 2) + (self._ordered_edges[2].length * 2), 2)

   def _compute_area(self) -> float:
      return round(self._ordered_edges[0].length * self._ordered_edges[2].length, 2)
   
def test_default() -> None:
   """Function to test the creation of a random rectangle."""
   print("Rectangle default test")
   vertices: list = [Vertex(0, 0), Vertex(0, 7), Vertex(5, 0), Vertex(5, 7)]
   rectangle = Rectangle(vertices)
   print("The rectangle is regular:", rectangle._is_regular)
   print("Vertices of the rectangle: ", end = "")
   rectangle.get_shape_vertices()
   print("Edges of the rectangle: ", end = "")
   rectangle.get_shape_edges()
   print("Inner angles of the rectangle:", rectangle.get_inner_angles())
   print("Perimeter of the rectangle:", rectangle._perimeter)
   print("Area of the rectangle:", rectangle._area)

def test_user_input() -> None:
   """Function to test the creation of a rectangle with user input."""
   print("Rectangle user input test")
   print("Enter the vertices of a rectangle")
   x1: float = float(input("Enter the x coordinate of the first vertex: "))
   y1: float = float(input("Enter the y coordinate of the first vertex: "))
   x2: float = float(input("Enter the x coordinate of the second vertex: "))
   y2: float = float(input("Enter the y coordinate of the second vertex: "))
   x3: float = float(input("Enter the x coordinate of the third vertex: "))
   y3: float = float(input("Enter the y coordinate of the third vertex: "))
   x4: float = float(input("Enter the x coordinate of the fourth vertex: "))
   y4: float = float(input("Enter the y coordinate of the fourth vertex: "))
   vertices: list = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3), Vertex(x4, y4)]
   rectangle = Rectangle(vertices)
   print("The rectangle is regular:", rectangle._is_regular)
   print("Vertices of the rectangle: ", end = "")
   rectangle.get_shape_vertices()
   print("Edges of the rectangle: ", end = "")
   rectangle.get_shape_edges()
   print("Inner angles of the rectangle:", rectangle.get_inner_angles())
   print("Perimeter of the rectangle:", rectangle._perimeter)
   print("Area of the rectangle:", rectangle._area)

if __name__ == "__main__":
   test_default()
   print()
   test_user_input()
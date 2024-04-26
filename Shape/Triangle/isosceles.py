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

class NotIsoscelesError(NotTriangleError):
   def __init__(self, message="The vertices do not form an isosceles triangle") -> None:
      super().__init__(message)

class Isosceles(Triangle):
   def __init__(self, *args) -> None:
      super().__init__(*args)
      self._base, self._equal_edges = self._compute_base_and_equal_edges()
      self._area = self._compute_area()
      self._perimeter = self._compute_perimeter()
      # print(self.get_area())
      # print(self.get_perimeter())
   
   def _compute_base_and_equal_edges(self) -> list:
      equal_pairs = sorted(self._edges, key = lambda edge: edge.length)
      base: Vertex = Vertex(0, 0)
      if equal_pairs[0].length != equal_pairs[1].length:
         base = equal_pairs[0]
         equal_pairs.remove(equal_pairs[0])
      else:
         base = equal_pairs[2]
         equal_pairs.remove(equal_pairs[2])
      return base, equal_pairs
   
   def _compute_area(self) -> float:
      height = math.sqrt((self._equal_edges[0].length**2) - ((self._base.length/2)**2))
      return round((self._base.length * height) / 2, 2)

   def _compute_perimeter(self) -> float:
      return round((self._equal_edges[0].length * 2) + self._base.length, 2)
     
def test_default() -> None:
   """Function to test the creation of a random isosceles triangle."""
   print("Isosceles default test")
   vertices = [Vertex(0, 0), Vertex(2, 2), Vertex(4, 0)]
   isosceles = Isosceles(vertices)
   print("The isosceles triangle is regular:", isosceles._is_regular)
   print("Vertices of the isosceles triangle: ", end = "")
   isosceles.get_shape_vertices()
   print("Edges of the isosceles triangle: ", end = "")
   isosceles.get_shape_edges()
   print("Inner angles of the isosceles triangle:", isosceles.get_inner_angles())
   print("Perimeter of the isosceles triangle:", isosceles._perimeter)
   print("Area of the isosceles triangle:", isosceles._area)

def test_user_input() -> None:
   """Function to test the creation of an isosceles triangle with user input."""
   print("Isosceles user input test")
   print("Enter the vertices of an isosceles triangle")
   valid_input: bool = False
   e1: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
   e2: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
   e3: Edge = Edge(Vertex(0, 0), Vertex(0, 0))

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
         e1: Edge = Edge(Vertex(x1, y1), Vertex(x2, y2))
         valid_input = True
   
   valid_input = False
   while valid_input == False:
      try:
         x3: float = enter_coordinate("x coordinate of the third vertex")
         y3: float = enter_coordinate("y coordinate of the third vertex")
         e2 = Edge(Vertex(x2, y2), Vertex(x3, y3))
         e3 = Edge(Vertex(x3, y3), Vertex(x1, y1))
         if (e1.length != e2.length) and (e1.length != e3.length) and (e2.length != e3.length):
            raise NotIsoscelesError
         elif (e1.slope == e2.slope) or (e1.slope == e3.slope) or (e2.slope == e3.slope):
            raise NotIsoscelesError
      except NotIsoscelesError as e:
         print(e)
      else:
         valid_input = True

   vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3)]
   isosceles = Isosceles(vertices)
   print("The isosceles triangle is regular:", isosceles._is_regular)
   print("Vertices of the isosceles triangle: ", end = "")
   isosceles.get_shape_vertices()
   print("Edges of the isosceles triangle: ", end = "")
   isosceles.get_shape_edges()
   print("Inner angles of the isosceles triangle:", isosceles.get_inner_angles())
   print("Perimeter of the isosceles triangle:", isosceles._perimeter)
   print("Area of the isosceles triangle:", isosceles._area)

if __name__ == "__main__":
   try:
      test_default()
      print()
      test_user_input()
   except KeyboardInterrupt:
      print("\n\nProgram stopped by the user")
   finally:
      print("Thank you for using the program!", end="")
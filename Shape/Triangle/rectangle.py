from os.path import dirname, realpath
import math
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.Triangle.triangle import Triangle
from Shape.Edge.vertex import Vertex, enter_coordinate
from Shape.Edge.edge import Edge

class NotRightTriangleError(Exception):
   def __init__(self, message="The vertices do not form a right triangle") -> None:
      super().__init__(message)

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
      temporary_edges: list = sorted(self._edges, key = lambda edge: edge.length) # * Guarantees the hypothenuse is the last edge, so the other two will be the legs (catetos)
      return round((temporary_edges[0].length * temporary_edges[1].length) / 2, 2)

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
   valid_input: bool = False
   e1: Edge = Edge(Vertex(0, 0), Vertex(0, 0))

   x1: float = enter_coordinate("x coordinate of the first vertex")
   y1: float = enter_coordinate("y coordinate of the first vertex")
   while valid_input == False:
      try:
         x2: float = enter_coordinate("x coordinate of the second vertex")
         y2: float = enter_coordinate("y coordinate of the second vertex")
         if ((x1 == x2) and (y1 == y2)):
            raise AssertionError
      except AssertionError:
         print("The second vertex cannot be the same as the first vertex")
      else:
         valid_input = True
   
   valid_input = False
   while valid_input == False:
      try:
         x3 = float(input("Enter the x coordinate of the third vertex: "))
         y3 = float(input("Enter the y coordinate of the third vertex: "))
         e1 = Edge(Vertex(x1, y1), Vertex(x2, y2))
         if ((x1 == x3) and (y1 == y3)) or ((x2 == x3) and (y2 == y3)):
            raise AssertionError
         elif (x1 == x2):
            if (y3 != y1) and (y3 != y2):
               raise NotRightTriangleError
         elif (y1 == y2):
            if (x3 != x1) and (x3 != x2):
               raise NotRightTriangleError
         else:
            e2 = Edge(Vertex(x2, y2), Vertex(x3, y3))
            e3 = Edge(Vertex(x3, y3), Vertex(x1, y1))
            if (e2.slope != 0 and e2.slope != None) or (e3.slope != 0 and e3.slope != None):
               raise NotRightTriangleError
      except AssertionError:
         print("The third vertex cannot be the same as any of the other two vertices")
      except NotRightTriangleError as e:
         print(e)
      else:
         valid_input = True

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
   try:
      test_default()
      print()
      test_user_input()
   except KeyboardInterrupt:
      print("\n\nProgram stopped by the user")
   finally:
      print("Thank you for using the program!", end="")
from os.path import dirname, realpath
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.shape import Shape
from Shape.Edge.vertex import Vertex, enter_coordinate
from Shape.Edge.edge import Edge

class NotStraightEdgeError(Exception):
   def __init__(self, message="The rectangle cannot be created because the vertex entered doesn't form a straight edge with the previous vertex") -> None:
      super().__init__(message)

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
   print("Enter the vertices of a rectangle in a clockwise manner")

   valid_input: bool = False
   v1: Vertex = Vertex(0, 0)
   v2: Vertex = Vertex(0, 0)
   v3: Vertex = Vertex(0, 0)
   v4: Vertex = Vertex(0, 0)

   x1: float = enter_coordinate("x coordinate of the first vertex")
   y1: float = enter_coordinate("y coordinate of the first vertex")
   v1 = Vertex(x1, y1)
   while valid_input == False:
      try:
         x2: float = enter_coordinate("x coordinate of the second vertex")
         y2: float = enter_coordinate("y coordinate of the second vertex")
         if (x1 == x2) and (y1 == y2):
            raise AssertionError
         elif (x1 != x2) and (y1 != y2):
            raise NotStraightEdgeError
      except AssertionError:
         print("The rectangle cannot be created because the vertices are the same")
      except NotStraightEdgeError as e:
         print(e)
      else:
         v2 = Vertex(x2, y2)
         valid_input = True
   
   valid_input = False
   while valid_input == False:
      try:
         x3: float = enter_coordinate("x coordinate of the third vertex")
         y3: float = enter_coordinate("y coordinate of the third vertex")
         if ((x2 == x3) and (y2 == y3)) or ((x1 == x3) and (y1 == y3)):
            raise AssertionError
         elif (x2 != x3) and (y2 != y3):
            raise NotStraightEdgeError
      except AssertionError:
         print("The rectangle cannot be created because the input matches a previous vertex")
      except NotStraightEdgeError as e:
         print(e)
      else:
         v3 = Vertex(x3, y3)
         valid_input = True
   
   valid_input = False
   while valid_input == False:
      try:
         x4: float = enter_coordinate("x coordinate of the fourth vertex")
         y4: float = enter_coordinate("y coordinate of the fourth vertex")
         v4 = Vertex(x4, y4)
         e2: Edge = Edge(v1, v4)
         e1: Edge = Edge(v3, v4)
         if ((x3 == x4) and (y3 == y4)) or ((x2 == x4) and (y2 == y4)) or ((x1 == x4) and (y1 == y4)):
            raise AssertionError
         elif ((e1.slope != None) and (e1.slope != 0)) or ((e2.slope != None) and (e2.slope != 0)):
            raise NotStraightEdgeError
      except AssertionError:
         print("The rectangle cannot be created because the input matches a previous vertex")
      except NotStraightEdgeError as e:
         print(e)
      else:
         valid_input = True

   vertices: list = [v1, v2, v3, v4]
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
   try:
      test_default()
      print()
      test_user_input()
   except KeyboardInterrupt:
      print("\n\nProgram stopped by the user", end="")
   finally:
      print("Thank you for using the program!")
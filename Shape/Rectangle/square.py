from os.path import dirname, realpath
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.Rectangle.rectangle import Rectangle
from Shape.Edge.vertex import Vertex, enter_coordinate
from Shape.Edge.edge import Edge

class NotSquareSide (Exception):
   def __init__(self, message="The vertices do not form a side of the square") -> None:
      super().__init__(message)

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
   print("Enter the vertices of a square in a way such that two consecutive vertices form a side of the square and not a diagonal")
   v1: Vertex = Vertex(0, 0)
   v2: Vertex = Vertex(0, 0)
   v3: Vertex = Vertex(0, 0)
   v4: Vertex = Vertex(0, 0)
   length: float = 0
   e1: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
   valid_input: bool = False

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
            raise NotSquareSide
      except AssertionError:
         print("The square cannot be created because the vertices are the same")
      except NotSquareSide as e:
         print(e)
      else:
         v2 = Vertex(x2, y2)
         e1 = Edge(Vertex(x1, y1), Vertex(x2, y2))
         length = e1.length
         valid_input = True
      
   valid_input = False
   while valid_input == False:
      try:
         x3: float = enter_coordinate("x coordinate of the third vertex")
         y3: float = enter_coordinate("y coordinate of the third vertex")
         e1 = Edge(Vertex(x2, y2), Vertex(x3, y3))
         if (x3 == x1) and (y3 == y1):
            raise AssertionError
         elif (e1.length != length):
            raise NotSquareSide
      except AssertionError:
         print("The square cannot be created because the vertices are the same")
      except NotSquareSide as e:
         print(e)
      else:
         v3 = Vertex(x3, y3)
         valid_input = True
   
   valid_input = False
   while valid_input == False:
      try:
         x4: float = enter_coordinate("x coordinate of the fourth vertex")
         y4: float = enter_coordinate("y coordinate of the fourth vertex")
         e1 = Edge(Vertex(x3, y3), Vertex(x4, y4))
         if ((x4 == x2) and (y4 == y2)) or ((x4 == x1) and (y4 == y1)) or ((x4 == x3) and (y4 == y3)):
            raise AssertionError
         elif (e1.length != length):
            raise NotSquareSide
      except AssertionError:
         print("The square cannot be created because the vertices are the same")
      except NotSquareSide as e:
         print(e)
      else:
         v4 = Vertex(x4, y4)
         valid_input = True

   vertices = [v1, v2, v3, v4]
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
   try:
      test_default()
      print()
      test_user_input()
   except KeyboardInterrupt:
      print("\n\nProgram stopped by the user", end="")
   finally:
      print("Thank you for using the program!")
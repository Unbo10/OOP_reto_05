from os.path import dirname, realpath
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.shape import Shape
from Shape.Edge.edge import Edge
from Shape.Edge.vertex import Vertex, enter_coordinate

class NotTriangleError(Exception):
   def __init__(self, *args) -> None:
      super().__init__(*args)

class Triangle(Shape):
   def __init__(self, *args) -> None:
      super().__init__(*args)
   
   def _create_vertices(self, vertices_giv) -> list:
      """Since triangles don't have diagonals, only edges need to be created (there is no need to check the order of the vertices therefore). Therefore, the method can be overriden to simply return the given vertices as they were submitted to the program."""
      return vertices_giv

   def _create_edges(self) -> list:
      """Method to create the edges of the triangle. Since the vertices' order doesn't matter, it creates the edges following the given order in the vertices list."""
      # * No need for a cycle really, since it will only create two of the three edges
      edges: list = []
      edges.append(Edge(self._vertices[0], self._vertices[1]))
      edges.append(Edge(self._vertices[1], self._vertices[2]))
      edges.append(Edge(self._vertices[2], self._vertices[0]))
      return edges
   
def test_default() -> None:
   """Function to test the creation of a random triangle."""
   print("Triangle default test")
   vertices = [Vertex(0, 0), Vertex(5, 8), Vertex(9, 2)]
   triangle = Triangle(vertices)
   print("The shape is regular:", triangle._is_regular)
   print("The vertices are: ", end="")
   triangle.get_shape_vertices()
   print("The edges are: ", end="")
   triangle.get_shape_edges()
   print("The inner angles are:", triangle.get_inner_angles())

def test_user_input() -> None:
   """Function to test the creation of a triangle with user input."""
   print("Triangle user input test")
   print("Enter the vertices of a triangle")
   e1: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
   e2: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
   valid_input: bool = False

   x1: float = float(input("x coordinate of the first vertex"))
   y1: float = float(input("y coordinate of the first vertex"))
   while valid_input == False:
      try:
         x2: float = float(input("x coordinate of the second vertex"))
         y2: float = float(input("y coordinate of the second vertex"))
         if ((x1 == x2) and (y1 == y2)):
            raise AssertionError
      except AssertionError:
         print("The second vertex cannot be the same as the first vertex")
      else:
         e1 = Edge(Vertex(x1, y1), Vertex(x2, y2))
         valid_input = True
   
   valid_input = False
   while valid_input == False:
      try:
         x3: float = float(input("x coordinate of the third vertex"))
         y3: float = float(input("y coordinate of the third vertex"))
         e2 = Edge(Vertex(x2, y2), Vertex(x3, y3))
         if (e1.slope == e2.slope):
            raise NotTriangleError("The vertices entered do not form a triangle")
      except NotTriangleError as e:
         print(e)
      else:
         valid_input = True

   vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3)]
   triangle = Triangle(vertices)
   print("The triangle is regular:", triangle._is_regular)
   print("The vertices are: ", end="")
   triangle.get_shape_vertices()
   print("The edges are: ", end="")
   triangle.get_shape_edges()
   print("The inner angles are:", triangle.get_inner_angles())

if __name__ == "__main__":
   try:
      test_default()
      print()
      test_user_input()
   except KeyboardInterrupt:
      print("\n\nProgram stopped by the user")
   finally:
      print("Thank you for using the program!", end="")
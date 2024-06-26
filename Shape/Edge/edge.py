from os.path import dirname, realpath
import sys
try:
   grandparent_dir = dirname(dirname(dirname(realpath(__file__))))
   sys.path.index(grandparent_dir)
except ValueError:
   sys.path.append(grandparent_dir)

from Shape.Edge.vertex import Vertex

class Edge: 
   def __init__(self, v1: Vertex, v2: Vertex) -> None:
      self.start = v2
      self.end = v1
      self.start = v1
      self.end = v2
      self.length = round(v1.calculate_vertex_distance(v2), 4)
      self.slope = self._compute_slope()
      self.vector_end: Vertex = Vertex(self.end.x - self.start.x, self.end.y - self.start.y) # * Vector from start to end
      self.vector_start: Vertex = Vertex(self.start.x - self.end.x, self.start.y - self.end.y) # * Vector from end to start

   def _compute_slope(self) -> float:
      if (self.end.x - self.start.x) == 0:
         return None
      else:
         return (self.end.y - self.start.y) / (self.end.x - self.start.x)
      
def test_default() -> None:
   """Function to test the creation of a random edge."""
   print("Edge default test")
   edge = Edge(Vertex(5, 5), Vertex(0, 0))
   print("Start vertex:", end = " ")
   edge.start.print_vertex_coordinates()
   print("End vertex:", end = " ")
   edge.end.print_vertex_coordinates()
   print("Length of the edge:", edge.length)
   print("Slope of the edge:", edge.slope)
   print("Vector from start to end:", end =" ")
   edge.vector_end.print_vertex_coordinates()
   print("Vector from end to start:", end =" ")
   edge.vector_start.print_vertex_coordinates()

def test_user_input() -> None:
   """Function to test the creation of an edge with user input."""
   print("Edge user input test")
   print("Enter the coordinates of the vertices of an edge")
   x1 = float(input("Enter the x coordinate of the first vertex: "))
   y1 = float(input("Enter the y coordinate of the first vertex: "))
   x2 = float(input("Enter the x coordinate of the second vertex: "))
   y2 = float(input("Enter the y coordinate of the second vertex: "))
   edge = Edge(Vertex(x1, y1), Vertex(x2, y2))
   print("Start vertex:", end = " ")
   edge.start.print_vertex_coordinates()
   print("End vertex:", end = " ")
   edge.end.print_vertex_coordinates()
   print("Length of the edge:", edge.length)
   print("Slope of the edge:", edge.slope)
   print("Vector from start to end:", end =" ")
   edge.vector_end.print_vertex_coordinates()
   print("Vector from end to start:", end =" ")
   edge.vector_start.print_vertex_coordinates()

if __name__ == "__main__":
   test_default()
   print()
   test_user_input()
import math

class Vertex:
   def __init__(self, given_x, given_y) -> None:
      self.x = given_x
      self.y = given_y
   
   def print_vertex_coordinates(self):
      print("(", end = "")
      print(self.x, end = "")
      print(", ", end = "")
      print(self.y, end = "")
      print(")")

   def calculate_vertex_distance (self, vert) -> float:
      return math.sqrt(((self.x - vert.x)**2) + ((self.y - vert.y)**2))
   
def test_default() -> None:
   """Function to test the creation of two random vertices and the distance between them."""
   print("Vertex default test")
   v1 = Vertex(0, 0)
   v2 = Vertex(3, 4)
   print("Vertex 1: ", end = "")
   v1.print_vertex_coordinates()
   print("Vertex 2: ", end = "")
   v2.print_vertex_coordinates()
   print("Distance between the vertices:", v1.calculate_vertex_distance(v2))

def test_user_input() -> None:
   """Function to test the creation of two vertices with user input and the distance between them."""
   print("Vertex user input test")
   print("Enter the coordinates of two vertices")
   x1 = float(input("Enter the x coordinate of the first vertex: "))
   y1 = float(input("Enter the y coordinate of the first vertex: "))
   x2 = float(input("Enter the x coordinate of the second vertex: "))
   y2 = float(input("Enter the y coordinate of the second vertex: "))
   v1 = Vertex(x1, y1)
   v2 = Vertex(x2, y2)
   print("Vertex 1: ", end = "")
   v1.print_vertex_coordinates()
   print("Vertex 2: ", end = "")
   v2.print_vertex_coordinates()
   print("Distance between the vertices:", v1.calculate_vertex_distance(v2))

if __name__ == "__main__":
   test_default()
   print()
   test_user_input()
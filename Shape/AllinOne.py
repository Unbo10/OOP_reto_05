import math # Built-in module
class Vertex:
   def __init__(self, given_x, given_y) -> None:
      self.x = given_x
      self.y = given_y
   
   def calculate_vertex_distance (self, vert) -> float:
      return math.sqrt(((self.x - vert.x)**2) + ((self.y - vert.y)**2))
   
class Edge: 
   def __init__(self, v1: Vertex, v2: Vertex) -> None:
      self.start = v1
      self.end = v2
      self.length = v1.calculate_vertex_distance(v2)
      self.slope = self._compute_slope()
      self.vector_end: Vertex = Vertex(v2.x - v1.x, v2.y - v1.y)
      self.vector_start: Vertex = Vertex(v1.x - v2.x, v1.y - v2.y)

   def _compute_slope(self) -> float:
      if (self.end.x - self.start.x) == 0:
         return None
      else:
         return (self.end.y - self.start.y) / (self.end.x - self.start.x)

class Shape:
   def __init__(self, list_of_vertices) -> None:
      # * It was not done using args to be able to pass a list of vertices as a parameter and not only individual vertices
      self._n_sides: int = len(list_of_vertices)
      self._vertices: list = self._create_vertices(list_of_vertices)
      # self.get_shape_vertices()
      self._edges: list = self._create_edges()
      # self.get_shape_edges()
      self._inner_angles: list = self._compute_inner_angles()
      self._is_regular: bool = self._is_shape_regular()
      self._area: float = None
      self._perimeter: float = None

   def _eliminate_repeated_vertices(self, vertices_giv) -> list:
      """Method to remove vertices with the same x and same y coordinates"""

      count = 0
      for k in vertices_giv:
         count = 0
         for j in vertices_giv:
               if (k.x == j.x) and (k.y == j.y):
                  count += 1
               if count > 1:
                  vertices_giv.remove(j)
                  count -= 1

      return vertices_giv
   
   def _sort_not_passed_vertices(self, m: Vertex, vertices_giv: list, passed: str) -> list:
      """Method to sort the vertices that have not been passed yet, that is, that have not been sorted yet. This is done to avoid positioning a vertex as the following of another vertex although is not the immediately following one."""

      m_pos = vertices_giv.index(m) # * Position of last min or max
      i = m_pos + 1
      if passed == "max_y":
         while i < len(vertices_giv):
            j = i + 1
            while j < len(vertices_giv):
               if vertices_giv[i].x < vertices_giv[j].x:
                  vertices_giv[i], vertices_giv[j] = vertices_giv[j], vertices_giv[i]
               elif (vertices_giv[i].x == vertices_giv[j].x) and (vertices_giv[j].y > vertices_giv[i].y):
                  vertices_giv[i], vertices_giv[j] = vertices_giv[j], vertices_giv[i]
               j += 1
            i += 1

      if passed == "max_x":
         while i < len(vertices_giv):
            j = i + 1
            while j < len(vertices_giv):
               if vertices_giv[i].x < vertices_giv[j].x:
                  vertices_giv[i], vertices_giv[j] = vertices_giv[j], vertices_giv[i]
               elif (vertices_giv[i].x == vertices_giv[j].x) and (vertices_giv[j].y < vertices_giv[i].y):
                  vertices_giv[i], vertices_giv[j] = vertices_giv[j], vertices_giv[i]
               j += 1
            i += 1

      if passed == "min_y":
         while i < len(vertices_giv):
            j = i + 1
            while j < len(vertices_giv):
               if vertices_giv[i].x < vertices_giv[j].x:
                  vertices_giv[i], vertices_giv[j] = vertices_giv[j], vertices_giv[i]
               elif (vertices_giv[i].x == vertices_giv[j].x) and (vertices_giv[j].y > vertices_giv[i].y):
                  vertices_giv[i], vertices_giv[j] = vertices_giv[j], vertices_giv[i]
               j += 1
            i += 1
      return vertices_giv

   def _get_max_and_min_vertices(self, vertices_giv: list) -> list:
      """The following block of code defines the min_y and max_y vertices, which will be, respectively, the bottom and top vertices of the shape. However, since there could be same-y coordinate vertices, there may be two top and/or bottom vertices. Therefore, those are grouped into two different list that are candidates for bottom and top vertices, and the list is then sorted according to the x coordinate of the vertices, and, taking into account the shape is being built clockwise, the top one should be the one with the smallest x coordinate and the bottom should have the biggest x coordinate among the candidates. An analogous process is done for the right-most and left-most vertices, with a variation on the condition to check: same y-coordinate."""

      vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.y)
      min_y_candidates: list = []
      max_y_candidates: list = []
      min_y_candidates.append(vertices_giv[0])
      max_y_candidates.append(vertices_giv[len(vertices_giv) - 1])
      i = 0
      for i in vertices_giv:
         if (i.y == min_y_candidates[0].y) and (i.x != min_y_candidates[0].x):
            min_y_candidates.append(i)
         if (i.y == max_y_candidates[0].y) and (i.x != max_y_candidates[0].x):
            max_y_candidates.append(i)

      min_y_candidates = sorted(min_y_candidates, key = lambda vertex: vertex.x)
      max_y_candidates = sorted(max_y_candidates, key = lambda vertex: vertex.x)
      min_y: Vertex = min_y_candidates[len(min_y_candidates) - 1]
      max_y: Vertex = max_y_candidates[0]

      # * An analogous process is done for the right-most and left-most vertices.
      vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.x)
      min_x_candidates: list = []
      max_x_candidates: list = []
      min_x_candidates.append(vertices_giv[0])
      max_x_candidates.append(vertices_giv[len(vertices_giv) - 1])
      for i in vertices_giv:
         if (i.x == min_x_candidates[0].x) and (i.y != min_x_candidates[0].y):
            min_x_candidates.append(i)
         if (i.x == max_x_candidates[0].x) and (i.y != max_x_candidates[0].y):
            max_x_candidates.append(i)

      min_x_candidates = sorted(min_x_candidates, key = lambda vertex: vertex.y)
      max_x_candidates = sorted(max_x_candidates, key = lambda vertex: vertex.y)
      min_x: Vertex = min_x_candidates[0]
      max_x: Vertex = max_x_candidates[len(max_x_candidates) - 1]
      # print("min_y:", min_y.x, min_y.y, "max_y:", max_y.x, max_y.y)
      # print("min_x: ", min_x.x, min_x.y, "max_x: ", max_x.x, max_x.y)

      return min_y, max_y, min_x, max_x

   def _create_vertices(self, vertices_giv) -> list:
      """This method is responsible for creating a clockwise list of the vertices of the shape. It does so by checking which conditions the vertices of a previously ordered and optimized (no repeated vertices) list of vertices fulfill. This will vary depending on the current outermost vertex from the center of the shape (left-most, right-most, top-most or bottom-most). The method will then sort the vertices so that the following one is the closest to the current vertex."""
      """Analogy: This system as a whole can be seen as a clock: imagine a convex shape. Although it can be as irregular as you want, it is an approximation of a circle, somewhat, right? Now, its vertices can be seen as different times the clock gives when its hands start to move clockwise. What the method does is it makes sure the usual times are set on the right place, for example, you don't want to see you just had lunch and it's 5:00 an hour later, right? To do this, it first sets the 12:00, 3:00, 6:00 and 9:00 times to have a reference of where the other times (vertices) are. Then, it just looks at the time at a certain position and compares it with the following reference (the current or already passed is 12:00 to start), so as to avoid misplacing times (vertices), and determines if there is any other time further in the past than the reference in the whole clock. If so, it swaps the times (vertices) so that the time (vertex) that is further in the past is the following one. It does this for all times (vertices) in the clock (shape) until it reaches the 12:00 time (vertex) again."""

      vertices_giv = self._eliminate_repeated_vertices(vertices_giv)
      vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.x)
      min_y, max_y, min_x, max_x = self._get_max_and_min_vertices(vertices_giv)
      passed: int = 0 
      # * There will be four conditions to pass: top (max_y), right (max_x), bottom (min_y) and left (one vertex before min_x).
      i: int = 0
      j: int = 0
      following_found: bool = False
      # * The following vertex will be the one that fulfills certain conditions depending on the current vertex and the passed condition. That way, the vertices will be sorted in a clockwise manner.

      # self._vertices = vertices_giv
      # self.get_shape_vertices() 
      while passed != 4:
         if passed == 0:
            # * The first vertex to be passed is the one with the maximum y coordinate
            while (passed == 0):
               if vertices_giv[i] == max_y:
                  passed += 1
               else:
                  j = i + 1
                  following_found = False
                  while following_found == False:
                     if vertices_giv[j] == max_y:
                        following_found = True
                        vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                        i += 1
                     elif (vertices_giv[j].y > vertices_giv[i].y) and (vertices_giv[j].x >= vertices_giv[i].x):
                        # * the first condition tested in all cases needs to be strictly greater or smaller so the shape is convex
                        vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                        following_found = True
                        i += 1
                        j = i + 1                            
                     else:
                           j += 1

         elif passed == 1:
            # * The second vertex to be passed is the one with the maximum x coordinate
            vertices_giv = self._sort_not_passed_vertices(max_y, vertices_giv, "max_y")
            while (passed == 1):
               if vertices_giv[i] == max_x:
                  passed += 1
               else:
                  j = i + 1
                  following_found = False
                  while following_found == False:
                     if vertices_giv[j] == max_x:
                        following_found = True
                        vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                        i += 1
                     elif (vertices_giv[j].x > vertices_giv[i].x) and (vertices_giv[j].y <= vertices_giv[i].y):
                        vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                        i += 1
                        j += 1
                        following_found = True
                     else:
                        j += 1                            
         
         elif passed == 2:
            # * The third vertex to be passed is the one with the minimum y coordinate
            vertices_giv = self._sort_not_passed_vertices(max_x, vertices_giv, "max_x")
            while (passed == 2):
               if (vertices_giv[i] == min_y) or (i == len(vertices_giv) - 1): # To avoid problems with 4-sided shapes
                  passed += 1
               else:
                  j = i + 1
                  following_found = False
                  while following_found == False:
                     if vertices_giv[j] == min_y:
                        following_found = True
                        vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                        i += 1
                     elif (vertices_giv[j].y < vertices_giv[i].y) and (vertices_giv[j].x <= vertices_giv[i].x):
                        vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                        i += 1
                        j += 1
                        following_found = True
                     else:
                        j += 1

         elif passed == 3:
            # * The fourth vertex to be passed is the last one before the vertex with the minimum x coordinate, so that the last edge is formed by the last vertex and the first one.
            vertices_giv = self._sort_not_passed_vertices(min_y, vertices_giv, "min_y")
            while (passed == 3):
               if i == len(vertices_giv) - 1:
                  passed += 1
               else:
                  j = i + 1
                  following_found = False
                  while following_found == False:
                     if i == len(vertices_giv) - 1:
                        following_found = True
                        passed += 1
                     elif (vertices_giv[j].x < vertices_giv[i].x) and (vertices_giv[j].y >= vertices_giv[i].y):
                        vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                        i += 1
                        j += 1
                        following_found = True
                     else:
                        j += 1
      # self._vertices = vertices_giv
      # self.get_shape_vertices() 
                                    
      return vertices_giv
   
   def _create_edges(self) -> list:
      """Method to create the edges of the shape. In doing so it removes the vertices that are contained in the edge defined by the following and previous vertices. This is done to avoid having two edges that are in reality one."""
      edges: list = []
      i = 0
      while i < len(self._vertices) - 1:
         # * Each iteration after the first one will check if the previous edge shares the same slope as the current one. If so, it will remove the ending vertex of the previous edge and both the current and previous edge, and create a new edge with the starting vertex of the previous edge and the ending vertex of the current edge. It will stop before accessing a vertex outisde the list.

         edges.append(Edge(self._vertices[i], self._vertices[i + 1]))
         if (i >= 1) and edges[i - 1].slope == edges[i].slope:
            self._vertices.remove(edges[i - 1].end) # * edges[i - 1] = vertices[i]
            edges.remove(edges[i])
            edges.remove(edges[i - 1])
            i -= 1
            edges.append(Edge(self._vertices[i], self._vertices[i + 1]))
         i += 1
      
      # * Because the last edge is formed by the last vertex and the first one, the last edge is created outside the loop, but the same conditions need to be checked. In this case, though, the last edge will be compared with the following one (the first one overall) and the previous one.
      edges.append(Edge(self._vertices[i], self._vertices[0]))
      if edges[i].slope == edges[i - 1].slope:
         self._vertices.remove(edges[i - 1].end)
         edges.remove(edges[i - 1])
         edges.remove(edges[i])
         i -= 1
         edges.append(Edge(self._vertices[i], self._vertices[i + 1]))
      
      if edges[i].slope == edges[0].slope:
         self._vertices.remove(edges[i].end)
         edges.remove(edges[i])
         edges.remove(edges[0])
         i -= 1
         edges.append(Edge(self._vertices[i], self._vertices[0]))

      self._n_sides = len(self._vertices)
      # print(self._n_sides, len(edges))
      
      return edges

   def _is_shape_regular(self) -> bool:
      same_length_count = 0
      length = self._edges[0].length
      for e in self._edges:
         if e.length == length:
            same_length_count += 1
         else:
            return False
      if same_length_count == self._n_sides: # * Unnecessary but makes the code more robust
         return True

   def _compute_area(self) -> None:
      pass

   def _compute_perimeter(self) -> float:
      """Method to compute the perimeter of the shape. Using the length attribute of the list of edges that define the shape."""
      perimeter: float = 0
      for e in self._edges:
         perimeter += e.length
      return round(perimeter, 2)

   def _compute_inner_angles(self) -> list:
      inner_angles: list = []
      i = 0
      while i < len(self._edges) - 1:
         inner_angles.append(math.acos(((self._edges[i].vector_start.x * self._edges[i + 1].vector_end.x) + (self._edges[i].vector_start.y * self._edges[i + 1].vector_end.y))/(self._edges[i].length * self._edges[i + 1].length)))
         i += 1
      inner_angles.append(math.acos(((self._edges[i].vector_start.x * self._edges[0].vector_end.x) + (self._edges[i].vector_start.y * self._edges[0].vector_end.y))/(self._edges[i].length * self._edges[0].length)))
      inner_angles = [round(t*(180/math.pi), 2) for t in inner_angles]
      # self.get_shape_edges()
      # print(inner_angles)
      return inner_angles
   
   def get_shape_vertices(self) -> None:
      for i in self._vertices:
         print("(", i.x, ",", i.y, ")", end="; ")
      print()

   def get_shape_edges(self) -> None:
      for i in self._edges:
         print("(", i.start.x, ",", i.start.y, ")", "(", i.end.x, ",", i.end.y, ")", end="; ")
      print()

   def get_inner_angles(self) -> list:
      return self._inner_angles   

   def get_area(self) -> float:
      return self._area
   
   def get_perimeter(self) -> float:
      return self._perimeter

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

class Triangle(Shape):
   def __init__(self, *args) -> None:
      super().__init__(*args)
   
   def _create_vertices(self, vertices_giv) -> list:
      """Since triangles don't have diagonals, only edges need to be created. Therefore, the method can be overriden to simply return the given vertices as they were submitted to the program."""
      return vertices_giv

   def _create_edges(self) -> list:
      """Method to create the edges of the triangle. Since the vertices' order doesn't matter, it creates the edges following the given order in the vertices list.
      """
      # * No need for a cycle really, since it will only create two of the three edges
      edges: list = []
      edges.append(Edge(self._vertices[0], self._vertices[1]))
      edges.append(Edge(self._vertices[1], self._vertices[2]))
      edges.append(Edge(self._vertices[2], self._vertices[0]))
      return edges

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
      
class Equilateral(Triangle):
   def __init__(self, *args) -> None:
      super().__init__(*args)
      self._perimeter = self._compute_perimeter()
      self._area = self._compute_area()
      # print(self.get_area())
      # print(self.get_perimeter())
   
   def _compute_perimeter(self) -> float:
      return round(self._edges[0].length * 3, 2)

   def _compute_area(self) -> float:
      return round((math.sqrt(3)/4)*(self._edges[0].length**2), 2)
   
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

if __name__ == "__main__":
   # Uncomment  the following lines if you want to test the create_shape() method quickly
   # v1 = Vertex(2, -1)
   # v2 = Vertex(3, -1)
   # v3 = Vertex(3.5, -1)
   # v4 = Vertex(9, 0)
   # v5 = Vertex(7, -1.25)
   # v6 = Vertex(10, 2)
   # v7 = Vertex(1, 3)
   # v8 = Vertex(2, 6)
   # v9 = Vertex(12, 4)
   # v10 = Vertex(10, 10)
   # v11 = Vertex(10, 10)
   # vertices_list: list = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]
   # test_shape = Shape(vertices_list)
   # print("Vertices: ")
   # test_shape.get_shape_vertices()

   print("Hello! This is a program to create a convex shape")
   print("Let's create a convex shape first!")
   choice = str(input(""))
   given_vertices: list = []
   vertex_type: str = "x"
   user_input = 0
   x: int = 0
   y: int = 0
   if choice == "y":
      print("To stop entering vertices type \"s\" after entering the y-coordinate of the last vertex")
      conti = True
      user_input = input("Please insert the x coordinate of the first vertex in the shape: ")
      while conti == True:
         if user_input != "s":
            if vertex_type == "x":
               x = float(user_input)
               vertex_type = "y"
               user_input = input("Now, please insert the y coordinate of the vertex in the shape: ")
            else:
               y = float(user_input)
               vertex_type = "x"
               given_vertices.append(Vertex(x, y))
               user_input = input("Please insert the x coordinate of the next vertex in the shape: ")

   else:
      conti = False

   shape1 = Shape(given_vertices)
   print("The shape is regular:", shape1._is_regular)
   print("The vertices are: ", end="")
   shape1.get_shape_vertices()
   print("The edges are: ", end="")
   shape1.get_shape_edges()
   print("The inner angles are:", shape1.get_inner_angles())
   print()
   
   given_vertices.clear()
   print("Now let's create an isosceles triangle! (one with two sides of equal length):")
   x1 = float(input("Enter the x coordinate of the first vertex of the triangle: "))
   y1 = float(input("Enter the y coordinate of the first vertex of the triangle: "))
   given_vertices.append(Vertex(x1, y1))
   x2 = float(input("Enter the x coordinate of the second vertex of the triangle: "))
   y2 = float(input("Enter the y coordinate of the second vertex of the triangle: "))
   given_vertices.append(Vertex(x2, y2))
   x3 = float(input("Enter the x coordinate of the third vertex of the triangle: "))
   y3 = float(input("Enter the y coordinate of the third vertex of the triangle: "))
   given_vertices.append(Vertex(x3, y3))
   isosceles = Isosceles(given_vertices)
   print("The shape is regular:", isosceles._is_regular)
   print("The vertices are: ", end="")
   isosceles.get_shape_vertices()
   print("The edges are: ", end="")
   isosceles.get_shape_edges()
   print("The inner angles are:", isosceles.get_inner_angles())
   print("The area of the triangle is:", isosceles.get_area())
   print("The perimeter of the triangle is:", isosceles.get_perimeter())
   print()

   given_vertices.clear()
   print("Now let's create an equilateral triangle! (one with all of its sides of the same length)")
   x1 = float(input("Enter the x coordinate of the first vertex of the triangle: "))
   y1 = float(input("Enter the y coordinate of the first vertex of the triangle: "))
   given_vertices.append(Vertex(x1, y1))
   x2 = float(input("Enter the x coordinate of the second vertex of the triangle: "))
   y2 = float(input("Enter the y coordinate of the second vertex of the triangle: "))
   given_vertices.append(Vertex(x2, y2))
   x3 = float(input("Enter the x coordinate of the third vertex of the triangle: "))
   y3 = float(input("Enter the y coordinate of the third vertex of the triangle: "))
   given_vertices.append(Vertex(x3, y3))
   equilateral = Equilateral(given_vertices)
   print("The shape is regular:", equilateral._is_regular)
   print("The vertices are: ", end="")
   equilateral.get_shape_vertices()
   print("The edges are: ", end="")
   equilateral.get_shape_edges()
   print("The inner angles are:", equilateral.get_inner_angles())
   print("The area of the triangle is:", equilateral.get_area())
   print("The perimeter of the triangle is:", equilateral.get_perimeter())
   print()

   given_vertices.clear()
   print("Now, let's create an scalene triangle! (one with all of its sides of different length)")
   x1 = float(input("Enter the x coordinate of the first vertex of the triangle: "))
   y1 = float(input("Enter the y coordinate of the first vertex of the triangle: "))
   given_vertices.append(Vertex(x1, y1))
   x2 = float(input("Enter the x coordinate of the second vertex of the triangle: "))
   y2 = float(input("Enter the y coordinate of the second vertex of the triangle: "))
   given_vertices.append(Vertex(x2, y2))
   x3 = float(input("Enter the x coordinate of the third vertex of the triangle: "))
   y3 = float(input("Enter the y coordinate of the third vertex of the triangle: "))
   given_vertices.append(Vertex(x3, y3))
   scalene = Scalene(given_vertices)
   print("The shape is regular:", scalene._is_regular)
   print("The vertices are: ", end="")
   scalene.get_shape_vertices()
   print("The edges are: ", end="")
   scalene.get_shape_edges()
   print("The inner angles are:", scalene.get_inner_angles())
   print("The area of the triangle is:", scalene.get_area())
   print("The perimeter of the triangle is:", scalene.get_perimeter())
   print()

   given_vertices.clear()
   print("Now, let's create a right triangle! (one with a right angle, two legs and a hypothenuse)")
   x1 = float(input("Enter the x coordinate of the first vertex of the triangle: "))
   y1 = float(input("Enter the y coordinate of the first vertex of the triangle: "))
   given_vertices.append(Vertex(x1, y1))
   x2 = float(input("Enter the x coordinate of the second vertex of the triangle: "))
   y2 = float(input("Enter the y coordinate of the second vertex of the triangle: "))
   given_vertices.append(Vertex(x2, y2))
   x3 = float(input("Enter the x coordinate of the third vertex of the triangle: "))
   y3 = float(input("Enter the y coordinate of the third vertex of the triangle: "))
   given_vertices.append(Vertex(x3, y3))
   rightTriangle = RightTriangle(given_vertices)
   print("The shape is regular:", rightTriangle._is_regular)
   print("The vertices are: ", end="")
   rightTriangle.get_shape_vertices()
   print("The edges are: ", end="")
   rightTriangle.get_shape_edges()
   print("The inner angles are:", rightTriangle.get_inner_angles())
   print("The area of the triangle is:", rightTriangle.get_area())
   print("The perimeter of the triangle is:", rightTriangle.get_perimeter())
   print()

   given_vertices.clear()
   print("Now, let's create a square! (all of its sides must have the same length)")
   x1 = float(input("Enter the x coordinate of the first vertex of the square: "))
   y1 = float(input("Enter the y coordinate of the first vertex of the square: "))
   given_vertices.append(Vertex(x1, y1))
   x2 = float(input("Enter the x coordinate of the second vertex of the square: "))
   y2 = float(input("Enter the y coordinate of the second vertex of the square: "))
   given_vertices.append(Vertex(x2, y2))
   x3 = float(input("Enter the x coordinate of the third vertex of the square: "))
   y3 = float(input("Enter the y coordinate of the third vertex of the square: "))
   given_vertices.append(Vertex(x3, y3))
   x4 = float(input("Enter the x coordinate of the third vertex of the square: "))
   y4 = float(input("Enter the y coordinate of the third vertex of the square: "))
   given_vertices.append(Vertex(x4, y4))
   square = Square(given_vertices)
   print("The shape is regular:", square._is_regular)
   print("The vertices are: ", end="")
   square.get_shape_vertices()
   print("The edges are: ", end="")
   square.get_shape_edges()
   print("The inner angles are:", square.get_inner_angles())
   print("The area of the square is:", square.get_area())
   print("The perimeter of the square is:", square.get_perimeter())
   print()

   given_vertices.clear()
   print("Now, let's create a rectangle! (a shape with two pairs of sides that must share the same length)")
   x1 = float(input("Enter the x coordinate of the first vertex of the rectangle: "))
   y1 = float(input("Enter the y coordinate of the first vertex of the rectangle: "))
   given_vertices.append(Vertex(x1, y1))
   x2 = float(input("Enter the x coordinate of the second vertex of the rectangle: "))
   y2 = float(input("Enter the y coordinate of the second vertex of the rectangle: "))
   given_vertices.append(Vertex(x2, y2))
   x3 = float(input("Enter the x coordinate of the third vertex of the rectangle: "))
   y3 = float(input("Enter the y coordinate of the third vertex of the rectangle: "))
   given_vertices.append(Vertex(x3, y3))
   x4 = float(input("Enter the x coordinate of the third vertex of the rectangle: "))
   y4 = float(input("Enter the y coordinate of the third vertex of the rectangle: "))
   given_vertices.append(Vertex(x4, y4))
   rectangle = Rectangle(given_vertices)
   print("The shape is regular:", rectangle._is_regular)
   print("The vertices are: ", end="")
   rectangle.get_shape_vertices()
   print("The edges are: ", end="")
   rectangle.get_shape_edges()
   print("The inner angles are:", rectangle.get_inner_angles())
   print("The area of the rectangle is:", rectangle.get_area())
   print("The perimeter of the rectangle is:", rectangle.get_perimeter())



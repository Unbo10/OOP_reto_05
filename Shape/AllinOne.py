import math # Built-in module

def enter_coordinate(coordinate: str) -> float:
   done: bool = False
   while done == False:
      try:
         n = float(input("Enter the {}: ".format(coordinate)))
      except ValueError as e:
         print("The value enterd is not a real number")
      else:
         done = True
   return n

class InsufficientVerticesError(Exception):
   def __init__(self, message="The shape must have more than three vertices") -> None:
      super().__init__(message)

class NotStraightEdgeError(Exception):
   def __init__(self, message="The rectangle cannot be created because the vertex entered doesn't form a straight edge with the previous vertex") -> None:
      super().__init__(message)

class NotSquareSide(Exception):
   def __init__(self, message="The vertices do not form a side of the square") -> None:
      super().__init__(message)

class NotTriangleError(Exception):
   def __init__(self, *args) -> None:
      super().__init__(*args)

class NotEquilateralError(NotTriangleError):
   def __init__(self, message="The vertices do not form an equilateral triangle") -> None:
      super().__init__(message)

class NotIsoscelesError(Exception):
   def __init__(self, message="The vertices do not form an isosceles triangle") -> None:
      super().__init__(message)
   
class NotRightTriangleError(Exception):
   def __init__(self, message="The vertices do not form a right triangle") -> None:
      super().__init__(message)

class Test:
   def test_user_input_vertex(self) -> None:
      """Function to test the creation of two vertices with user input."""
      print("Vertex user input test")
      print("Enter the coordinates of two vertices")
      x1: float = enter_coordinate("x coordinate of the first vertex")
      y1: float = enter_coordinate("y coordinate of the first vertex")
      x2: float = enter_coordinate("x coordinate of the second vertex")
      y2: float = enter_coordinate("y coordinate of the second vertex")
      v1: Vertex = Vertex(x1, y1)
      v2: Vertex = Vertex(x2, y2)
      print("Vertex 1: ", end = "")
      v1.print_vertex_coordinates()
      print("Vertex 2: ", end = "")
      v2.print_vertex_coordinates()
      print("Distance between the vertices:", v1.calculate_vertex_distance(v2))
   
   def test_user_input_edge(self) -> None:
      """Function to test the creation of an edge with user input."""
      print("Edge user input test")
      print("Enter the coordinates of the vertices of an edge")

      valid_input: bool = False
      x1: float = enter_coordinate("x coordinate of the first vertex")
      y1: float = enter_coordinate("y coordinate of the first vertex")
      while valid_input == False:
         try:
            x2: float = enter_coordinate("x coordinate of the second vertex")
            y2: float = enter_coordinate("y coordinate of the second vertex")
            if  (x1 == x2) and (y1 == y2):
               raise ValueError
         except ValueError as e:
            print("The edge cannot be created because the vertices are the same")
         else:
            valid_input = True

      edge: Edge = Edge(Vertex(x1, y1), Vertex(x2, y2))
      print("Start vertex:", end = " ")
      edge.start.print_vertex_coordinates()
      print("End vertex:", end = " ")
      edge.end.print_vertex_coordinates()
      print("Length of the edge:", round(edge.length, 4))
      print("Slope of the edge:", edge.slope)
      print("Vector from start to end:", end =" ")
      edge.vector_end.print_vertex_coordinates()
      print("Vector from end to start:", end =" ")
      edge.vector_start.print_vertex_coordinates()

   def test_user_input_shape(self) -> None:
      """Function to test the creation of a convex shape with user input."""
      print("Enter the coordinates of the vertices of a convex shape (must have more than 3 vertices for the method _create_vertices() to work. The method is overriden for this particular case in the module \"triangle.py\")")
      given_vertices: list = []
      vertex_type: str = "x"
      user_input = 0
      x: float = 0
      y: float = 0
      conti = True
      print("To stop entering vertices press Ctrl+C")
      while conti == True:
         try:
            x = enter_coordinate("x coordinate of the vertex")
            y = enter_coordinate("y coordinate of the vertex")
            for i in given_vertices:
               if (i.x == x) and (i.y == y):
                  raise AssertionError
         except AssertionError:
            print("The vertex has already been entered")
         except KeyboardInterrupt:
            conti = False
         else:
            given_vertices.append(Vertex(x, y))

      try:
         shape1 = Shape(given_vertices)
         if (len(given_vertices)==3):
            raise InsufficientVerticesError
      except InsufficientVerticesError as i:
         print()
         print(i)
      except IndexError:
         print()
         print("The shape is not convex")
      else:
         print("The shape is regular:", shape1._is_regular)
         print("The vertices are: ", end="")
         shape1.get_shape_vertices()
         print("The edges are: ", end="")
         shape1.get_shape_edges()
         print("The inner angles are:", shape1.get_inner_angles())

   def test_user_input_rectangle(self) -> None:
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

   def test_user_input_square(self) -> None:
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
            if ((x4 == x2) and (y4 == y2)) or ((x4 == x1) and (y4 == y1)):
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

   def test_user_input_triangle(self) -> None:
      """Function to test the creation of a triangle with user input."""
      print("Triangle user input test")
      print("Enter the vertices of a triangle")
      x1: float = enter_coordinate("x coordinate of the first vertex")
      y1: float = enter_coordinate("y coordinate of the first vertex")
      valid_input: bool = False

      while valid_input == False:
         try:
            x2: float = enter_coordinate("x coordinate of the second vertex")
            y2: float = enter_coordinate("y coordinate of the second vertex")
            if (x1 == x2) and (y1 == y2):
               raise NotTriangleError("The vertices must be different")
         except NotTriangleError as e:
            print(e)
         else:
            valid_input = True
      
      valid_input = False
      while valid_input == False:
         try:
            x3: float = enter_coordinate("x coordinate of the third vertex")
            y3: float = enter_coordinate("y coordinate of the third vertex")
            if ((x2 == x3) and (y2 == y3)) or ((x1 == x3) and (y1 == y3)):
               NotTriangleError("The vertices must be different")
         except NotTriangleError as e:
            print(e)
         else:
            valid_input = True

      vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3)]
      triangle = Triangle(vertices)
      print("The shape is regular:", triangle._is_regular)
      print("The vertices are: ", end="")
      triangle.get_shape_vertices()
      print("The edges are: ", end="")
      triangle.get_shape_edges()
      print("The inner angles are:", triangle.get_inner_angles())

   def test_user_input_equilateral(self) -> None:
      """Function to test the creation of an equilateral triangle with user input."""
      print("Equilateral triangle user input test")
      print("Warning: Any square root must be entered as a floating-point number with at least four (4) decimal places") 
      print("Enter the vertices of an equilateral triangle")
      length: float = 0
      e1: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
      e2: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
      e3: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
      valid_input: bool = False

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
            e1 = Edge(Vertex(x1, y1), Vertex(x2, y2))
            length = round(e1.length, 4)
            valid_input = True
      
      valid_input = False
      while valid_input == False:
         try:
            x3: float = enter_coordinate("x coordinate of the third vertex")
            y3: float = enter_coordinate("y coordinate of the third vertex")
            e2 = Edge(Vertex(x2, y2), Vertex(x3, y3))
            e3 = Edge(Vertex(x3, y3), Vertex(x1, y1))
            if (round(e2.length, 4) != length) or (round(e3.length, 4) != length):
               # print(length, round(e2.length, 4), round(e3.length, 4))
               raise NotEquilateralError
         except NotEquilateralError as e:
            print(e)
         else:
            valid_input = True
      
      vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3)]
      equilateral = Equilateral(vertices)
      print("The equilateral triangle is regular:", equilateral._is_regular)
      print("Vertices of the equilateral triangle: ", end = "")
      equilateral.get_shape_vertices()
      print("Edges of the equilateral triangle: ", end = "")
      equilateral.get_shape_edges()
      print("Inner angles of the equilateral triangle:", equilateral.get_inner_angles())
      print("Perimeter of the equilateral triangle:", equilateral._perimeter)
      print("Area of the equilateral triangle:", equilateral._area)

   def test_user_input_isosceles(self) -> None:
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

   def test_user_input_trirectangle(self) -> None:
      """Function to test the creation of a right triangle with user input."""
      print("Right triangle user input test")
      print("Enter the vertices of a right triangle")
      valid_input = False
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

   def test_user_input_scalene(self) -> None:
      """Function to test the creation of a scalene triangle with user input."""
      print("Scalene triangle user input test")
      print("Enter the vertices of an scalene triangle")
      e1: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
      e2: Edge = Edge(Vertex(0, 0), Vertex(0, 0))
      valid_input: bool = False

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
            e1 = Edge(Vertex(x1, y1), Vertex(x2, y2))
            valid_input = True
      
      valid_input = False
      while valid_input == False:
         try:
            x3: float = enter_coordinate("x coordinate of the third vertex")
            y3: float = enter_coordinate("y coordinate of the third vertex")
            e2 = Edge(Vertex(x2, y2), Vertex(x3, y3))
            if (e1.slope == e2.slope):
               raise NotTriangleError
         except NotTriangleError as e:
            print(e)
         else:
            valid_input = True

      vertices = [Vertex(x1, y1), Vertex(x2, y2), Vertex(x3, y3)]
      scalene = Scalene(vertices)
      print("The scalene triangle is regular:", scalene._is_regular)
      print("Vertices of the scalene triangle: ", end = "")
      scalene.get_shape_vertices()
      print("Edges of the scalene triangle: ", end = "")
      scalene.get_shape_edges()
      print("Inner angles of the scalene triangle:", scalene.get_inner_angles())
      print("Perimeter of the scalene triangle:", scalene._perimeter)
      print("Area of the scalene triangle:", scalene._area)

   def test_user_input_all(self) -> None:
      self.test_user_input_shape()
      print()
      self.test_user_input_rectangle()
      print()
      self.test_user_input_square()
      print()
      self.test_user_input_triangle()
      print()
      self.test_user_input_scalene()
      print()
      self.test_user_input_equilateral()
      print()
      self.test_user_input_isosceles()
      print()
      self.test_user_input_trirectangle()
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
      ordered_edges = sorted(self._edges, key = lambda edge: edge.length) # * Guarantees the hypothenuse is the last edge, so the other two will be the legs (catetos)
      return round((ordered_edges[0].length * ordered_edges[1].length) / 2, 2)

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
   test = Test()
   try:
      test.test_user_input_all()
   except KeyboardInterrupt:
      print("\n\nThe program was interrupted by the user.")
   finally:
      print("Thank you for testing the all-in-one shape module! 😃", end="")
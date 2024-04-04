from Shape.shape import test_user_input as test_shape
from Shape.Rectangle.rectangle import test_user_input as test_rectangle
from Shape.Rectangle.square import test_user_input as test_square
from Shape.Triangle.equilateral import test_user_input as test_equilateral
from Shape.Triangle.isosceles import test_user_input as test_isosceles
from Shape.Triangle.rectangle import test_user_input as test_trirectangle
from Shape.Triangle.scalene import test_user_input as test_triangle

if __name__ == "__main__":
    print("Welcome to the test of the different shapes included in the package Shape!")
    print("You will insert the data needed to create each of the package's shapes")
    print()
    test_shape()
    print()
    test_equilateral()
    print()
    test_isosceles()
    print()
    test_trirectangle()
    print()
    test_triangle()
    print()
    test_rectangle()
    print()
    test_square()




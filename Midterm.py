import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    """ Computes the area of circle with radius 'radius'.

    Returns:
    float: area of the circle rounded to 2 decimal points.
    """
    area = math.pi * radius ** 2
    rounded_area = round(area, 2)

    return rounded_area

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    """ Generates a hollow right triangle of stars of height 'n' if n > 3.

    Returns:
    string: a right triangle of height 'n' if n > 3,
    string: a message if n <= 3
    """
    # checks if n is large enough
    if n <= 3:
        return "The triangle height should be at least 4."

    triangle = ""
    # adds the first n - 1 rows of stars and spaces to triangle
    for i in range(n - 1):
        triangle += "*"
        for j in range(i - 1):
            triangle += " "
        if 0 < i:
            triangle += "*"
        triangle += "\n"

    # adds the final row of stars to triangle
    for k in range(n):
        triangle += "*"

    return triangle

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    """ Generates an inverted pyramid of height 'n' if n > 2.
    
    Returns:
    string: an inverted pyramid of height 'n' if n > 2,
    string: a message if n <= 2
    """
    # checks if n is large enough
    if n < 3:
        return "The pyramid height should be at least 3."
    
    pyramid = ""
    for i in range(n):
        # adds i spaces at the start of each row
        for j in range(i):
            pyramid += " "
        # adds 2n-2i-1 stars to each row
        for k in range(2 * (n - i) - 1):
            pyramid += "*"
        pyramid += "\n"

    # returns pyramid without the last "\n"
    return pyramid.rstrip()

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(2))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(5))
print()

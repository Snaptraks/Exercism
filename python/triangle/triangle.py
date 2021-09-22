def _is_triangle(sides):
    a, b, c = sides

    return ((a + b > c)
            and (a + c > b)
            and (b + c > a)
            and all([s > 0 for s in sides]))


def equilateral(sides):
    a, b, c = sides
    return (_is_triangle(sides)
            and (a == b == c))


def isosceles(sides):
    return (_is_triangle(sides)
            and len(set(sides)) <= 2)


def scalene(sides):
    return (_is_triangle(sides)
            and len(set(sides)) == 3)

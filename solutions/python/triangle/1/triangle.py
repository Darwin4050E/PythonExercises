def validate_triangle(sides):
    side_a_b_ge_c = sides[0] + sides[1] >= sides[2]
    side_b_c_ge_a = sides[1] + sides[2] >= sides[0]
    side_a_c_ge_b = sides[0] + sides[2] >= sides[1]
    if(sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0):
        return False
    return side_a_b_ge_c and side_b_c_ge_a and side_a_c_ge_b

def equilateral(sides):
    return validate_triangle(sides) and (sides[0] == sides[1]) and (sides[1] == sides[2])


def isosceles(sides):
    return validate_triangle(sides) and (equilateral(sides) or (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]))


def scalene(sides):
    return validate_triangle(sides) and sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]

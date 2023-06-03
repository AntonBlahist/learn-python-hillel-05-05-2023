import math


def triangle_side():
    """
    Creating a list of triangle sides.
    Return <triangle sides>.
    """
    triangle_sides = []
    a = input("Enter side A: ")
    if a == "":
        print("You didn't indicate the side.")
    else:
        a = int(a)
        triangle_sides.append(a)
    b = input("Enter side B: ")
    if b == "":
        print("You didn't indicate the side.")
    else:
        b = int(b)
        triangle_sides.append(b)
    c = input("Enter side C: ")
    if c == "":
        print("You didn't indicate the side.")
    else:
        c = int(c)
        triangle_sides.append(c)
    for x in triangle_sides:
        if x <= 0:
            print("The side of the triangle must be greater than 0.")
            exit()
    return triangle_sides


def triangle_exist(sides):
    """
    Verifying the existence of a triangle.
    Return True or False.
    """
    if len(sides) < 3:
        return False
    if (sides[0] + sides[1]) > sides[2] \
            and (sides[0] + sides[2]) > sides[1] \
            and (sides[1] + sides[2]) > sides[0]:
        return True
    else:
        return False


def triangle_perimeter(sides):
    """
    Calculating the perimeter of a triangle.
    Return the perimeter.
    """
    func_perimeter = sum(sides)
    return func_perimeter


def triangle_area(sides):
    """
    Calculating the area of a triangle.
    Return the area.
    """
    half_p = sum(sides) / 2
    func_area = math.sqrt(half_p
                          * (half_p - sides[0])
                          * (half_p - sides[1])
                          * (half_p - sides[2]))
    return func_area


if __name__ == "__main__":
    print("The program calculates the perimeter and area of a triangle.")
    side = triangle_side()
    exist = triangle_exist(side)
    if exist:
        perimeter = triangle_perimeter(side)
        area = triangle_area(side)
        print(f"A triangle exists. Its perimeter is {perimeter},"
              f" its area is {area}.")
    if not exist:
        print("A triangle with the sides indicated does not exist.")

def circle():
    radius = 42

    square = round(3.1415926 * radius ** 2, 4)

    point_1 = (23, 34)

    distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
    bool_1 = distance_1 <= radius

    point_2 = (30, 30)

    distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
    bool_2 = distance_2 <= radius

    print(square, "\n", bool_1, "\n", bool_2)

circle()
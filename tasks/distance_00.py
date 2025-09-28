def distance():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    distances = {}

    for city1, (x1, y1) in sites.items():
        distances[city1] = {}
        for city2, (x2, y2) in sites.items():
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[city1][city2] = dist

    print(distances)
distance()
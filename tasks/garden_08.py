def garden_08():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

    garden_set = set(garden)
    meadow_set = set(meadow)

    print(garden_set | meadow_set)

    print(garden_set & meadow_set)

    print(garden_set - meadow_set)

    print(meadow_set - garden_set)
garden_08()
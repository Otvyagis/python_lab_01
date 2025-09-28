def my_family_04():
    my_family = ["Олег", "Игорь", "Татьяна", "Александр"]

    my_family_height = [
        ["Олег", 180],
        ["Игорь", 180],
        ["Александр", 176],
        ["Татьяна", 163]
    ]
    print("Рост отца -",str(my_family_height[2][1]), "см")
    print("Общий рост моей семьи -", str(sum(member[1] for member in my_family_height)))
my_family_04()
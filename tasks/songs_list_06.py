def songs_list_06():
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]

    halo_time = violator_songs_list[3][1]
    enjoy_the_silence_time = violator_songs_list[5][1]
    clean_time = violator_songs_list[8][1]
    total_time = halo_time + enjoy_the_silence_time + clean_time
    print("Три песни звучат", round(total_time, 3), "минут")

    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }

    sweetest_perfection_time = violator_songs_dict['Sweetest Perfection']
    policy_of_truth_time = violator_songs_dict['Policy of Truth']
    blue_dress_time = violator_songs_dict['Blue Dress']
    other_total_time = sweetest_perfection_time + policy_of_truth_time + blue_dress_time
    print("А другие три песни звучат", round(other_total_time), "минут")
songs_list_06()
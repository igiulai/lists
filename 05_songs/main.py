violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

n = int(input("Сколько песен выбрать? "))
total_time = 0.0

# Создаем словарь для быстрого поиска песен по названию
songs_dict = {song[0]: song[1] for song in violator_songs}

# Запрашиваем названия песен и суммируем время
for i in range(n):
    song_name = input(f"Название {i+1}-й песни: ")
    if song_name in songs_dict:
        total_time += songs_dict[song_name]
    else:
        print(f"Песни '{song_name}' нет в списке, пропускаем.")

print(f"Общее время звучания песен — {round(total_time, 2)} минуты")

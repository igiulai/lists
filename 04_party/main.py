guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print("\nСейчас на вечеринке ", len(guests), "человек: ", guests)
    action = input("Гость пришел или ушел? ").lower()

    if action == "пора спать":
        break

    if action == "пришел":
        if len(guests) < 6:
            name = input("Имя гостя: ")
            guests.append(name)
            print("Привет, ", name, "!")
        else:
            name = input("Имя гостя: ")
            print("Прости, ", name, ", но мест нет.")
    elif action == "ушел":
        name = input("Имя гостя: ")
        if name in guests:
            guests.remove(name)
            print("Пока, ", name, "!")
        else:
            print("Гостя с именем ", name, "нет на вечеринке.")
    else:
        print("Не понял команду. Введите 'пришел', 'ушел' или 'пора спать'.")

print("\nВечеринка закончилась, все легли спать.")
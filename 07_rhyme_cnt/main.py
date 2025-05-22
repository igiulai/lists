n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))
print(f"\nЗначит, выбывает каждый {k}-й человек\n")

people = list(range(1, n + 1))
current = 0  # Текущая позиция в круге

while len(people) > 1:
    print(f"Текущий круг людей: {people}")
    start = current % len(people)
    print(f"Начало счёта с номера {people[start]}")

    # Вычисляем кто выбывает
    current = (start + k - 1) % len(people)
    print(f"Выбывает человек под номером {people[current]}\n")

    # Удаляем выбывшего
    people.pop(current)

print(f"Остался человек под номером {people[0]}")
n = int(input("Количество чисел: "))
sequence = []
for i in range(n):
    num = int(input(f"Число: "))
    sequence.append(num)

print("\nПоследовательность:", sequence)

# Функция проверки симметричности
def is_symmetric(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[-i - 1]:
            return False
    return True

# Находим минимальное количество чисел для добавления
add_numbers = []
for i in range(n):
    if is_symmetric(sequence[i:]):
        add_numbers = sequence[:i][::-1]
        break

print("Нужно приписать чисел:", len(add_numbers))
print("Сами числа:", add_numbers)
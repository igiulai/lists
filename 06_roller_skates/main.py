n = int(input("Количество роликов: "))
skates = []
for i in range(n):
    size = int(input(f"Размер пары {i+1}: "))
    skates.append(size)

k = int(input("\nКоличество людей: "))
people = []
for i in range(k):
    size = int(input(f"Размер ноги человека {i+1}: "))
    people.append(size)

skates.sort()
people.sort()

count = 0
i = j = 0

while i < len(skates) and j < len(people):
    if skates[i] >= people[j]:
        count += 1
        i += 1
        j += 1
    else:
        i += 1

print("\nНаибольшее количество людей, которые могут взять ролики: ", count)
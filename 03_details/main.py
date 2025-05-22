shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input("Название детали: ")

count = 0
total_cost = 0

for item in shop:
    if item[0] == detail_name:
        count += 1
        total_cost += item[1]

print("Количество деталей: ", count)
print("Общая стоимость: ", total_cost)
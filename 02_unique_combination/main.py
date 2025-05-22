def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    len1, len2 = len(list1), len(list2)

    while i < len1 and j < len2:
        if list1[i] < list2[j]:
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged or list2[j] != merged[-1]:
                merged.append(list2[j])
            j += 1
        else:  # равные элементы
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
            j += 1

    # Добавляем оставшиеся элементы из list1
    while i < len1:
        if not merged or list1[i] != merged[-1]:
            merged.append(list1[i])
        i += 1

    # Добавляем оставшиеся элементы из list2
    while j < len2:
        if not merged or list2[j] != merged[-1]:
            merged.append(list2[j])
        j += 1

    return merged

# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
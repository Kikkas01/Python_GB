# 5.Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Решение 1 - c определением точного места размещения нового элемента в соответствии с условиями задачи:

new_element = input("Введите новый элемент рейтинга в виде натурального числа:")
if not new_element.isdigit():
    print("Неверный формат числа")
    exit()
new_element = int(new_element)

rating = [10, 6, 4, 4, 3]
count = len(rating)
for el in rating:
    count = count - 1
    if new_element > el and count > 0:
        rating.insert(rating.index(el), new_element)
        break
    elif new_element == el and count > 0:
        count = count + 1
        continue
    elif new_element < el and count > 0:
        continue
    else:
        rating.append(new_element)
        break
print(rating)

# Решение 2 - более простой вариант, но он "перемешивает" одинаковые числа за счет пересортировки:

new_element = input("Введите новый элемент рейтинга в виде натурального числа:")
if not new_element.isdigit():
    print("Неверный формат числа")
    exit()
new_element = int(new_element)

rating = [10, 6, 4, 4, 3, new_element]
rating.sort()
rating.reverse()
print(rating)

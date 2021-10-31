# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и
# словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

products = []
no_unit = 1
name = None
price = None
quantity = None
measure = None

while True:
    if name is None:
        name = input("Введите наименование товара:")
    if price is None:
        price = float(input("Введите цену товара:"))
    if quantity is None:
        quantity = input("Введите количество товара:")
        if not quantity.isdigit():
            print("Введите целое число")
            exit()
        quantity = int(quantity)
    if measure is None:
        measure = input("Введите единицы измерения товара:")

    products.append(
        (no_unit,
         {"Наименование": name,
          "Цена": price,
          "Количество": quantity,
          "Единицы измерения": measure}
         )
    )
    no_unit += 1
    name = None
    price = None
    quantity = None
    measure = None

    print(products)

    input_end = input("Закончен ли ввод значений: y/n? ")
    if input_end == "y":
        break
print(products)

analytics = {
    "Наименование": [],
    "Цена": [],
    "Количество": [],
    "Ед. измерения": []
}

for number, prod_info in products:
    analytics["Наименование"].append(prod_info["Наименование"])
    analytics["Цена"].append(prod_info["Цена"])
    analytics["Количество"].append(prod_info["Количество"])
    analytics["Ед. измерения"].append(prod_info["Единицы измерения"])

print(analytics)

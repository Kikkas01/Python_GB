# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

try:
    with open("task4.txt", encoding='utf-8') as txt_file_4:
        new = []
        rus = ["Один", "Два", "Три", "Четыре"]
        eng = ["One", "Two", "Three", "Four"]
        count = 0
        for line in txt_file_4:
            new.append(line.replace(eng[count], rus[count]))
            count += 1
    with open("task4_1.txt", "w", encoding='utf-8') as txt_file_4_1:
        txt_file_4_1.writelines(new)
except IOError:
    print("error")

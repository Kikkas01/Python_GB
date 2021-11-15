# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

try:
    with open("task1.txt", "w", encoding='utf-8') as txt_file:
        while True:
            new_string = input("Введите строку текстового файла: ")
            if not new_string:
                break
            txt_file.writelines(f"{new_string}\n")
except IOError:
    print("error")

print(txt_file.closed)

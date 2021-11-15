# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("task2.txt") as txt_file_2:
    count = 0
    for line in txt_file_2:
        count += 1
        print(f"Количество слов в строке №{count} равно {str(len(line.split()))}")
with open("task2.txt") as txt_file_2:
    print(f"Количество строк в файле равно {len(txt_file_2.readlines())}")

print(txt_file_2.closed)

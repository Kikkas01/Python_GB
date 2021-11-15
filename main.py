import sys
from Lesson4 import task1

try:
    file, work_time, rate, bonus = sys.argv
except ValueError:
    print("Invalid arguments")
    exit()

print(task1.salary(int(work_time), float(rate), float(bonus)))



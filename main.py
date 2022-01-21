# Задание 1

date = input("Введите дату: ")
print(date)

Task = input("Описание задачи: ")
print(Task)

# Задание 1 

date = input('Введите дату: ')
task = input('Введите задачу: ')

s = date + ' ' + task
print(s)

# Альтернативное решение
print(date, task)
# print может выводить на экран сразу несколько строк через пробел

# Задание 2


date_1 = input('Введите дату: ')
task_1 = input('Введите задачу: ')
date_2 = input('Введите дату: ')
task_2 = input('Введите задачу: ')
date_3 = input('Введите дату: ')
task_3 = input('Введите задачу: ')

print(date_1, task_1)
print(date_2, task_2)
print(date_3, task_3)

# Задание 3

task_dict = {}

date = input('Введите дату: ')
task = input('Введите задачу: ')
task_dict[date] = task

date = input('Введите дату: ')
task = input('Введите задачу: ')
task_dict[date] = task


date = input('Введите дату: ')
task = input('Введите задачу: ')
task_dict[date] = task

# Если хотите лучше понять это решение - добавьте вывод на экран после каждого пользовательского ввода
# print(date, task)
# print(task_dict)
# Вы увидите, что переменные date и task изменяются, но данные в словаре task_dict остаются прежними
# Программа решает головоломку:
# Сколько вопросов необходимо задать, чтобы однозначно определить пятизначный номер?
import random

num = str(random.randint(0, 100000))
print(list(num))


def guess_the_num(num):
    print("Ответ должен содержать только да или нет!")
    num_s = 0
    num_e = 100000
    while num_e != list(num):
        answer = input(f"Число больше {num_s + (num_e - num_s)//2}? ")
        if answer == 'да':
            num_s = num_s + (num_e - num_s)//2
        else:
            num_e = num_s + (num_e - num_s)//2
        print(f'Start = {num_s}')
        print(f'End = {num_e}')





guess_the_num(num)

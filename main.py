# Программа решает головоломку:
# Сколько вопросов необходимо задать, чтобы однозначно определить пятизначный номер?
import random

num = str(random.randint(9999, 99999))
print(list(num))


def guess_the_num(num):
    print("Ответ должен содержать только да или нет!")
    temp_num = 99999
    print(temp_num)
    while temp_num != list(num):
        answer = input(f"Число больше {round(temp_num/2)}? ")
        if answer == 'да':
            # всё будет повторяться по циклу
            pass
        else:
            pass





guess_the_num(num)

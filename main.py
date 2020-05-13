# Программа решает головоломку:
# Сколько вопросов необходимо задать, чтобы однозначно определить пятизначный номер?
import random

num = random.randint(0, 100000)
print(num)


def guess_the_num(num):
    print("Ответ должен содержать только да или нет!")
    num_s = 0
    num_e = 100000
    step = 0
    while num_e != num:
        print(f"Число больше {num_s + (num_e - num_s)//2}? ")
        if num > num_s + (num_e - num_s)//2:
            print("Да")
            num_s = num_s + (num_e - num_s)//2
        else:
            print("Нет")
            num_e = num_s + (num_e - num_s)//2
        step +=1
    step -=1
    return step


print(f"Число шагов = {guess_the_num(num)}")
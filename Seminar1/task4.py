# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал 
# каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

n= int(input("Введите число кратное 6: "))
print(f" Петя сделал:    {n//6}  журавликов"    
    f"\n Катя сделалала: {n//6*4}  журавликов"
    f"\n Сережа сделал:  {n//6}  журавликов")


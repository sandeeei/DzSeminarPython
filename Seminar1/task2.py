# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

n= int(input ("Введите трехзначное число: "))
if n<100 or n>999:
    print("Вы ввели не трехзначное число")
else:    
    print(f"Сумма цифр данного числа  {n//100+n%100//10+n%10}")

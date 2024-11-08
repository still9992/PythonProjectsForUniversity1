first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first != second and second != third and first != third: #Если нет одинаковых
    print(0)
elif first == second and second == third and first == third: #Если все числа одинаковы
    print(3)
else: # Остаются случаи, когда только два одинаковых
    print(2)
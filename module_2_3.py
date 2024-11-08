#Нули ничто, отрицание недопустимо
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#my_list = [42, 69, 13, 0, 99, 5, 9, 8, 7, 6, 5]
i = 0
while i <= len(my_list):  
    if i == len(my_list):
        print("Достигнут конец списка.")
        break
    elif my_list[i] < 0:
        #print("Достигнуто отрицательное число:", my_list[i])
        break
    elif my_list[i] > 0:
        print(my_list[i])
    i = i + 1

        
    


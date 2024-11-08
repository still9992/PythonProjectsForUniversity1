## Условия
#name = input ('Введите имя: ')
#if name == "Вадим":
#    print("Здравствуйте, администратор!")
#if name == "Денис":
#    print("Здравствуйте, преподаватель!")
#else:
#    print("Привет", name)

#number = int(input("Введите число: ")) #Fizz Buzz FizzBuzz
#if number %3 == 0 and number %5 == 0:
#    print('FizzBuzz')
#elif number %3 == 0:
#    print('Fizz')
#elif number %5 == 0:
#    print("Buzz")
#else:
#    print("Число не подходит")
##or - не строгий оператор; and - строгий оператор

## Cтиль кода
#import this # сборник пословиц в тему питона
#name = input("Enter your name ")
#if 5 > 1:
#    print("ok")
##Форматирование кода в Phycharm: ctrl+alt+L

#Цикл WHILE

#while True:
#    number = int(input("Введите число: "))
#    if number % 2 == 0:
#        print("Число четное")
#        continue #Отправляет к следующему шагу цикла, пропуская все команды далее
#    else:
#        print("Число нечетное")
#        break # останавливает выполнение данного цикла
#    print("Меня не забыли")
#print("Я за циклом")

##Цикл FOR
#for i in 1, 2, 3, 4:
#    print(i)

#list_ = ["one", "two", "three"]
#for i in list_:
#    if i == "three":
#        list_.remove(i) # удаление конкретного элемента в списке
#print(list_)

#list_ = ["one", "two", "three"]
#for i in range(len(list_)):
#    list_[i] = '^_^' # замена элементов в каждом элементе
#print(list_)

#list_2 = [2, 5, 2, 8, 3]
#sum_ = 0
#for i in range(len(list_2)):
#    sum_ += list_2[i] #сумма элементов списка
#print(sum_)

##таблица умножения
#for i in range(1, 11): # начало, конец, шаг
#    for j in range(1, 11):
#        print(f'{i} x {j} = {i * j}')

# Перебор словаря
dict_ = {"a": 1, "b": 2, "c": 3}
for i in dict_:
    print(i, dict_[i])

#То же самое, но через метод
dict_ = {"a": 1, "b": 2, "c": 3}
for i, k in dict_.items():
    print(i, k)
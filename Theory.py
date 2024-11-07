##Срез в строке:
#name = "Vadim"
#print(name[0:3]) #- выведет Vad
#print(name[:3]) #- то же самое что и print(name[0:3])

#print(name[0:3:2]) #выведет Vd

#print(name[2:]) #- выведет dim

#print(name[::-1]) #- выведет midaV

#print(name[1::2]) #- каждый второй символ на вывод
##___________________________
#name = input("Введите Ваше имя: ")
#current_year = 2024
#date_of_birth = input("В каком году вы родились?")
#age = current_year - int(date_of_birth)
#print("Здравствуйте,", name)
#print("В этом году Вам", age,"лет/года")

#print("привет, я строка в нижнем регистре")
#print("привет, я строка в нижнем регистре".upper().lower())
#print("привет, я строка в нижнем регистре".replace(" ","_"))

##Списки
##food = ["apple", "coconut", "banana"]
##print(food[0])
##food[0] = "peach" #- заменит нулевой или любой указанный элемент списка
#print(food)
#food.append(True) #- добавить элемент в конец списка
#print(food)
#food.extend(["string", 2])
#print(food)
#food.remove("peach")
#print(food)

#print("coconut" in food) #- выведет true
#print(food[0:2:2]) #- начало:конец:шаг

##___________
#Кортежи - используются для создания списка без изменяемых элементов. Занимает меньше места, чем список list. Поддерживает конкатенацию
#tuple_ = 1, 2, 3, 4, True, "string"
#list_ = [1, 2, 3, 4, True, "string"]
#tuple_2 = (1,2,3,4)
#tuple_3 = tuple([1,2,3,4])
#print(tuple_)
#print(tuple_2)
#print(tuple_3)
##tuple_[0]=200 # - обращаться к элементу кортежа НЕЛЬЗЯ

#print(tuple_.__sizeof__()) #72
#print(list_.__sizeof__()) #88
## Если в кортеже есть список, то к нему можно обращаться и менять значения ТОЛЬКО в списке
#tuple_ = [1, 2, 3], 4, True, "string"
#tuple_[0][0] = 512
#print(tuple_)

#tuple_ = tuple_*3
#print(tuple_) # три раза выведет кортеж в одной строке

#Словарь - неупорядоченная коллекция, не всегда будет все по порядку
# ключ не может быть списком	
#from importlib.metadata import PathDistribution


#phone_book = {"Denis": 125151324, "Ivan": 15135135} # ключ:значение
#print(phone_book)
## для обращения к элементу словаря необходимо указать ключ
#print(phone_book["Denis"])
##Замена значения словаря через обращение по ключу
#phone_book["Denis"] = 9999999999
#print(phone_book)
##Если обратиться к несуществующему ключу, то он добавится в конец словаря
#phone_book["Anton"] = 241251515
#print(phone_book)
##Удаление элемента словаря по ключу
#del phone_book["Ivan"]
#print(phone_book)
## Методы работы со словарями
#phone_book.update({"Sasha":5123513313, "Alex":12125515135})
#print(phone_book)
##
#print(phone_book.get("Kamal", "Такого ключа нет"))
## pop - извлекает элемент и значение элемента можно записать в переменную (работает со списками, если указать элемент)
#print(phone_book)
#a = phone_book.pop("Anton")
#print(phone_book)
#print(a)
## keys - коллекция из ключей
#print(phone_book.keys())
## Если нужен и ключ и значение - items
#print(phone_book.items())

#_______________________________
#Множества - хранят только уникальные значения. Значения могут быть разного типа
set_ = {1,2,2,3,4,5,3,2,1,5,2,5, "strinnnng", True, (1,2,3)} # повторов не будет
print(set_)
list_ = [1,2,3,4,5,6,7,8,9,0,2,2,1,2,4,6,7,8,9,3]
list_ = set(list_) # преобразование списка во множество теперь list без повторов
#Методы discard - не будет ругаться если элемента нет,
print(list_)
list_.discard(1) # удаление числа из множества
print(list_)
#list_.remove(12) # удаление числа из множества, но если такого числа нет - будет ошибка
#print(list_)
print(list_)
list_.add(10) # добавление числа в конец множества, если число уже было, то не добавится
print(list_)



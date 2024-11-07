#_____Работа со словарем
my_dict = {"Kirill":1966, "Ivan":1984, "Nikita":2004, "Mark":1994, "Sergey":1933, "Nikolay":1978, "Micke":1986}
print(my_dict)
print(my_dict["Nikita"])
print(my_dict.get("Alex", "Введен отсутствующий ключ"))
my_dict.update({"Simon":1952, "Nikon":1921})
temp_value = my_dict.pop("Kirill")
print(temp_value)
print(my_dict)
#_____Работа с множествами
print("Задачи с множествами:")
my_set = {53.,2617,53.,"Hello",11,11,11,4462,"Hello",86,32,32,12,53,53}
print(my_set)
my_set.add(99)
my_set.add(777)
my_set.remove(4462)
print(my_set)

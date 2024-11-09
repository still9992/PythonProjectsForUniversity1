# Задание "Средний балл":
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students) #Преобразуем множество в список *неупорядоченный
students.sort() #Упорядочим список студентов

#тут нужен цикл, но я в питоне циклы еще не знаю --> 
# --> цикл не заработал list indices must be integers or slices, not tuple
# i = len(grades)
# grades_avr = []
# for i in range(len(grades)):
#    grades_avr[i] = sum(grades[i])/len(grades[i])
#    print(i,grades_avr[i])

grades_avr = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), 
              sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), 
              sum(grades[4])/len(grades[4]), ]
report_dict =  dict(zip(students, grades_avr))
print(report_dict)


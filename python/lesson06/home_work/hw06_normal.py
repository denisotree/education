import school

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


mother1 = school.Person("Иванова", "Татьяна", "Васильевна")
father1 = school.Person("Иванов", "Николай", "Александрович")

mother2 = school.Person("Бойко", "Людмила", "Викторовна")
father2 = school.Person("Бойко", "Дмитрий", "Игоревич")

mother3 = school.Person("Остапенко", "Мария", "Дмитриевна")
father3 = school.Person("Остапенко", "Тимофей", "Cергеевич")

student1 = school.Student(mother1, father1, "Иванов", "Дмитрий", "Александрович")
student2 = school.Student(mother2, father2, "Бойко", "Тимур", "Дмитриевич")
student3 = school.Student(mother3, father3, "Остапенко", "Кирилл", "Тимофеевич")

geo_subj = school.Subject("География")
math_subj = school.Subject("Математика")
rus_subj = school.Subject("Русский язык")

math_teacher = school.Teacher(math_subj, "Васильева", "Наталья", "Борисовна")
geo_teacher = school.Teacher(geo_subj, "Борисова", "Варвара", "Степановна")
rus_teacher = school.Teacher(rus_subj, "Дмитриева", "Ольга", "Васильевна")

class1 = school.Class(5, "A")
class2 = school.Class(8, "a")
class3 = school.Class(1, "В")

class1.add_student(student1)
class1.add_teacher(math_teacher, rus_teacher, geo_teacher)
class2.add_student(student2)
class2.add_teacher(math_teacher, rus_teacher, geo_teacher)
class3.add_student(student3)
class3.add_teacher(math_teacher, geo_teacher)

school = school.School()
school.add_class(class1, class2, class3)

print("Классы школы: ", school._classes())
print(f"Ученики класса {class1.name} ", school.students(class1.name))
print(f"Предметы ученика {student2.full_name} ", school.subjects(student2.full_name))
print(f"Родители ученика {student2.full_name} ", school.parents(student2.full_name))
print(f"Учителя класса {class1.name} ", school.teachers(class1.name))

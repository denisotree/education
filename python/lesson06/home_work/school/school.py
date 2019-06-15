class Person:
    def __init__(self, last_name, first_name, middle_name):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name

    @property
    def full_name(self):
        return f"{self.lname} {self.fname[0]}.{self.mname[0]}."


class Subject:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, subject, lname, fname, mname):
        Person.__init__(self, lname, fname, mname)
        self.subject = subject


class Student(Person):
    def __init__(self, mother, father, lname, fname, mname):
        Person.__init__(self, lname, fname, mname)
        self.mother = mother
        self.father = father

    def parents(self):
        return [self.mother.full_name, self.father.full_name]


class Class:
    def __init__(self, number, ch):
        self.number = number
        self.ch = ch
        self.teachers = []
        self.students = []

    @property
    def name(self):
        return f"{self.number}{self.ch.upper()}"

    def add_teacher(self, *args):
        for a in args:
            self.teachers.append(a)

    def add_student(self, *args):
        for a in args:
            self.students.append(a)


class School:
    def __init__(self):
        self.classes = []

    def add_class(self, *args):
        for a in args:
            self.classes.append(a)

    def _classes(self):
        return [x.name for x in self.classes]

    def students(self, classname):
        students = [x.students for x in self.classes if x.name == classname]
        return [x.full_name for x in students[0]]

    def subjects(self, studentname):
        classes = [x for x in self.classes if studentname in [y.full_name for y in x.students]]
        return [x.subject.name for x in classes[0].teachers]

    def parents(self, studentname):
        class_students = [x.students for x in self.classes if studentname in [y.full_name for y in x.students]]
        students = [x for x in class_students[0] if studentname == x.full_name]
        return students[0].parents()

    def teachers(self, classname):
        teachers = [x.teachers for x in self.classes if x.name == classname]
        return [x.full_name for x in teachers[0]]


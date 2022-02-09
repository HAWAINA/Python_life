# Создать класс Person с атрибутами fullname, age, is_married
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

# Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
    def introduce_myself(self, full_name, age, is_married):
        print(f"fullname: {full_name}\n "
              f"age: {age}\n "
              f"is_married: {is_married}\n")

    def __str__(self):
        return f"full name {self.full_name}\n" \
               f"age {self.age}\n" \
               f"is married {self.is_married}\n" \

# Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        Person.__init__(self, full_name, age, is_married)
        self.marks = marks

# Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
    def average(self):
        print(sum(self.marks) / 5)

# Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
class Teacher(Person):
    salary = 45000

    def __init__(self, full_name, age, is_married, experience=3):
        Person.__init__(self, full_name, age, is_married)
        self.experience = experience

# Добавить в класс Teacher поле уровня класса salary
# Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
    def salary_average(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary/100*5) * (self.experience-3))
            return new_salary

# Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
teach = Teacher(full_name="Alex", age=36, is_married="married", experience=9)
print(f'Teacher_name: {teach.full_name}\n'
      f'Teacher_age: {teach.age}\n'
      f'Teacher_married: {teach.is_married}\n'
      f'Teacher_experience: {teach.experience}\n'
      f'Teacher_salary: {teach.salary_average()}\n')

# Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается методом как результат.
def create_students():
    st1 = Student(full_name="Dilyar", age="18", is_married="not married", marks={
        "History": 65,
        "Biology": 43,
        "Geography": 89,
        "Math": 23,
        "Physics": 77,
    })
    st2 = Student(full_name="Atosh", age="17", is_married="not married", marks={
        "History": 24,
        "Biology": 90,
        "Geography": 89,
        "Math": 45,
        "Physics": 67,
    })
    # print(f'{st2.full_name} {st2.age} {st2.is_married} {st2.marks}')
    st3 = Student(full_name="Ismet", age="18", is_married="married", marks={
        "History": 85,
        "Biology": 30,
        "Geography": 79,
        "Math": 35,
        "Physics": 77,
    })
    result = [st1, st2, st3]
    return result

# Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.
students = create_students()
for i in students:
    lst = []
    for marks in i.marks.values():
        lst.append(marks)
    print(f"Name: {i.full_name}\n"
          f"Age: {i.age}\n"
          f"Married: {i.is_married}\n"
          f"Average marks: {sum(lst)/len(lst)}\n")
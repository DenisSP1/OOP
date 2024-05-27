class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self .courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def courses(self):
        all_courses = ', '.join(self.courses_in_progress)
        return all_courses
    
    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)
        grade_for_lecturer = sum(all_grades) / len(all_grades)
        return round(grade_for_lecturer, 1)
    
    def compare_st(self, other_student):
        if isinstance(other_student, Student):
            b = self.average_grade() < other_student.average_grade()
            return b
        print('Не студент')
        return
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\nКурсы в процессе изучения: {self.courses()}\nЗавершенные курсы: {self.end_courses()}'

    def end_courses(self):
        all_end_courses = ', '.join(self.finished_courses)
        return all_end_courses

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []

    def compare(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            a = self.average_grade() < other_lecturer.average_grade()
            return a
        print('Не лектор')
        return
        
    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)
        grade_for_lecturer = sum(all_grades) / len(all_grades)
        return round(grade_for_lecturer, 1)
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
   
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'  

student_1 = Student('Paul', 'Freeman', 'male')
student_2 = Student('Robert', 'Downey', 'male')

lecturer_1 = Lecturer('Sam', 'Winchester')
lecturer_2 = Lecturer('Dean', 'Winchester')

reviewer_1 = Reviewer('Maria', 'Smith')
reviewer_2 = Reviewer('Tina', 'Humen')

mentor_1 = Mentor('Woody', 'Harrelson')
mentor_2 = Mentor('Nina', 'Richy')

student_1.courses_in_progress += ['Python', 'Java', 'C++']
student_1.grades.update({'Python':[9, 9, 3], 'Java':[9, 9, 8], 'C++':[10, 7, 9]})
student_1.finished_courses += ['JavaScript']

student_2.courses_in_progress += ['Python', 'Java', 'C++']
student_2.grades.update({'Python':[7, 9, 2], 'Java':[9, 9, 10], 'C++':[10, 10, 5]})
student_2.finished_courses += ['Framework']

lecturer_1.courses_in_progress += ['Python', 'Java', 'C++']
lecturer_1.grades.update({'Python':[5, 9, 2], 'Java':[5, 9, 10], 'C++':[5, 10, 5]})

lecturer_2.courses_in_progress += ['Python', 'Java', 'C++']
lecturer_2.grades.update({'Python':[9, 9, 2], 'Java':[9, 9, 9], 'C++':[10, 10, 9]})

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

help = ("""
    'Welcome to help menu: '
    'sag' - средняя оценка за дз конкретного курса у всех студентов
    'lag' - средняя оценка за лекции конкретного курса у всех лекторов
    'all_students' - все студенты
    'all_lecturers' - все лекторы
    'all_reviewers' - все ревьюверы
    'student_compare' - сравниваем студентов по средней оценке за ДЗ
    'lecturer_compare' - сравниваем лекторов по средней оценке за лекции

    'Course list: Python, Java, JavaScript'
""")

def average_grades(student_list, course):
    grade_list = []
    for student in student_list:
        if course in student.courses_in_progress and course in student.grades:
            avg = sum(student.grades.get(course)) / len(student.grades.get(course))
            grade_list.append(round(avg, 1))
    res = f'Средний балл за ДЗ по курсу {course} = {sum(grade_list) / len(grade_list)}'
    print(res)
    return res

def avg_grades(lecturer_list, course):
    grade_list = []
    for lecturer in lecturer_list:
        if course in lecturer.courses_in_progress and course in lecturer.grades:
            avg = sum(lecturer.grades.get(course)) / len(lecturer.grades.get(course))
            grade_list.append(round(avg, 1))
    res = f'Средняя оценка за лекцию по курсу {course} = {sum(grade_list) / len(grade_list)}'
    print(res)
    return res

def student_compare():
    if student_1 < student_2:
        print(
            f' Средняя оценка за дз {student_1.name} {student_1.surname} меньше средней оценки {student_2.name} {student_2.surname}')
        print(student_1 < student_2)
    elif student_1 > student_2:
        print(
            f' Средняя оценка за дз {student_1.name} {student_1.surname} больше средней оценки {student_2.name} {student_2.surname}')
        print(student_1 > student_2)
    elif student_1 == student_2:
        print(
            f' Средняя оценка за дз {student_1.name} {student_1.surname} равна средней оценки {student_2.name} {student_2.surname}')
        print(student_1 == student_2)

def lecturer_compare():
    if lecturer_1 < lecturer_2:
        print(
            f' Средняя оценка за лекции {lecturer_1.name} {lecturer_1.surname} меньше средней оценки {lecturer_2.name} {lecturer_2.surname}')
        print(lecturer_1 < lecturer_2)
    elif lecturer_1 > lecturer_2:
        print(
            f' Средняя оценка за лекции {lecturer_1.name} {lecturer_1.surname} больше средней оценки {lecturer_2.name} {lecturer_2.surname}')
        print(lecturer_1 > lecturer_2)
    elif lecturer_1 == lecturer_2:
        print(
            f' Средняя оценка за лекции {lecturer_1.name} {lecturer_1.surname} равна средней оценки {lecturer_2.name} {lecturer_2.surname}')
        print(lecturer_1 == lecturer_2)

def start():
    while True:
        answer = input('\nВведите команду или Help для справки: ').lower()
        if answer.lower() == 'help':
            print(help)
        elif answer == 'sag':
            course_name = input('Введите название курса: ').capitalize()
            average_grades(student_list, course_name)
        elif answer == 'lag':
            course_name = input('Введите название курса: ').capitalize()
            avg_grades(lecturer_list, course_name)
        elif answer == 'all_students':
            print(f'\nСтуденты: \n{student_1} \n{student_2}')
        elif answer == 'all_lecturers':
            print(f'\nЛекторы: \n{lecturer_1} \n{lecturer_2}')
        elif answer == 'all_reviewers':
            print(f'\nРевьюверы: \n{reviewer_1} \n{reviewer_2}')
        elif answer == 'student_compare':
            student_compare()
        elif answer == 'lecturer_compare':
            lecturer_compare()
        elif answer == 'quit':
            print('Вы вышли из программы!')
            break
        else:
            print('Неверная команда!')

start()
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.courses_attached:
                lecturer.grades.setdefault(course, []).append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def average_grade(self):
        total_grades = 0
        quantity_total_grades = 0
        for value in self.grades.values():
                quantity_total_grades += len(value)
                total_grades += sum(value)

        result = total_grades / quantity_total_grades
        return result

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return (f'Имя:{self.name}\n' 
                f'Фамилия:{self.surname}\n' 
                f'Средняя оценка за лекции:{self.average_grade()}\n' 
                f'Курсы в процессе изучения:{self.courses_in_progress}\n' 
                f'Завершенные курсы:{self.finished_courses}\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.courses_attached:
                student.grades.setdefault(course, []).append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}\n' f'Фамилия:{self.surname}\n'


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []

    def average_grade(self):
        total_grades = 0
        quantity_total_grades = 0
        for value in self.grades.values():
            quantity_total_grades += len(value)
            total_grades += sum(value)

        result = total_grades / quantity_total_grades
        return result

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return (f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}\n' 
                f'Средняя оценка за лекции:{self.average_grade()}\n')



Student_1 = Student(name='Tim', surname='Baranov', gender="male")
Student_1.finished_courses.append("python с нуля")
Student_1.grades = {'Java': [10, 2, 6], 'Git': [10, 9, 8]}
Student_1.courses_in_progress = ['Java' , 'Git']
Student_1.courses_attached = ['Java']

Student_2 = Student(name='Kolya', surname='Smirnov', gender="male")
Student_2.finished_courses.append("Java")
Student_2.grades = {'Python': [8, 7, 6], 'HTML': [8, 7, 6], 'Java': [10, 6]}
Student_2.courses_in_progress = ['Python' , 'HTML']
Student_2.courses_attached = ['Paskal', 'Python', 'HTML', 'Java']



Lecturer_1 = Lecturer(name = 'Ivan', surname = 'Sokolov')
Lecturer_1.courses_attached = ['Java','Git', 'C++']
Lecturer_1.grades = {'Java': [12, 6], 'C++': [12, 6]}
Lecturer_1.finished_courses = ["HTML"]
Lecturer_1.courses_in_progress = ['Java','Git']

Lecturer_2 = Lecturer(name = 'Vitya', surname = 'Dalov')
Lecturer_2.courses_attached = ['Paskal', 'C++']
Lecturer_2.grades = {'Paskal': [7, 5], 'C++': [7, 5]}
Lecturer_2.finished_courses = ["C#"]
Lecturer_2.courses_in_progress = ['C++', 'Paskal']



Reviewer_1 = Reviewer(name = 'Stas', surname = 'Fedorov')
Reviewer_1.courses_attached = ["Paskal", 'Python']

Reviewer_2 = Reviewer(name = 'Nikita', surname = 'Samoilov')
Reviewer_2.courses_attached = ["C++"]

students_list = [Student_1, Student_2]
lecturers_list = [Lecturer_1, Lecturer_2]

def get_av_grade_all_students(students_list, course):
    av_grade = 0
    i = 0
    for student in students_list:
        if course in student.courses_attached:

            av_grade += sum(student.grades[course])
            i += len(student.grades[course])

    if i > 0:
        return av_grade / i
    else:
        return "У студента нет оценок"

def get_av_grade_all_lecturers(lecturers_list, course):
    av_grade = 0
    i = 0
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            av_grade += sum(lecturer.grades[course])
            i += len(lecturer.grades[course])

    if i > 0:
        return av_grade / i
    else:
        return "У лектора нет оценок"




# print(Student_1)
# print(Lecturer_1)
# print(Reviewer_1)

# print(Student_1.__gt__(Student_2))
#print(Student_1.average_grade())
#print(Student_2.average_grade())
# print(Student_1.rate_lecturer(lecturer = Lecturer_1 ,course="Java",grade= 8))
# print(Student_1.__str__())

# print(Reviewer_1.rate_hw(student = Student_2, course = "Python", grade = 10))
# print(Reviewer_1.__str__())

# print(Lecturer_1.__str__())
# print(Lecturer_1.average_grade())

print(get_av_grade_all_students(students_list, 'Java'))
print(get_av_grade_all_lecturers(lecturers_list, 'C++'))
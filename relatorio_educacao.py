import csv

def create_student(student):
    return {
        'id': student[0],
        'name': student[1],
        'mother_name': student[2],
        'father_name': student[3],
        'gender': student[4],
        'birth_date': student[5]
    }

with open('alunos.csv', 'r') as file:
    data = list(csv.reader(file, delimiter=';'))
    students = [create_student(student) for student in data[1:]]

    print(students)

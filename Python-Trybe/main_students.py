recovery_students = []

def students_note():
    with open("students.txt", mode='r', encoding= 'utf-8') as grades_file:
        for line in grades_file:
            student_grade = line
            student_grade = student_grade.split(" ")
            if int(student_grade[1]) < 6:
                recovery_students.append(student_grade[0])

    with open("recovering_students.txt", mode='w', encoding='utf-8') as recovery_students_file:
        print(recovery_students)
        recovery_students_file.writelines(recovery_students)

if __name__ == "__main__":
    students_note()
import csv

with open("graduacao_unb.csv", encoding='utf-8') as file:

    graduation_file = csv.reader(file, delimiter= ",", quotechar= '"')

    header, *data = graduation_file

group_by_department = {}

for row in data:
    department = row[15]
    if department not in group_by_department:
        group_by_department[department] = 1
    group_by_department[department] += 1

with open("filter_courses_gradutation_unb.csv", 'w', encoding= 'utf-8') as file:
    filter_writer = csv.writer(file)


    headers = [
        'Departamento de cursos',
        'Total de curso',
            ]
    filter_writer.writerow(headers)

    for department, grade in group_by_department.items():
        row = [
            department,
            grade
        ]
        filter_writer.writerow(row)
from time import sleep

# Permitir cadastrar alunos e suas notas. OK
# Calcular a média de cada aluno. OK
# Mostrar a lista de alunos aprovados (média ≥ 7) e reprovados (média < 7). OK
# Mostrar a maior e a menor média da turma. OK

cadaluno = {}
listaaluno = []
maior = menor = 0
def StudentsNotes():

    while True:

        cadaluno.clear()
        cadaluno['name'] = str(input('Type the name of the student: ')).strip().capitalize()
        cadaluno['grade1'] = int(input(f'Type the first grade of the {cadaluno["name"]}: '))
        cadaluno['grade2'] = int(input('And here, the second note: '))
        cadaluno['average'] = (cadaluno['grade1'] + cadaluno['grade2']) / 2
        listaaluno.append(cadaluno.copy())
        choice = str(input('Would you like to finish this? [Y,N]: ')).strip().upper()[0]
        while choice not in "YN":
            print('Wrong Choice, Sir... please, type again...')
            sleep(0.7)
            choice = str(input('Would you like to finish this? [Y,N]: ')).strip().upper()[0]
        if choice in "Y":
            break
    print('=-=-=-= DATES OF THE STUDENTS =-=-=-=')

    for aluno in listaaluno:
        print(f'-Name: {aluno["name"]}')
        sleep(0.3)
        print(f'-Grade 1: {aluno["grade1"]}')
        sleep(0.3)
        print(f'-Grade 2: {aluno["grade2"]}')
        sleep(0.3)
        print(f'-Average: {aluno["average"]}')
        sleep(0.3)
        if aluno["average"] < 7:
            print(f'The {aluno["name"]} unfortunately is failed.')
        else:
            print(f'Congratulations! The {aluno["name"]} is approved!')
        sleep(0.8)

        maior = menor = listaaluno[0]["average"]  

    for aluno in listaaluno:
        media = aluno["average"]
        if media > maior:
            maior = media
        elif media < menor:
            menor = media

    print('=-=-=-=-=-=-=-=')
    print(f'The highest score recorded was {maior} and the lowest score was {menor}')

StudentsNotes()

print('Come back soon!')




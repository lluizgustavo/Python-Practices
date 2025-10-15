names = ['Jullyan', 'Gustavo', 'Alessandro', 'Luan']

def main(index):
    bigger_name = ''
    for name in index:
        if len(name) > len(bigger_name):
            bigger_name = name
    return bigger_name

print(main(names))


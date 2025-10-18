names = ['Jullyan', 'Gustavo', 'Alessandro', 'Luan']
def main(sring):
    for name in sring:
        if len(name) > len(sring):
            sring = name
    return sring

print(main(names))


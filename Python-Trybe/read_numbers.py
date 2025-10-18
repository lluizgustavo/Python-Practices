import sys

list_num = []

def test_read_number():
    while True:
        num = str(input('Type a number: ')).strip().upper()[0]
        if not num.isnumeric():
            print('Error! You type a letter, not a number, try it again....', file= sys.stderr)
            continue 
        else:
            list_num.append(num)            
        choice = str(input('Would you like to continue? [Y,N]: ')).strip().upper()[0]
        while choice not in 'YNyn':
            print('Please, type a valid choice.')
            choice = str(input('Would you like to continue? [Y,N]: ')).strip().upper()[0]

        if isinstance(choice, str):
            if choice == 'N':
                print('See ya!')
                break
        elif choice == 'Yy':
            continue
        else:
            print('Error! Choice inst accepted, try it again...', file = sys.stderr)
            continue


    print(f'List before with the numbers separated: {list_num}')
    print('-=' * 5)
    new_list = sum([int(x) for x in list_num])
    print(f'List now with the sum wtih all of the numbers: {new_list}')


        

(test_read_number())
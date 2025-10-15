class String:
    def __init__(self, char: str) -> None:
        self.char = char[0].lower()
        self.string = ''
        self.list_strings = []
        print(f'Char reserved: {self.char}')


    def add_string(self, string):
        if string in self.list_strings:
            print('This string is still in the list.')
            return
        self.list_strings.append(string)
        print('String added.')

    
    def show_list_string(self):
        print(f'LOADING LIST WITH CHAR {self.char.upper()}')
        print('-=' * 10)
        for self.sentence in self.list_strings:
            if self.sentence[0] == 'g':
                print(self.sentence)
        

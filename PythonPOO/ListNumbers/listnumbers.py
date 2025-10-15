class ListIntNumbers:


    def __init__(self, number: int) -> None:
        self.list_numbers = [number]

    def add_number(self, number: int) -> None:
        self.list_numbers.append(number)
        print('Number Sucesfully added.')
    
    def show_total_sum(self):
        self.total_sum = sum(self.list_numbers)
        print(f'The sum is: {self.total_sum}')
    

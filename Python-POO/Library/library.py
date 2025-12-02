from typing import Any, Union


class Library:
    def __init__(self, title: str , author: str, year: int, code: int,) -> None:       
        self.__title = title 
        self.__author = author
        self.__year = year
        self.__code = code
        self.available = True
        print('Book sucesfully added!')

    def loan_book(self):
        if self.available == False:
            print('This book is not available / on stock.')
            return
        print('Book sucesfully borrowed!')
        self.available = False
        
    def return_book(self):
        if self.available == True:
            print('This book is available / on stock.')
            return
        print('Book sucesfully returned!')

            
class User:
    loan_limit = 1

    def __init__(self, name, registration):
        self.name = name
        self.registration = registration
    

class Student(User):
    loan_limit = 3

    def __init__(self, name, registration, workload: int ):
        self.workload = workload
        super().__init__(name, registration)


class Teacher(User): 
    loan_limit = 5




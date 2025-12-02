from datetime import datetime
from random import randint


from random import randint

class Person:
    current_year = 2025

    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def eat(self, food):
        if self.talking:
            print(f'{self.name} cannot eat while talking...')
            return
        if self.eating:
            print(f'{self.name} is already eating!')
            return
        
        print(f'{self.name} is eating {food}')
        self.eating = True
    
    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return
        print(f'{self.name} stopped eating.')
        self.eating = False

    def talk(self):
        if self.eating:
            print(f'{self.name} cannot talk while eating.')
            return
        
        if self.talking:
            print(f'{self.name} is already talking.')
            return
        
        print(f'{self.name} is talking...')
        self.talking = True
    
    def stop_talking(self):
        if not self.talking:
            print(f'{self.name} is not talking.')
            return
        print(f'{self.name} stopped talking.')
        self.talking = False

    def get_birth_year(self):
        print(self.current_year - self.age)
    
    @classmethod
    def by_birth_year(cls, name, birth_year):
        age = cls.current_year - birth_year
        return cls(name, age)
    
    @staticmethod
    def get_id():
        id = randint(1, 10000)
        return id

from people import Person

p1 = Person('Luiz', 18)

p1.eat('Apple')
p1.eat('Pineapple')
p1.stop_eating()
p1.talk()
p1.stop_talking()
p1.get_birth_year()
print(Person.get_id())

print(p1.get_id)
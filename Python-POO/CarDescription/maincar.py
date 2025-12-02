from car import Car


    
car1 = Car('Chevette', 1980, 93)
car2 = Car('Audi', 2016, 109)

print(car1.increase_speed(7))
print(car2.decrease_speed(115))
print(car2.decrease_speed(22))

car1.show_car_description()
car2.show_car_description()
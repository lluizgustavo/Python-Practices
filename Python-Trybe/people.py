import area

people_per_square_meter = 2
base_square = 60
high_square = 45

people_area = area.rectangle(base_square, high_square) * people_per_square_meter
print(f'Aproximally, therell be {people_area} in that party.')
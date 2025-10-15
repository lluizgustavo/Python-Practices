def Triangle(set1: int, set2: int, set3: int):
    if set1 == set2 == set3:
        return f'Its an equilateral triangle.'
    elif set1 == set2 and set1 != set3 or set2 == set3 and set2 != set1 or set3 == set1 and set3 != set2:
        return f'Its an isosceles triangle.'
    elif set1 != set2 != set3:
        return f'Its a scalene triangle'
    
print(Triangle(4,2,1))
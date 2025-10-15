PI = 3.14

def square(side):
    return side ** 2


def rectangle(base, high):
    return base * high

def circle(radius):
    return PI * radius * radius

if __name__ == "__main__":
    print(f'Square area:', square(10))
    print(f'Retangle area:', rectangle(3, 4))
    print('Circle area', circle(5))
def smaller(numbers: list):
    smallest = numbers[0]  # começa assumindo que o primeiro é o menor
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

listnum = [5, 2, 9, 1, 7]
print(smaller(listnum))
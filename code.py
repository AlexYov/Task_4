def func(numbers):
    list = [number for number in numbers if numbers.count(number) < 2]
    return list

numbers = [1, 9, 8, 8, 7, 6, 1, 6]
print(func(numbers))

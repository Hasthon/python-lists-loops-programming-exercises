arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]


def sumods():
    sum = 0
    for number in arr:
        if number % 2 == 1:
            sum += number
    return sum

print(sumods())
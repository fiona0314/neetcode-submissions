def add_two_numbers() -> int:
    numbers = input()
    sum_add = 0
    for i in numbers.split(","):
        sum_add += int(i)

    return sum_add



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

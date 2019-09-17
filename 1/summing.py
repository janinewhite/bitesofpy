def sum_numbers(numbers=None):
    total = 0
    if numbers==None:
        for num in range(1,101):
            total += num
    elif len(numbers)==0:
        pass
    else:
        for num in numbers:
            total += int(num)
    return total

#numbers = []
#print(str(sum_numbers(numbers)))
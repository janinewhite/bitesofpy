def sum_numbers(numbers=None):
    total = 0
    if numbers==None or len(numbers)==0:
        for num in range(1,101):
            total += num
    else:
        for num in numbers:
            total += int(num)
    return total

#numbers = []
#print(str(sum_numbers(numbers)))
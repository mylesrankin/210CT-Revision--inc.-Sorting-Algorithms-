def sumDigits(number):
    result = 0
    number = str(number)
    for i in number:
        result = result + int(i)
    return result

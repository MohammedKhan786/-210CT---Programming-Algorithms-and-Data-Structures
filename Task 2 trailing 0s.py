def trailing(number):
    trailing = 0
    while number > 1:
        number = number // 5
        trailing = number + trailing
    return(trailing)
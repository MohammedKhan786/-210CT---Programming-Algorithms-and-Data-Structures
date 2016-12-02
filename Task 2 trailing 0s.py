#Count the number of trailing 0s in a factorial number. 

def trailing(number):
    trailing = 0
    #divide by 5 and add up the answer until the answer is 1
    while number > 1:
        number = number // 5
        trailing = number + trailing
    return(trailing)

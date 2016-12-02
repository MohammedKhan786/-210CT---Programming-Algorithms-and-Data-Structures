#Write a recursive function (pseudocode and code) to check if a number n is prime (hint:
#check whether n is divisible by any number below n).


def primecheck (N):
    # check in N 2 and if it is return true
    if N == 2:
        return True
    # check if N is less then 2 because if n is less the 2 it can not be a prime
    # check if there a remainder when dividing by 2 
    elif N < 2 or N%2 == 0:
        return False
    #take 1 away from N and call prime
    else:
        check = N - 1
        prime(N, check)


def prime (N, check):
    remainder = N % check
    # if remainder = 0 that mean that N can be dividing by another number with mean it on a prime
    if remainder ==0:
        print (False)
    # if check <= 2 then it has check all the number belowe N to check if there was a remainder
    elif check <= 2:
        print (True)
     #take 1 away from N and call prime
    else:
        check = check -1
        prime (N, check)

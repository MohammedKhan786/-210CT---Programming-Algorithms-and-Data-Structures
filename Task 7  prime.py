def prime (N, check):
    remainder = N % check
    if remainder ==0:
        print (False)
    elif check <= 2:
        print (True)
    else:
        check = check -1
        prime (N, check)
        
    

def primecheck (N):
    if N == 2:
        return True
    elif N < 2 or N%2 == 0:
        return False
    else:
        check = N - 1
        prime(N, check)
        

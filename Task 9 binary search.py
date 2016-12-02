def binarysearch(L, low, hight):

    if len(L) == 0:
        return False

    start = 0
    end = len(L)-1

    while start <= end:
        midpoint = (start + end)//2
        if low < L[midpoint] and hight > L[midpoint]:
            return True
        elif hight < L[midpoint]:
            end = midpoint - 1
        elif low > L[midpoint]:
             start = midpoint + 1
        else:
            return False 

    if low < L[midpoint] and hight > L[midpoint]:
            return True
    else:
            return False 

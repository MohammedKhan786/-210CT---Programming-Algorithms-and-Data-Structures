LReverse=[]


def reverse(I):
    L = I.split()
    while len(L) > 0:
        remaining = len(L) - 1
        num = L.pop(remaining)
        LReverse.append(num)
        if len(L) == 0:
            return LReverse



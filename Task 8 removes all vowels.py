def removevowels (S):
    if len(S) == 0:
        return S
    elif S[0] == "a" or S[0] == "A":
        return removevowels(S[1:])
    elif S[0] == "e" or S[0] == "E":
        return removevowels(S[1:])
    elif S[0] == "i" or S[0] == "I":
        return removevowels(S[1:])
    elif S[0] == "o" or S[0] == "O":
        return removevowels(S[1:])
    elif S[0] == "u" or S[0] == "U":
        return removevowels(S[1:])
    else:
        return S[0] + removevowels(S[1:])
        


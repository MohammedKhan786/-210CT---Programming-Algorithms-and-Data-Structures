def order(L):
    L.append (0)
    Csorting = []
    Lsorted = []
    Ccount = 1  
    Lcount = 0

    for i in range(0,len(L)-1):
        number = (L[i])
        if L[i] < L[i+1]:
            Ccount = Ccount + 1
            Csorting.append (number)
        if L[i] >= L[i+1] and Ccount > Lcount:
            Csorting.append (number)
            Lcount = Ccount
            Ccount = 1
            Lsorted=Csorting
            Csorting=[]
        if L[i] >= L[i+1] and Ccount < Lcount:
             Ccount = 1
             Csorting=[]
    return(Lsorted)
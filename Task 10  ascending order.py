#Given a sequence of n integer numbers, extract the sub-sequence of maximum length which is in
#ascending order. Example input: L = [1,2,3,4,1,5,1,6,7] Output: [1,2,3,4]


def order(L):
    L.append (0)
    Csorting = []
    Lsorted = []
    Ccount = 1  
    Lcount = 0

    for i in range(0,len(L)-1):
        number = (L[i])
        # if [i] is bigger then [i+1] then add one to Ccount and add L[i] to Csorting and repeat until [i] is less or equal to [i+1]
        if L[i] < L[i+1]:
            Ccount = Ccount + 1
            Csorting.append (number)
        # if [i] is less or equal to [i+1] and Ccount is bigger Lcount replace Lcount with Ccount and Lsorted with Csorting
        if L[i] >= L[i+1] and Ccount > Lcount:
            Csorting.append (number)
            Lcount = Ccount
            Ccount = 1
            Lsorted=Csorting
            Csorting=[]
         # if [i] is less or equal to [i+1] and Ccount is less then Lcount reset Ccount and Csorting
        if L[i] >= L[i+1] and Ccount < Lcount:
             Ccount = 1
             Csorting=[]
    return(Lsorted)

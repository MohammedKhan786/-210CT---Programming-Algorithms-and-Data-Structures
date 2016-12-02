#Write the pseudocode and code for a function that reverses the words in a sentence. Input:
#"This is awesome" Output: "awesome is This". Give the Big O notation.
    
LReverse=[]

#remove the last word and add it to the reverses list 
def reverse(I):
    L = I.split()
    while len(L) > 0:
        remaining = len(L) - 1
        num = L.pop(remaining)
        LReverse.append(num)
        if len(L) == 0:
            return LReverse

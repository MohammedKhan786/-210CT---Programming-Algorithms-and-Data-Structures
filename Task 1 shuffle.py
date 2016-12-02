#Write a function that randomly shuffles an array of integers and explain the rationale behind its implementation.

import random
shuffled=[]

def shuffle(L):
    while len(L) > 0:
        remaining = len(L) - 1
        index = random.randint(0, remaining)
        num = L.pop(index)
        shuffled.append(num)
        if len(L) == 0:
            return shuffled

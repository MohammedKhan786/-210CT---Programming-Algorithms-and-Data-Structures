#Write the pseudocode for a function which returns the highest perfect square which is less or equal to
#its parameter (a positive integer). Implement this in the programming language of your choice

def perfectsquare(Number):
    N = 0
    square = 0

    while Number >= square:
        N = N + 1
        square = N * N
        
        
    N = N - 1
    square = N * N
    return (square)
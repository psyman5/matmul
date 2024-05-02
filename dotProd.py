def dotProd(a, b):

    '''Dot product of two lists. Used in matMul.'''

    sumDot = 0 
    for index, element in enumerate(a):
        x = element * b[index]
        
        sumDot += x

    return sumDot


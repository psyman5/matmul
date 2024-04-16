def dotProd(a, b):

    '''Dot product of two matrices. Used in multMatrix.'''

    sumDot = 0
    for index, element in enumerate(a):
        x = element * b[index]
    
        sumDot += x

    return sumDot


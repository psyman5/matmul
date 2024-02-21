def dotProd(a, b):
    sumDot = 0
    for index, element in enumerate(a):
        x = element * b[index]
    
        sumDot += x

    return sumDot


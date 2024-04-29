from matrixByMatrixMult import matMul
def takeExponent(matrix, power):

    '''Takes the exponent of a given matrix to a given power. Returns a matrix object.'''
    
    if power == 2:
        newMat = matMul(matrix, matrix)
    else:
        for x in range(power):
            newMat = matMul(matrix, newMat)
    return newMat
        
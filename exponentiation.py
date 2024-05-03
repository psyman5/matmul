from matrixByMatrixMult import matMul
from matrixClass import matrix
def takeExponent(mat, power):

    '''Takes the exponent of a given matrix to a given power. Returns a matrix object.'''

    newMat = mat
    
    for x in range(power):
        newMat = matMul(mat, newMat)

    return newMat
        
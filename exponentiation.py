from matrixByMatrixMult import multMatrix
def takeExponent(matrix, power):
    
    newMat = multMatrix(matrix, matrix)

    for x in range(power):
        newMat = multMatrix(matrix, newMat)

    newMat.displayMatrix(newMat.elements)

    return newMat
        
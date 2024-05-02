from matrixClass import matrix
from dotAdd import dotAdd
from dotProd import dotProd
from exponentiation import takeExponent
from getTrace import getTrace
from matrixByMatrixMult import matMul
from scalarMult import scalarMult
from sparseMatrixEncoder import matrixToCode
from sparseMatrixEncoder import codeToMatrix
from createIdentityMatrix import CreateIdentityMatrix
from getDiagonal import getDiagonal


def testFunctions():

    for x in range(30): #tests square matrices up to given size
        testMatrix = matrix(x,x,[],[_**2 for _ in range(x**2)], False)
        testMatrix.constructMatrix()

        testMatrix2 = matrix(x,x,[],[x for x in range(x**2)], False)
        testMatrix2.constructMatrix()

        takeExponent(testMatrix, 2)
        getTrace(testMatrix)
        getDiagonal(testMatrix)
        matMul(testMatrix, testMatrix2)
        scalarMult(testMatrix, 3)
        matrixToCode(testMatrix)
        codeToMatrix(testMatrix, matrixToCode(testMatrix))
        CreateIdentityMatrix(x)
    
    for x in range(30): # nonsquare, some tests don't apply
        testMatrix = matrix(x+1,x,[],[_**2 for _ in range(x*(x+1))], False)
        testMatrix.constructMatrix()

        testMatrix2 = matrix(x, x+1,[],[x for x in range(x*(x+1))], False)
        testMatrix2.constructMatrix()
        takeExponent(testMatrix, x)
        matMul(testMatrix, testMatrix2)
        
        scalarMult(testMatrix, x)
        matrixToCode(testMatrix)

    for x in range(30): # nonsquare, some tests don't apply
        testMatrix = matrix(x,x+1,[],[_**2 for _ in range(x*(x+1))], False)
        testMatrix.constructMatrix()

        testMatrix2 = matrix(x+1,x,[],[x for x in range(x*(x+1))], False)
        testMatrix2.constructMatrix()

        takeExponent(testMatrix, x)
        matMul(testMatrix, testMatrix2)
        scalarMult(testMatrix, x)
        matrixToCode(testMatrix)
    
    return 0

matrix1 = matrix(3,2, [] , [x for x in range(6)], True)
matrix1.constructMatrix()

matrix2 = matrix(2,3, [] , [x for x in range(6)], True)
matrix2.constructMatrix()

matrix1.transposeMatrix()
matrix1.transposeMatrix()

matrix2.transposeMatrix()
matrix2.transposeMatrix()
from matrixClass import matrix
from dotAdd import dotAdd
from dotProd import dotProd
from exponentiation import takeExponent
from getTrace import getDiagonalAndTrace
from matrixByMatrixMult import multMatrix
from scalarMult import scalarMult
from sparseMatrixEncoder import matrixToCode
from sparseMatrixEncoder import codeToMatrix
import random

random.seed(999)


testMatrix = matrix(100,100,None,[random.random()*x for x in range(100**2)], None, False)

testMatrix.constructMatrix()

testMatrix2 = matrix(100,100,None,[random.random()*x for x in range(100**2)], None, False)

testMatrix2.constructMatrix()

testMatrix3 = matrix(100,100, None,[], None, False )

testMatrix3.constructMatrix()

#dotAdd(testMatrix,testMatrix2)

#dotProd(testMatrix, testMatrix2)

takeExponent(testMatrix,3)

getDiagonalAndTrace(testMatrix)[0]

getDiagonalAndTrace(testMatrix)[1]

multMatrix(testMatrix,testMatrix2)

scalarMult(testMatrix,0)

matCode = matrixToCode(testMatrix)

codeToMatrix(testMatrix3, matCode)














import timeit
from matrixClass import matrix
from matrixByMatrixMult import multMatrix
from exponentiation import takeExponent


#matrixOne = matrix(2,2,[],[x for x in range(2**2)], [], True)
#matrixTwo = matrix(2,2,[],[x for x in range(2**2)], [], True)

matrixOne = matrix(8,8,[],[0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0], [], True)
matrixTwo = matrix(1,8,[],[2,2,2,3,2,2,3,2], [], True)

matrixOne.constructMatrix(elements=matrixOne.elements,rows=matrixOne.rows, 
                          columns=matrixOne.columns, entries= matrixOne.entries, constructFlag= matrixOne.constructFlag)

matrixTwo.constructMatrix(elements=matrixTwo.elements,rows=matrixTwo.rows, 
                          columns=matrixTwo.columns, entries= matrixTwo.entries,  constructFlag= matrixTwo.constructFlag)


#matrixTwo.columnizeMatrix(matrixTwo.elements, [], matrixTwo.columns, matrixTwo.rows)

#multMatrix(matrixOne, matrixTwo)
takeExponent(matrix=matrixOne, power = 300)








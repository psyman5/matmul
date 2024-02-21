from matrixClass import matrix
from matrixByMatrixMult import multMatrix


matrixOne = matrix(3,1,[],"1,2,3".split(','), [])
matrixTwo = matrix(1,3,[],"4,5,6".split(','), [])

matrixOne.constructMatrix(elements=matrixOne.elements,rows=matrixOne.rows, 
                          columns=matrixOne.columns, entries= matrixOne.entries)

matrixTwo.constructMatrix(elements=matrixTwo.elements,rows=matrixTwo.rows, 
                          columns=matrixTwo.columns, entries= matrixTwo.entries)


#matrixTwo.columnizeMatrix(matrixTwo.elements, [], matrixTwo.columns, matrixTwo.rows)

multMatrix(matrixOne, matrixTwo)









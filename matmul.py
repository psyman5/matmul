import timeit
from matrixClass import matrix
from scalarMult1 import scalarMult1
from scalarMult2 import scalarMult2


matrixOne = matrix(4,4,[],[x for x in range(16)])
matrixTwo = matrix(2,2,[],"5,6,7,8".split(','))

matrixOne.constructMatrix(elements=matrixOne.elements,rows=matrixOne.rows, 
                          columns=matrixOne.columns, entries= matrixOne.entries)


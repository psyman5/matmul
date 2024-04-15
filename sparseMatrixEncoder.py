from matrixClass import matrix

#sampleSparseMatrix = matrix(4,4, [0,2,0,0,3,1,8,7,9,0,0,1,0,0,0,4], [], [] ,constructFlag = True)

sampleSparseMatrix = matrix(4,4,[],[0,2,0,0,3,1,8,7,9,0,0,1,0,0,0,4], [], True)

sampleSparseMatrix.constructMatrix(elements=sampleSparseMatrix.elements,rows=sampleSparseMatrix.rows, 
                          columns=sampleSparseMatrix.columns, entries= sampleSparseMatrix.entries, constructFlag= sampleSparseMatrix.constructFlag)

print(sampleSparseMatrix.getSparsity())





def encodeSpareMatrix(matrix):
    pass

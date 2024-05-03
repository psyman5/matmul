from dotProd import dotProd
from matrixClass import matrix

def matMul(m1, m2): #TODO: move to Strassen's Algorithm
    
    '''Multiplies two Matrix objects via the naive method.'''

    if m1.rows != m2.columns:
        print("Incompatible Matrices!")
        print((m1.rows, m1.columns), (m2.rows, m2.columns))
        raise ValueError
    
    rowCounter = 0
    columnCounter = 0
    
    newMat = matrix(rows=m1.rows, columns=m2.columns, elements= [], # create a new matrix,
                    entries = [], constructFlag = False)
    
    m2.transposeMatrix() #transpose for multiplication
    #m2.displayMatrix()

    if m2.rows != 1:
        for rowIndexA, rowA in enumerate(m1.elements):
                for rowIndexB, rowB in enumerate(m2.elements):
                    #print(rowA, rowB)
                    newMat.entries.append(dotProd(rowA, rowB))

    else:
        for rowIndexA, rowA in enumerate(m1.elements):
            newMat.entries.append(dotProd(rowA, m2.elements[0]))
            
    

    newMat.constructMatrix() #construct the matrix
    
    m2.transposeMatrix() #transpose matrix back

    return newMat #return the matrix

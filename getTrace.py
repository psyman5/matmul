from matrixClass import matrix

def getTrace(matrix):

    '''Returns trace and the diagonal of a given matrix object.'''

    if matrix.rows != matrix.columns:
        print("Non-Square Matrix")
    
    else:

        diagonalList = []

        for index, row in enumerate(matrix.elements):
            diagonalList.append(row[index])
            
        trace = sum(diagonalList)

        del diagonalList

        return trace

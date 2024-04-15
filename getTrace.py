from matrixClass import matrix

def getDiagonalAndTrace(matrix):

    '''Returns a list of matrix elements along the diagonal. RETURN USES NORMAL MATRIX I,J NOTATION. DOES NOT USE ZERO BASED INDEXING. '''
    if matrix.rows != matrix.columns:
        print("Non-Square Matrix")
    
    else:

        diagonalList = []

        for index, row in enumerate(matrix.elements):
            diagonalList.append(row[index])
            
        trace = sum(diagonalList)

        return (trace, diagonalList)

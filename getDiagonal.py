from matrixClass import matrix

def getDiagonal(matrix):

    if matrix.rows != matrix.columns:
        print("Non-Square Matrix")
    
    else:

        diagonalList = []

        for index, row in enumerate(matrix.elements):
            diagonalList.append(row[index])
        
        diagTuple = tuple(diagonalList)

        del diagonalList

        return diagTuple
from matrixClass import matrix

def getDiagonalAndTrace(matrix):
    if matrix.rows != matrix.columns:
        print("Non-Square Matrix")
    
    else:

        diagonalList = []

        for index, row in enumerate(matrix.elements):
            diagonalList.append(row[index])
            
        trace = sum(diagonalList)

        return (trace, diagonalList)

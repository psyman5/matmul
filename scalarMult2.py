from matrixClass import matrix
def scalarMult2(num, mat):
    rowCounter = 0
    columnCounter = 0

    for row in mat.elements:
        for element in row:
            matrix.elements[matrix.elements.index(row)][row.index(element)] = num * element
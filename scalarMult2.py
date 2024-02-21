from matrixClass import matrix

def scalarMult2(num, mat):
    for row in mat.elements:
        for element in row:
            mat.elements[mat.elements.index(row)][row.index(element)] = num * element
from matrixClass import matrix

def scalarMult(num, mat):

    '''Multiplies a Matrix object by a scalar value.'''

    for row in mat.elements:
        for element in row:
            mat.elements[mat.elements.index(row)][row.index(element)] = num * element
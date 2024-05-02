from matrixClass import matrix
import random

def matrixToCode(matrix):

    '''Encodes a matrix into a list of tuples containing row, column, and value information for non-zero entries, respectively.'''

    encoded = []

    for index, row in enumerate(matrix.elements):
        for col, element in enumerate(row):
            if element != 0:
                encoded.append((matrix.elements.index(row)+1, col+1, element))
            else:
                pass
    return encoded

def codeToMatrix(matrix, matrixEncoding):

    '''Creates and constructs matrix from an encoding done by matrixToCode. Returns a matrix object.'''

    matrix.elements = [[0 for x in range(matrix.columns)] for row in range(matrix.rows)]

    for element in matrixEncoding:
        #print(element[0])
        matrix.setNumber(element[0], element[1], element[2])
    
    return
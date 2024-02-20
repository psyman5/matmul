from matrixClass import matrix
def scalarMult1(num, mat):
    rowCounter = 0
    columnCounter = 0

    rawEntries = mat.decodeElements(mat.elements, mat.rows, mat.columns)

    multipliedEntries = []

    for entry in rawEntries:
        multipliedEntries.append(num * int(entry))
    
    mat.encodeElements(entries = multipliedEntries, columns = mat.columns, rows = mat.rows)

    #mat.displayMatrix(elements = mat.elements)

    return mat

def multMatrix(m1, m2):
    from matrixClass import matrix
    if m1.rows != m2.columns:
        print("Incompatible Matrices!")
        return
    
    rowCounter = 0
    columnCounter = 0
    newMat = matrix(rows=m1.rows,columns=m2.columns, elements= [], entries = "")

    for row in m1.rows:
        for element in row:
            dot = element * m2.elements[columnCounter]
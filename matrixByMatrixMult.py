from dotProd import dotProd
from matrixClass import matrix

def multMatrix(m1, m2): #TODO: implement matrix multiplication
    
    if m1.rows != m2.columns:
        print("Incompatible Matrices!")
        return
    
    rowCounter = 0
    columnCounter = 0
    newMat = matrix(rows=m1.rows,columns=m2.columns, elements= [], 
                    entries = [], columnizedElements= [])
    #newMat.constructMatrix(newMat.elements,newMat.rows,newMat.columns, entries = "")
    

    
    m2.columnizeMatrix(m2.elements, [], m2.columns, m2.rows)

    for index, aRow in enumerate(m1.elements):
        
        for bRow in m2.columnizedElements:  
            prod = dotProd(a = aRow, b = m2.columnizedElements[index])
            print(index, prod)
            
            newMat.entries.append(prod)
    
    newMat.constructMatrix(newMat.elements, newMat.rows, newMat.columns, newMat.entries)
    

    return newMat

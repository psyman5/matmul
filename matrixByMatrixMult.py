from dotProd import dotProd
from matrixClass import matrix

def multMatrix(m1, m2): #TODO: implement matrix multiplication
    
    '''Multiplies two Matrix objects via the naive method. Time complexity: O(n^3).'''

    if m1.rows != m2.columns:
        print("Incompatible Matrices!")
        return
    
    rowCounter = 0
    columnCounter = 0
    newMat = matrix(rows=m1.rows,columns=m2.columns, elements= [], # create a new matrix,
                    entries = [], columnizedElements= [], constructFlag= False)
    

    
    m2.columnizeMatrix(m2.elements, [], m2.columns, m2.rows)

    for indexA, aRow in enumerate(m1.elements): #for every row in matrix 1, 
        
        for indexB, bRow in enumerate(m2.columnizedElements): #for every column in matrix 2, 
            prod = dotProd(a = aRow, b = m2.columnizedElements[indexB]) #get the dot product of the two,
            #print(index, prod)
            
            newMat.entries.append(prod) #add it to a new list containing the entries of the new matrix
            #print(indexA,indexB, newMat.entries)
    
    newMat.constructMatrix() #construct the matrix
    

    return newMat #return the matrix

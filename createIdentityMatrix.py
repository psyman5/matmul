from matrixClass import matrix

def CreateIdentityMatrix(size):

    '''Creates a square identity matrix of given size (size*size). Returns a matrix object.'''

    identityMatrix = matrix(size, size, [], [], [] , False)
    oneCounter = 0

    for x in range(size**2):
        if x == 0:
            identityMatrix.entries.append(1)
        else:
            if oneCounter != size:
                oneCounter += 1
                identityMatrix.entries.append(0)
            else:
                oneCounter = 0
                identityMatrix.entries.append(1)

    identityMatrix.constructMatrix()

    return identityMatrix 

    
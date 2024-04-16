def dotAdd(a, b):

    '''Dot addition of two matrices a and b.'''

    addedNums = [element + b[index] for index, element in enumerate(a)]

    return addedNums

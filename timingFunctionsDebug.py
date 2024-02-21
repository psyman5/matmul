

def timingScalar():
    import timeit
    from matrixClass import matrix
    from matrixByMatrixMult import multMatrix

    matrixOne = matrix(1000,1000,[],[x for x in range(1000000)], [], False)
    matrixTwo = matrix(1000,1000,[],[x for x in range(1000000)], [], False)

    args = (1,  2)
    rep = 1000

    # Time the function with the given arguments
    elapsed_time = timeit.timeit('multMatrix(matrixOne,matrixTwo)', number=rep)
    average_time = elapsed_time /  100

    print(f"The function took on average {average_time} seconds to execute.")
    print(f"Execution time of multMatrix: {elapsed_time} seconds")

timingScalar()
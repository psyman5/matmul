

def timingScalar():
    import timeit
    from matrixClass import matrix
    from scalarMult1 import scalarMult1
    from scalarMult2 import scalarMult2

    args = (1,  2)
    rep = 1000000
    n=100
    execTimeList1 = [] 
    execTimeList2 = []

    for x in range(0,n):
        numList = [x for x in range(5,n^2+1)]
        matrixOne = matrix(len(numList)-1,len(numList)-1,[],numList)


        # Time the function with the given arguments
        timeTaken1 = timeit.timeit('scalarMult1(2, matrixOne)', globals=globals(), number = rep)
        averageTime1 = timeTaken1 / rep

        timeTaken2 = timeit.timeit('scalarMult2(2, matrixOne)', globals=globals(), number = rep)
        averageTime2 = timeTaken1 / rep

        execTimeList1.append(timeTaken1)
        execTimeList2.append(timeTaken2)





    '''print(f"Execution time of ScalarMult1: {timeTaken1} seconds")
    print(f"Average time of ScalarMult1: {averageTime1} seconds")
    print('\n')
    print(f"Execution time of ScalarMult2: {timeTaken2} seconds")
    print(f"Average time of ScalarMult2: {averageTime2} seconds")'''

    print(execTimeList1)
    print("\n")
    print(execTimeList2)
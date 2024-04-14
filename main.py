import timeit
from matrixClass import matrix
from matrixByMatrixMult import multMatrix
from exponentiation import takeExponent
from getTrace import getDiagonalAndTrace


#matrixOne = matrix(2,2,[],[x for x in range(2**2)], [], True)
#matrixTwo = matrix(2,2,[],[x for x in range(2**2)], [], True)

matrixOne = matrix(2,2,[],[4,4,2,3], [], False)
matrixTwo = matrix(2,2,[],[3,6,4,8], [], True)

matrixOne.constructMatrix(elements=matrixOne.elements,rows=matrixOne.rows, 
                          columns=matrixOne.columns, entries= matrixOne.entries, constructFlag= matrixOne.constructFlag)

#matrixTwo.constructMatrix(elements=matrixTwo.elements,rows=matrixTwo.rows, 
                          #columns=matrixTwo.columns, entries= matrixTwo.entries,  constructFlag= matrixTwo.constructFlag)


matrixOne.addRow([3,2])
matrixOne.addColumn([4,4,4])
matrixOne.setNumber(2,1,3)

matrixOne.displayMatrix()

print(getDiagonalAndTrace(matrixOne)[0])

#takeExponent(matrixOne, 10)
'''timeList = []


for exponent in range(2, 31):
    number = 10000
    # Define the setup code
    setup_code = """from __main__ import matrixOne, takeExponent"""
    # Define the code to be timed
    stmt = f"""takeExponent(matrixOne, {exponent})"""
    # Time the execution of the code
    execution_time = timeit.timeit(stmt, setup=setup_code, number = number)

    timeList.append([exponent, execution_time/number])
    
    print(f"Time taken to calculate {matrixOne} raised to the power of {exponent} 10000 times: {execution_time} seconds")

print(timeList)

#matrixOne.displayMatrix()'''







class matrix():
    def __init__(self, rows, columns, elements, entries, columnizedElements, constructFlag):
        self.rows = rows 
        self.columns = columns
        self.elements = elements
        self.entries = entries
        self.columnizedElements = columnizedElements
        self.constructFlag = constructFlag

    def encodeElements(self, entries, columns, rows):

        '''Separates the entry array/string into an array containing arrays containing column values.'''

        elements = [[] for _ in range(rows)]
        rowCounter = 0
        columnCounter = 0

        for entry in entries:
            entry = int(entry)
            if columnCounter < columns -1:
                elements[rowCounter].append(entry)
                columnCounter += 1
            elif columnCounter == columns -1:
                elements[rowCounter].append(entry)
                columnCounter = 0
                rowCounter += 1
            else:
                raise ValueError("Incorrect Matrix Dimensions")
        self.elements = elements

        return elements
    
    def decodeElements(self, elements, rows, columns):

        '''Transforms a Matrix into a list of its elements. Returns a list of strings.'''

        rowCounter = 0
        columnCounter = 0


        rawEntries = []

        for row in elements:
            if columnCounter < columns:
                print(columnCounter)
                rawEntries.append(str(row[columnCounter]))
                columnCounter += 1

            elif columnCounter == columns:
                rawEntries.append(str(row[columnCounter]))
                columnCounter = 0
        
        return rawEntries

    def displayMatrix(self):
        
        '''Prints the matrix via the terminal.'''

        for x in self.elements:
            print(x)

    def constructMatrix(self, elements, rows, columns, entries, constructFlag): #assembles matrix from pieces.
        
        '''Officially creates the matrix using previous functions.'''


        def encodeElements(self, entries, columns, rows):
            elements = [[] for _ in range(rows)]
            rowCounter = 0
            columnCounter = 0

            for entry in entries:
                entry = int(entry)
                if columnCounter < columns - 1 :
                    elements[rowCounter].append(entry)
                    
                    columnCounter += 1
                elif columnCounter == columns - 1:
                    elements[rowCounter].append(entry)
                    #print("Row Done:: " + str(entry),str(rowCounter),str(columnCounter))
                    columnCounter = 0
                    if rows > 1:
                        rowCounter += 1
                else:
                    raise ValueError("Incorrect Matrix Dimensions")
            self.elements = elements

            return elements
    
        def displayMatrix(self):

            for x in self.elements:
                print(x)

        elements = encodeElements(self, entries, columns, rows) #this isn't used but it is not working without it so i will keep it in here

        if constructFlag is True: 
            displayMatrix(self)
            print("\n")


    def columnizeMatrix(self, elements, columnizedElements, columns, rows):
        
        '''Takes the transpose of the matrix. Specifically limited to row > columns matrices.'''

        columnCounter = 0
        rowCounter = 0 
        columnizedElements = [[] for _ in elements]
        
        #print(rows,columns)

        if rows >= columns:
            for c in range(columns):
                for index, row in enumerate(elements):
                    columnizedElements[c].append(row[columnCounter])
                    #print(row, columnCounter,columnizedElements[index])
                columnCounter += 1
            
        else:
            self.columnizedElements = elements
            return columnizedElements

        self.columnizedElements = columnizedElements

        return columnizedElements
    
    def addRow(self, rowEntries):
        
        '''Adds a row to the vertical end of the matrix. rowEntries must be an iterable.'''

        if len(rowEntries) != self.columns:
            print("Incorrect number of row values!")
            raise ValueError
        
        else:
            self.rows += 1
            self.elements.append([])

            for entry in rowEntries:
                self.elements[-1].append(entry)

            return self.elements
        
    def addColumn(self, colEntries):
        
        '''Adds a column to the horizontal end of the matrix. colEntries must be an iterable.'''

        if len(colEntries) != self.rows:
            print("Incorrect number of column values!")
            raise ValueError
        else:
            self.columns += 1
            entryIndex = 0
            for index, row in enumerate(self.elements):
                row.append(colEntries[index])
            return self.elements

        

    def removeRow(self, rowNum):
        
        '''Removes a given row. ARGUMENT USES NORMAL MATRIX I,J NOTATION. DOES NOT USE ZERO BASED INDEXING.'''

        if (rowNum > self.rows) or ( rowNum < 1):
            print("Row number accessed does not exist.")
            raise ValueError
        else:
            self.rows -= 1
            del self.elements[rowNum - 1]

            return self.elements

    def removeColumn(self, colNum):
        
        '''Removes a given column. ARGUMENT USES NORMAL MATRIX I,J NOTATION. DOES NOT USE ZERO BASED INDEXING.'''

        if (colNum > self.columns) or ( colNum < 1):
            print("Column number accessed does not exist.")
            raise ValueError
        
        else:
            self.columns -= 1
            for element in self.elements:
                del element[colNum - 1]
            
            return self.elements

    def setNumber(self, row, col, val):
        
        '''Changes a given element's value. ARGUMENT USES NORMAL MATRIX I,J NOTATION. DOES NOT USE ZERO BASED INDEXING.'''

        if (row > self.rows) or (row < 1):
            print("Row number accessed does not exist.")
            raise ValueError
        
        elif (col > self.columns) or (col < 1):
            print("Column number accessed does not exist.")
            raise ValueError

        else:
            self.elements[row-1][col-1] = val

        return self.elements
    
    def searchForOccurences(self, desired):
        
        '''Searches for all occurences of a certain value. '''

        occurences = []
        for row in self.elements:
            for element in row:
                if element == desired:
                    occurences.append([self.elements.index(row)+1, row.index(desired)+1])

        return occurences
    
    def getSparsity(self):

        '''Finds the sparsity of the matrix. Returns a float fractional representation.'''

        numZeroes = len(self.searchForOccurences(0))

        sparsity = (1 - numZeroes/(self.rows*self.columns))

        return sparsity


                    
        

            

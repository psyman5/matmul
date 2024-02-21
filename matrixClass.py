class matrix():
    def __init__(self, rows, columns, elements, entries):
        self.rows = rows 
        self.columns = columns
        self.elements = elements
        self.entries = entries

    def encodeElements(self, entries, columns, rows):
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
        
        '''for row in elements:
            for element in row:
                rawEntries.append(str(element))'''
        
        return rawEntries

    def displayMatrix(self, elements):

        for x in elements:
            print(x)

    def constructMatrix(self, elements, rows, columns, entries): #assembles matrix from pieces.

        def encodeElements(self, entries, columns, rows):
            elements = [[] for _ in range(rows)]
            rowCounter = 0
            columnCounter = 0

            for entry in entries: #TODO fix this, zero-based indexing issue
                entry = int(entry)
                if columnCounter < columns - 1 :
                    elements[rowCounter].append(entry)
                    #print("Col Done: " + str(entry),str(rowCounter),str(columnCounter))
                    columnCounter += 1
                elif columnCounter == columns - 1:
                    elements[rowCounter].append(entry)
                    #print("Row Done:: " + str(entry),str(rowCounter),str(columnCounter))
                    columnCounter = 0
                    rowCounter += 1
                else:
                    raise ValueError("Incorrect Matrix Dimensions")
            self.elements = elements

            return elements
    
        def displayMatrix(self, elements):

            for x in elements:
                print(x)

        def check():
            for element in elements:
                if len(element) < columns:
                    print("Dimension Error!")

        elements = encodeElements(self, entries, columns, rows)
        displayMatrix(self, encodeElements(self, entries, columns, rows))
        check()


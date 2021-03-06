import csv
import os

directory1 = "sudokulist.csv"

# check if exist csv file
def checkcsvfile():
    if not os.path.isfile(directory1):
        print("Creating new csv file" + directory1)
        with open('sudokulist.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['ID', 'R0C0', 'R0C1', 'R0C2', 'R0C3', 'R0C4', 'R0C5', 'R0C6', 'R0C7', 'R0C8',
                                 'R1C0', 'R1C1', 'R1C2', 'R1C3', 'R1C4', 'R1C5', 'R1C6', 'R1C7', 'R1C8',
                                 'R2C0', 'R2C1', 'R2C2', 'R2C3', 'R2C4', 'R2C5', 'R2C6', 'R2C7', 'R2C8',
                                 'R3C0', 'R3C1', 'R3C2', 'R3C3', 'R3C4', 'R3C5', 'R3C6', 'R3C7', 'R3C8',
                                 'R4C0', 'R4C1', 'R4C2', 'R4C3', 'R4C4', 'R4C5', 'R4C6', 'R4C7', 'R4C8',
                                 'R5C0', 'R5C1', 'R5C2', 'R5C3', 'R5C4', 'R5C5', 'R5C6', 'R5C7', 'R5C8',
                                 'R6C0', 'R6C1', 'R6C2', 'R6C3', 'R6C4', 'R6C5', 'R6C6', 'R6C7', 'R6C8',
                                 'R7C0', 'R7C1', 'R7C2', 'R7C3', 'R7C4', 'R7C5', 'R7C6', 'R7C7', 'R7C8',
                                 'R8C0', 'R8C1', 'R8C2', 'R8C3', 'R8C4', 'R8C5', 'R8C6', 'R8C7', 'R8C8',
                                 ])
            csvfile.close()


# insert sudoku to csv file
def insersudoku(arraynumber):
    row = []
    with open(directory1, 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        lastid = getlastid() + 1
        row.append(lastid)
        for i in range(0, 9):
            for j in range(0, 9):
                row.append(arraynumber[i][j])
        filewriter.writerow(row)
        csvfile.close()


def getlastid():
    id = -1
    number = 0
    # open file
    with open(directory1, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if number > 0 and int(row[0]) > id:
                id = int(row[0])
            number += 1
    return id


def getsudokubyid(id):
    sudokurow = None
    with open(directory1, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                if int(row[0]) == id:
                    sudokurow = row
                    break
            except:
                pass
    f.close()

    if sudokurow is not None:
        sudoku = [[]]
        j, l = 0, 0
        for i in sudokurow[1:]:
            sudoku[j].append(int(i))
            l += 1
            if l == 9:
                j += 1
                l = 0
                sudoku.append([])
    else:
        sudoku = False
    return sudoku


checkcsvfile()

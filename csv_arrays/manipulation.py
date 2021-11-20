import csv



def write_CSV(filename: str, array):
    with open(filename, 'w', newline='') as file:
        csv.writer(file, delimiter=',').writerows(array)

def read_CSV(filename: str):
    file = open(filename, 'rt')
    lines = file.read().splitlines()
    array = []
    numberOfLines = len(lines)
    for i in range(numberOfLines):
        line = lines[i]
        values = line.split(',')
        array.append(values)
    return array

def search_2D_array(array: list, value: str, column: int = 0) -> int:
    for index in range(len(array)):
        if value == array[index][column]:
            return index

def search_1D_array(array: list, value: str) -> int:
    for index in range(len(array)):
        if value == array[index]:
            return index

def columnate(board, column_index = 0, top: int = None, bottom: int = None):
    column = []
    board = board[top:bottom]
    for i in range(len(board)):
        column.append(board[i][column_index])
    return column

def append_CSV(filename: str, appendage):
    array = read_CSV(filename)
    array.append(appendage)
    write_CSV(filename, array)

def append_CSV_line(filename: str, value: int, column: int, *appendage):
    array = read_CSV(filename)
    for i in array:
        if i[column] == value:
            for j in appendage:
                i.append(j)
    write_CSV(filename, array)

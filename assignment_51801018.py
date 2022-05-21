import sys
import random

'''
Apply random seed with student ID: 51801018
'''
m = 51801018
random.seed(m)

def checkInputArgument(inputAgr):
    '''
    function objective
    input: inputAgr dtype: int
    output: if the input agrument is false, this function forces the program stop immediately
    '''
    if inputAgr <= 0 or inputAgr > 81:
        print("The input argument is wrong.")
        exit(0)
    elif(inputAgr % 9 != 0):
        print("The input argument is not divisible by 9.")
        exit(0)
        
def checkAndCreate(booleanMatrix, element, prevElement, latinSquarePermutations, i):
    '''
    fucntion objective
    input: booleanMatrix, element is current 1 square, prevElement is the list of previous elements
    , latinSquarePermutation to store all latin squares, i counter
    output: append new element to latinSquarePermutaion
    '''
    if i == len(booleanMatrix):
        return element;
    else:
        prevElement = set();
        for j in range(0, i+1):
            if booleanMatrix[i][j] != 0:
                prevElement.add(element[j])
        for k in range(1, 4):
            if k not in prevElement:
                element[i]=k
                checkAndCreate(booleanMatrix, element, prevElement, latinSquarePermutations, i+1);
        if i==len(booleanMatrix)-1:
            return latinSquarePermutations.append(element.copy());

def latinSquaresGenerate(booleanMatrix):
    '''
    function objective
    input: booleanMatrix is the matrix that all of whose columns and rows each have exactly one nonzero element
    output: all permutation of latin squares
    '''
    latinSquarePermutations = [];
    for k in range(1, 4):
        element = [0] * len(booleanMatrix)
        element[0] = k
        prevElement = set()
        checkAndCreate(booleanMatrix, element, prevElement, latinSquarePermutations, 1)
    for i in range(len(latinSquarePermutations)):
        for j in range(len(latinSquarePermutations[i])):
            latinSquarePermutations[i][j]-=1;
    return latinSquarePermutations
        
def scaleToBase10(sudokuBase3, scalerMatrix):
    '''
    function objective
    input: sudokuBase3 which stored 9 latin squares, scalerMatrix is 1 latin square
    output: sudokuBase10 is the 9 latin squares after scaling sudokuBase3 to base 10 with scalerMatrix
    '''
    for i in range(len(sudokuBase3)):
        B3 = sudokuBase3[i].copy()
        S = scalerMatrix[i]
        for j in range(len(sudokuBase3[i])):
            B3[j] = B3[j] + 1 + 3 * S
        sudokuBase3[i] = B3.copy()
    return sudokuBase3
    
def getRow(sudokuBase10, i):
    '''
    function objective
    input: sudokuBase10, i is row number
    output: row
    '''
    S = []
    if(i<=3):
        if(i==1 or i==4 or i==7):
            r=0
        if(i==2 or i==5 or i==8):
            r=3
        if(i==3 or i==6 or i==9):
            r=6
        for j in range(3):
            S.append(sudokuBase10[j][r:r+3])
    elif(i<=6):
        if(i==1 or i==4 or i==7):
            r=0
        if(i==2 or i==5 or i==8):
            r=3
        if(i==3 or i==6 or i==9):
            r=6
        for j in range(3,6):
            S.append(sudokuBase10[j][r:r+3])
    elif(i<=9):
        if(i==1 or i==4 or i==7):
            r=0
        if(i==2 or i==5 or i==8):
            r=3
        if(i==3 or i==6 or i==9):
            r=6
        for j in range(6,9):
            S.append(sudokuBase10[j][r:r+3])
    return S

def rowSwapping(latinSquareBase10, firstRow, secondRow):
    '''
    function objective
    input: latinSquareBase10, firstRow, secondRow
    output: swapping them, return new latinSquareBase10
    '''
    A = getRow(latinSquareBase10, firstRow)
    B = getRow(latinSquareBase10, secondRow)
    temp = [firstRow, secondRow]
    arr = [B, A]
    for i in temp:
        if(i<=3):
            if(i==1 or i==4 or i==7):
                r=0
            if(i==2 or i==5 or i==8):
                r=3
            if(i==3 or i==6 or i==9):
                r=6
            for s in range(3):
                latinSquareBase10[s][r:r+3]=arr[temp.index(i)][s]
        elif(i<=6 and i>3):
            if(i==1 or i==4 or i==7):
                r=0
            if(i==2 or i==5 or i==8):
                r=3
            if(i==3 or i==6 or i==9):
                r=6
            for s in range(3,6):
                latinSquareBase10[s][r:r+3]=arr[temp.index(i)][s-3]
        elif(i<=9 and i>6):
            if(i==1 or i==4 or i==7):
                r=0
            if(i==2 or i==5 or i==8):
                r=3
            if(i==3 or i==6 or i==9):
                r=6
            for s in range(6,9):
                latinSquareBase10[s][r:r+3]=arr[temp.index(i)][s-6]
    return latinSquareBase10
    
def diggingHoles(latinSquareBase10, numberOfHoles):
    '''
    function objective
    input: latinSquareBase10, numberOfHoles
    output: Digging n-holes in latinSquareBase10
    '''
    numberOfHoles = numberOfHoles//9
    for i in range(len(latinSquareBase10)):
        A = list(range(len(latinSquareBase10[0])))
        for j in range(numberOfHoles):
            k = A.pop(random.randint(0,len(A)-1))
            latinSquareBase10[i][k]=0
    return latinSquareBase10

def outputFile(Sudoku, outputFileName):
    '''
    function objective
    input: Sudoku puzzle, outputFileName
    output: the text file stored sudoku puzzle
    '''
    file = open(outputFileName, "w")
    for i in range(3):
        for j in range(3):
            for k in range(3):
                file.write(str(Sudoku[i*3+k][j*3])+','+str(Sudoku[i*3+k][j*3+1])+','+str(Sudoku[i*3+k][j*3+2]))
                if(k < 2):
                    file.write(',')
            file.write('\n')
    file.close()

def Main(numberOfHoles, outputFileName):
    '''
    Main fuction calls each previous function step by step
    '''
    checkInputArgument(numberOfHoles)

    booleanMatrix =    [[0,1,1, 1,0,0, 1,0,0],
                        [1,0,1, 0,1,0, 0,1,0],
                        [1,1,0, 0,0,1, 0,0,1],

                        [1,0,0, 0,1,1, 1,0,0],
                        [0,1,0, 1,0,1, 0,1,0],
                        [0,0,1, 1,1,0, 0,0,1],

                        [1,0,0, 1,0,0, 0,1,1],
                        [0,1,0, 0,1,0, 1,0,1],
                        [0,0,1, 0,0,1, 1,1,0]]

    sudokuBase3 = []
    allLatinSquare = latinSquaresGenerate(booleanMatrix)
    print(allLatinSquare)

    '''
    Step 1: Latin squares generate
    sudokuBase3 takes 9 latin squares from allLatinSquare
    scalerMatrix takes 1 latin square from allLatinSquare
    '''
    for i in range(9):
        i = random.randint(0,11)
        sudokuBase3.append(allLatinSquare[i])
    print("sudokuBase3", sudokuBase3)

    scalerMatrix = allLatinSquare[random.randint(0,11)]
    print("scalerMatrix", scalerMatrix)

    '''
    Step 2: Scaling base3-matrix to base10-matrix
    '''
    sudokuBase10 = scaleToBase10(sudokuBase3, scalerMatrix)
    print("sudokuBase10", sudokuBase10)

    '''
    Step 3: Row swapping
    2nd & 4th
    3rd & 7th
    6th & 8th
    '''
    sudokuBase10 = rowSwapping(sudokuBase10,2,4)
    sudokuBase10 = rowSwapping(sudokuBase10,3,7)
    sudokuBase10 = rowSwapping(sudokuBase10,6,8)

    '''
    Step 4: Digging holes. The number of holes is the 1st agrument from user and it is multiple of 9
    '''
    Sudoku = diggingHoles(sudokuBase10, numberOfHoles)

    '''
    Step 5: Write to file
    '''
    outputFile(Sudoku, outputFileName)

# 2 commandline agrument get from user
numberOfHoles = int(sys.argv[1])
outputFileName = sys.argv[2]

Main(numberOfHoles, outputFileName)
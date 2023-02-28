import time

########################################################
#################### Insertion Sort ####################
########################################################

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


####################################################
#################### Merge Sort ####################
####################################################

#   Merge(array, left, middle, right)
def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #Left and Right Sides
    Left = [0] * (n1)
    Right = [0] * (n2)

    #Split main array into two subarrays
    for i in range(0, n1):
        Left[i] = array[l + i]

    for j in range(0, n2):
        Right[j] = array[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            array[k] = Left[i]
            i += 1
        else:
            array[k] = Right[j]
            j += 1
        k += 1

    #Left Side
    while i < n1:
        array[k] = Left[i]
        i += 1
        k += 1
    #Right Side
    while j < n2:
        array[k] = Right[j]
        j += 1
        k += 1

def mergeSort(array, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(array, l, m)
        mergeSort(array, m + 1, r)
        merge(array, l, m, r)

###################################################
#################### Heap Sort ####################
###################################################

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[largest] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]


        heapify(array, n, largest)


def heapSort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(array, i, 0)


######################################################
#################### Main Program ####################
######################################################


exitCount = 0

while exitCount != 1:

# Sorting Method selection
    print("Enter type of sort to execute \n1: Insertion Sort \n2: Merge Sort \n3: Heap Sort \n0: Close and exit")
    sortType = eval(input("Choice: "))
    print(" ")
    if(sortType == 1):
        sortType = "Insertion"
    elif(sortType == 2):
        sortType = "Merge"
    elif(sortType == 3):
        sortType = "Heap"
    elif(sortType == 0):
        exit()
    else:
        print("Sorry invalid input, exiting program, please try again")
        exit()

# File type selection
    print("Enter which type of files to sort \n1: Unsorted Input \n2: Sorted Input \n0: Exit")
    inputType = eval(input("Choice: "))
    print(" ")
    if(inputType == 0):
        exit()
    elif(inputType == 1):
        inputType = "perm"
    elif(inputType == 2):
        inputType = "sorted"
    else:
        print("Sorry invalid input, exiting program, please try again")
        exit()

# File type selection
    print("Enter file to print")
    print("1:  " + inputType + "15K.txt")
    print("2:  " + inputType + "30K.txt")
    print("3:  " + inputType + "45K.txt")
    print("4:  " + inputType + "60K.txt")
    print("5:  " + inputType + "75K.txt")
    print("6:  " + inputType + "90K.txt")
    print("7:  " + inputType + "105K.txt")
    print("8:  " + inputType + "120K.txt")
    print("9:  " + inputType + "135K.txt")
    print("10: " + inputType + "150K.txt")
    fileName = eval(input("Choice: "))
    print(" ")


    match fileName:
        case 1:
            fileSuffix = "15K.txt"
            fileName = inputType + fileSuffix
        case 2:
            fileSuffix = "30K.txt"
            fileName = inputType + fileSuffix
        case 3:
            fileSuffix = "45K.txt"
            fileName = inputType + fileSuffix
        case 4:
            fileSuffix = "60K.txt"
            fileName = inputType + fileSuffix
        case 5:
            fileSuffix = "75K.txt"
            fileName = inputType + fileSuffix
        case 6:
            fileSuffix = "90K.txt"
            fileName = inputType + fileSuffix
        case 7:
            fileSuffix = "105K.txt"
            fileName = inputType + fileSuffix
        case 8:
            fileSuffix = "120K.txt"
            fileName = inputType + fileSuffix
        case 9:
            fileSuffix = "135K.txt"
            fileName = inputType + fileSuffix
        case 10:
            fileSuffix = "150K.txt"
            fileName = inputType + fileSuffix
        case _:
            print("Sorry incorrect input, exiting program, please try again")
            exit()

#Load File
    file = open(fileName, 'r')
    lines = file.read().split('\n')
    lines.remove("")
    n = len(lines)

    if(sortType == "Insertion"):
        startTime = time.time()
        insertionSort(lines)
        endTime = time.time()
    elif(sortType == "Merge"):
        startTime = time.time()
        mergeSort(lines, 0, n-1)
        endTime = time.time()
    elif(sortType == "Heap"):
        startTime = time.time()
        heapSort(lines)
        endTime = time.time()
    else:
        print("Error Try again")
        exit()

    totalTime = endTime - startTime
    print(" \nTime: " + str(totalTime) + " seconds \n")

    if(sortType == "Insertion"):
        writeFile = open("IS" + fileSuffix, "w")
    elif(sortType == "Merge"):
        writeFile = open("MS" + fileSuffix, "w")
    elif(sortType == "Heap"):
        writeFile = open("HS" + fileSuffix, "w")

    for i in range(n):
        writeFile.write(lines[i] + "\n"),

    file.close()
    writeFile.close()


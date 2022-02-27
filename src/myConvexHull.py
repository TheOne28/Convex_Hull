from cmath import sqrt
from copy import deepcopy
from numpy import arange, arccos


def determinant(p1, p2, p3):
    #Pengecekan posisi p3 dibanding dengan p1 p2
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]

    return (x1*y2) + (x3 * y1) + (x2 * y3) - (x3 * y2) - (x2 * y1) - (x1 * y3)

def findLength(p1, p2):
    difx = p1[0] - p2[0]
    dify = p1[1] - p2[1]

    return ((difx ** 2) + (dify ** 2)) ** 0.5

def findCosine(find, param1, param2):
    denom = (param1 ** 2) + (param2 ** 2) - (find ** 2)
    return denom / (2 * param2 * param1)

def findDistance(cosine, param1):
    param2 = cosine * param1
    return ((param1 ** 2) - (param2 ** 2)) ** 0.5

def checkexist(array, toCheck):
    for each in array:
        if(each[0] == toCheck[0] and each[1] == toCheck[1]):
            return True
        elif(each[0] == toCheck[1] and each[1] == toCheck[0]):
            return True
    return False

def creteDict(data):
    dataInDict = {}
    for i in range(len(data)):
        dataInDict[tuple(data[i])] = i 
    return dataInDict


def convexhull(data):
    copy_data = deepcopy(data)
    dataInDict = creteDict(copy_data)
    length = len(data)

    sorted_data = sorted(copy_data, key = lambda x: (x[0], x[1]))

    p1 = sorted_data[0]
    p2 = sorted_data[length - 1]

    left_part = []
    right_part = []

    for i in range(1, length - 1):
        if(determinant(p1, p2, sorted_data[i]) > 0):
            left_part.append(sorted_data[i])
        elif(determinant(p1, p2, sorted_data[i]) < 0):
            right_part.append(sorted_data[i])
    
    final = []

    DCStep(left_part, p1, p2, final, dataInDict)
    DCStep(right_part, p1, p2, final, dataInDict)

    # finalClean = []
    # [finalClean.append(element) for element in final if element not in finalClean] 
    return final

def DCStep(array, p1, p2, final, dataInDict):
    if(len(array) == 0):
        newPair = []
        newPair.append(dataInDict[tuple(p1)])
        newPair.append(dataInDict[tuple(p2)])

        if(not checkexist(final, newPair)):
            final.append(newPair)
    else:
        length = findLength(p1, p2)
        maxLength = 0
        maxAngle = 0.0
        p3 = []
        # print(final)
        # print(array)

        for i in range(len(array)):
            length2 = findLength(p1, array[i])
            length3 = findLength(p2, array[i])

            cosine = findCosine(length3, length2, length)
            distance = findDistance(cosine, length2)
            if(distance > maxLength):
                maxLength = distance
                p3 = array[i]
                maxAngle = arccos(cosine)
            elif(distance == maxLength):
                angle = arccos(cosine)
                if(angle > maxAngle):
                    maxLength = distance
                    p3 = array[i]
                    maxAngle = angle

        first_part = []
        second_part = []

        if(len(p3) != 0):
            for i in range(0, len(array)):
                if(array[i][0] != p3[0] and array[i][1] != p3[1]):
                    #Sebelah kiri garis p1pmax
                    if(determinant(p1, p3, array[i]) > 0):
                        first_part.append(array[i])    
                    #Sebelah kanan garis p2pmax
                    elif(determinant(p2, p3, array[i]) < 0):
                        second_part.append(array[i])

            # print(p3)
            # print("\n")
            DCStep(first_part, p1, p3, final, dataInDict)
            DCStep(second_part, p2, p3, final, dataInDict)

from copy import deepcopy
from math import isclose, acos

def determinant(p1, p2, p3):
    #menghitung determinan dari p1, p2, p3 -> p1 dan p2 membentuk garis dan 
    #p1, p2, dan p3 adalah pasangan titik
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]

    return (x1*y2) + (x3 * y1) + (x2 * y3) - (x3 * y2) - (x2 * y1) - (x1 * y3)

def findLength(p1, p2):
    #Menghitung panjang garis yang dibentuk oleh titik p1 dan p2 
    difx = p1[0] - p2[0]
    dify = p1[1] - p2[1]

    return ((difx ** 2) + (dify ** 2)) ** 0.5

def findCosine(find, param1, param2):
    #Menghitung cosine yang dibentuk oleh garis find param1, dan param2
    #Sudut yang dibentuk adalah sudut antara param1 dan param2, dengan find adalah sisi di depan sudut
    #Masing-masing find, param1, dan param2 berisi panjang dari masing" garis

    denom = (param1 ** 2) + (param2 ** 2) - (find ** 2)
    denom /= (2 * param2 * param1)
    return denom

def checkexist(array, toCheck):
    #Mengecek kemuncukan titik toCheck di arrays
    for each in array:
        if(each[0] == toCheck[0] and each[1] == toCheck[1]):
            return True
    return False

def createDict(data):
    #Membuat dictionary dengan key berupa pasangan point dan value adalah indexnya di dataset awal
    dataInDict = {}
    
    for i in range(len(data)):
        dataInDict[tuple(data[i])] = i 

    return dataInDict


def preprocessing(data):
    dataInDict = createDict(data)

    cleanData = []
    [cleanData.append(x) for x in data if not checkexist(cleanData, x)]

    sortedData = sorted(cleanData, key = lambda x: (x[0], x[1]))

    return dataInDict, sortedData


def convexhull(data):
    #Membuat deepcopy dari data awal untuk mengurangi risiko kerusakan data awal
    copyData = deepcopy(data)
    
    dataInDict, sortedData = preprocessing(copyData)
    
    p1 = sortedData[0]
    p2 = sortedData[len(sortedData) - 1]

    left_part = []
    right_part = []

    for i in range(1, len(sortedData) - 1):
        if(determinant(p1, p2, sortedData[i]) > 0):
            left_part.append(sortedData[i])
        elif(determinant(p1, p2, sortedData[i]) < 0):
            right_part.append(sortedData[i])
    
    hullPair = []
    DCStep(left_part, p1, p2, hullPair, dataInDict)
    DCStep(right_part, p2, p1, hullPair, dataInDict)

    return hullPair

def DCStep(array, p1, p2, final, dataInDict):
    if(len(array) == 0):
        newPair = []
        newPair.append(dataInDict[tuple(p1)])
        newPair.append(dataInDict[tuple(p2)])

        if(not checkexist(final, newPair)):
            final.append(newPair)
    else:
        length = findLength(p1, p2)
        #length -> p1 p2

        maxLength = 0
        maxAngle = 0.0
        p3 = []

        for i in range(len(array)):
            length2 = findLength(p1, array[i])
            length3 = findLength(p2, array[i])

            cosine = findCosine(length3, length2, length)
            
            #!Ini kasus cosine > 1, dalam beberapa uji coba terjadi karena ketidakdepatan float, saya belum menemukan solusinya
            if(cosine > 1 or cosine < -1):
                cosine = 1
            area = determinant(p1, p2, array[i])
            distance = abs(area) / length
            
            if(distance > maxLength):
                maxLength = distance
                p3 = array[i]
                maxAngle = acos(cosine)
            elif(isclose(distance, maxLength)):
                angle = acos(cosine)
                if(angle > maxAngle):
                    maxLength = distance
                    p3 = array[i]
                    maxAngle = angle

        first_part = []
        second_part = []

        if(len(p3) != 0):
            for i in range(len(array)):
                if(array[i][0] != p3[0] or array[i][1] != p3[1]):
                    #Sebelah kiri garis p1pmax
                    if(determinant(p1, p3, array[i]) > 0):
                        first_part.append(array[i])    
                    #Sebelah kanan garis p2pmax
                    if(determinant(p2, p3, array[i]) < 0):
                        second_part.append(array[i])
            DCStep(first_part, p1, p3, final, dataInDict)
            DCStep(second_part, p3, p2, final, dataInDict)

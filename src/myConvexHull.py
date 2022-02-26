from cmath import sqrt
from copy import deepcopy
from numpy import arange, arccos

def keysort(data):
    first = data[0]
    second = data[1]
    return (first, second)

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
    return (param1 ** 2) - (param2 ** 2) ** 0.5

def convexhull(data):
    copy_data = deepcopy(data)
    length = len(data)

    sorted_data = sorted(copy_data, key=keysort)
    
    p1 = sorted_data[0]
    p2 = sorted_data[length - 1]

    left_part = []
    right_part = []

    for i in range(1, length - 1):
        if(determinant(p1, p2, sorted_data[i]) > 0):
            left_part.append(sorted_data[i])
        else:
            right_part.append(sorted_data[i])
    
    final = DCStep(left_part, p1, p2 )
    final[0].append(DCStep(right_part, p1, p2))

    return final

def DCStep(array, p1, p2):
    if(len(array) == 0):
        return p2
    else:
        final = []

        length = findLength(p1, p2)
        maxLength = 0
        maxAngle = 0.0
        p3 = []
        print(len(array))
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
                angle = arccos(findCosine(length, length2, length3))
                if(angle > maxAngle):
                    maxLength = distance
                    p3 = array[i]
                    maxAngle = angle

        first_part = []
        second_part = []

        if(len(p3) != 0):
            for i in range(0, len(array)):
                if(array[i][0] != p3[0] and array[i][1] != p3[1]):
                    if(determinant(p1, p3, array[i]) > 0):
                        first_part.append(array[i])
                    
                    if(determinant(p2, p3, array[i]) > 0):
                        second_part.append(array[i])
                
        final.append(DCStep(first_part, p1, p3))
        final[0].append(DCStep(second_part, p2, p3))

        return final
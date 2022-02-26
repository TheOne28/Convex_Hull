from copy import deepcopy

from numpy import sort

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

def convexhull(data):
    copy_data = deepcopy(data)
    length = len(data)

    sorted_data = sorted(copy_data, key=keysort)
    
    p1 = sorted_data[0]
    p2 = sorted_data[length - 1]

    left_part = []
    right_part = []

    for i in range(1, length - 1):
        if(determinant(p1, p2, sorted_data[i])):
            left_part.append(sorted_data[i])
        else:
            right_part.append(sorted_data[i])
    return 


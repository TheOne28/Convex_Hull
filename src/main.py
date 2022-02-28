from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from myConvexHull import convexhull

color = {
    "blue" : "b",
    "green" : "g",
    "red" : "r",
    "cyan" : "c",
    "magenta" : "m",
    "yellow" : "y",
    "black" : "k",
    "white" : "w"
}

color_list = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"]

def getDatabase():
    print("Welcome to ConvexHull")
    print("Currenlt, we only works for 3 databases: ")
    print("1. Iris")
    print("2. Wine")
    print("3. Breast_Cancer")

    choice = 0
    while(True):
        choice = int(input("Which databases do you want to use (input the number)? "))

        if(choice >= 1 and choice <= 3):
            break
        else:
            print("That number is not available, please input another number")
    
    if(choice == 1):
        return datasets.load_iris()
    elif(choice == 2):
        return datasets.load_wine()
    else:
        return datasets.load_breast_cancer()
    
def getFeatureName(data):
    i = 1
    featureNames = {}

    for each in data.feature_names:
        featureNames[i] = each
        i += 1

    print("Available feature to be plotted: ")
    
    for each in featureNames:
        print("{}.{}".format(each, featureNames[each]))
    
    id1 = 0
    id2 = 0

    while(True):
        id1 = int(input("Which features do you want to use for x axis (input the number)? "))
        
        if(id1 >= 1 and id1 <= len(featureNames)):
            break
        else:
            print("That number is not available, please input another number")

    while(True):
        id2 = int(input("Which features do you want to use for y axis (input the number)? "))
        
        if(id2 >= 1 and id2 <= len(featureNames) and id2 != id1 ):
            break
        elif(id1 == id2):
            print("That number is already selected for feature in x axis, please input another number")
        else:
            print("That number is not available, please input another number")
    
    return featureNames, id1 - 1, id2 - 1

def getColor(count):
    selectedColor = []
    print("Now choose, {} colors for your line".format(count))
    print("Available color: ")

    for each in color_list:
        print("  {}".format(each))
    
    while(count > 0):
        select = ""
        while(True):
            select = input("Which color do you want to use? ")

            if(select.lower() in color_list):
                selectedColor.append(color[select])
                break
            else:
                print("Those color is not available, please input another color")

        
        count -= 1
        
        if(count != 0):
            print("Next Color !")

    return selectedColor

def main():
    data = getDatabase()
    df = pd.DataFrame(data.data, columns=data.feature_names)

    feature_names, id1, id2 = getFeatureName(data)
    df['Target'] = pd.DataFrame(data.target)

    plt.figure(figsize = (10, 6)) 
    plt.title('{} vs {}'.format(feature_names[id1 + 1], feature_names[id2 + 1]))
    plt.xlabel(data.feature_names[id1]) 
    plt.ylabel(data.feature_names[id2]) 

    selected_color = getColor(len(data.target_names))

    for i in range(len(data.target_names)): 
        bucket = df[df['Target'] == i] 
        bucket = bucket.iloc[:,[id1, id2]].values

        hull = convexhull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color=selected_color[i]) 
        for simplex in hull: 
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], selected_color[i])

    plt.legend()

    output = input("Please choose name for your output file: ")
    plt.savefig("../test/output/{}.jpg".format(output), bbox_inches="tight")

if (__name__ == "__main__"):
    main()
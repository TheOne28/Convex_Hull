import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import myConvexHull

from sklearn import datasets
data = datasets.load_iris()

#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
print(data.feature_names)

df['Target'] = pd.DataFrame(data.target)  
plt.figure(figsize = (10, 6)) 
colors = ['b','r','g'] 
plt.title('Sepal Width vs Sepal Length') 
plt.xlabel(data.feature_names[0]) 
plt.ylabel(data.feature_names[1]) 
for i in range(len(data.target_names)): 
    bucket = df[df['Target'] == i] 
    bucket = bucket.iloc[:,[0,1]].values

    hull = myConvexHull.convexhull(bucket)
    # hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer 
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i]) 
    for simplex in hull: 
        # print(simplex, bucket[simplex[0]], bucket[simplex[1]])
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
    # print("\n") 

plt.legend()

plt.savefig("../test/output/sepalv3.jpg", bbox_inches='tight')
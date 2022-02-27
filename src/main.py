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
plt.title('Petal Width vs Petal Length') 
plt.xlabel(data.feature_names[2]) 
plt.ylabel(data.feature_names[3]) 
for i in range(len(data.target_names)): 
    bucket = df[df['Target'] == i] 
    bucket = bucket.iloc[:,[2,3]].values

    hull = myConvexHull.convexhull(bucket)
    # hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer 
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i]) 
    for simplex in hull: 
        # print(simplex, bucket[simplex[0]], bucket[simplex[1]])
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i]) 

plt.legend()

# plt.savefig("../test/output/petalv2.jpg", bbox_inches='tight')
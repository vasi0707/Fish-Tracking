
path = r"C:\Users\Vasanth\OneDrive\Desktop\6_0.csv"

import pandas as pd
import math
import matplotlib.pyplot as plt

df = pd.read_csv(path)

a=list(df.x)
b=list(df.y)
c=list(df.velo)

v=[]

for i in range(len(a)-1):
    x_d = abs(a[i+1]-a[i])
    y_d = abs(b[i+1]-b[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    v.append(dist)

p = list(range(0,len(v)))
plt.plot(p,v)
plt.xlabel('Frames')
plt.ylabel('Velocity')
plt.title('TRIAL12-Fish_0')
plt.show()

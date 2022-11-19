import csv
with open('tt.txt','r') as f:
    x = [column[6] for column in csv.reader(f,delimiter='\t')]

with open('tt.txt','r') as f:
    y = [column[7] for column in csv.reader(f,delimiter='\t')]

with open('tt.txt','r') as f:
    u = [column[22] for column in csv.reader(f,delimiter='\t')]

import pandas as pd
import math
import matplotlib.pyplot as plt

v=[]
a=[]
b=[]

for j in range(len(u)):
    if(u[j]=='5'):
        a.append((float(x[j])*0.05))
        b.append((float(y[j])*0.05))

for i in range(len(a)-1):
    x_d = abs(a[i+1]-a[i])
    y_d = abs(b[i+1]-b[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    v.append(dist)

p = list(range(0,len(v)))
plt.plot(p,v)
plt.xlabel('Frames')
plt.ylabel('Velocity')
plt.title('TRIAL6-Fish_0')
plt.show()

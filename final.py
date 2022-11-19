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

path = r"C:\Users\Vasanth\OneDrive\Desktop\6_0.csv"

import pandas as pd
import math
import matplotlib.pyplot as plt

df = pd.read_csv(path)

a1=list(df.x)
b1=list(df.y)
e=list(df.velo)
c=[]
for i in range(len(e)):
    c.append((e[i]/25))

v1=[]

for i in range(len(a1)-1):
    x_d = abs(a1[i+1]-a1[i])
    y_d = abs(b1[i+1]-b1[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    v1.append(dist)

def vvv(m,p):
    new = 0
    for i in range(p,p+10):
        new = new + m[i]
    return (new/10)

avg = []
avg1 = []
avg2 = []

for i in range(0,len(v)-10,10):
    avg.append(vvv(v,i))

for i in range(0,len(v1)-10,10):
    avg1.append(vvv(v1,i))

for i in range(0,len(c)-10,10):
    avg2.append(vvv(c,i))


p = list(range(0,len(avg)))
p1 = list(range(0,len(avg1)))
p2 = list(range(0,len(avg2)))
plt.plot(p,avg,label = "FastTrack Velocity")
plt.plot(p1,avg1,label = "Trex(Co-ords Velocity)")
plt.plot(p2,avg2,label = "Trex(Velocity)")
plt.legend()
plt.xlabel('Frames')
plt.ylabel('Velocity')
plt.title('TRIAL6-Fish_0')
plt.show()
    

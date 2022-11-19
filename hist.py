import pandas as pd
import math
import matplotlib.pyplot as plt
import csv
import numpy as np

path1 = r"C:\Users\Vasanth\OneDrive\Desktop\6_0.csv"

df1 = pd.read_csv(path1)

a1=list(df1.x)
b1=list(df1.y)
trex_6=list(df1.velo)

trex_cal_6=[]

for i in range(len(a1)-1):
    x_d = abs(a1[i+1]-a1[i])
    y_d = abs(b1[i+1]-b1[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    trex_cal_6.append(dist)


with open('tracking_vasanth.txt','r') as f:
    x1 = [column[6] for column in csv.reader(f,delimiter='\t')]

with open('tracking_vasanth.txt','r') as f:
    y1 = [column[7] for column in csv.reader(f,delimiter='\t')]

with open('tracking_vasanth.txt','r') as f:
    u1 = [column[22] for column in csv.reader(f,delimiter='\t')]

fas_6=[]
a2=[]
b2=[]

for j in range(len(u1)):
    if(u1[j]=='5'):
        a2.append((float(x1[j])*0.05))
        b2.append((float(y1[j])*0.05))

for i in range(len(a2)-1):
    x_d = abs(a2[i+1]-a2[i])
    y_d = abs(b2[i+1]-b2[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    fas_6.append(dist)

path2 = r"C:\Users\Vasanth\OneDrive\Desktop\7_0.csv"

df2 = pd.read_csv(path2)

a3=list(df2.x)
b3=list(df2.y)
trex_7=list(df2.velo)

trex_cal_7=[]

for i in range(len(a3)-1):
    x_d = abs(a3[i+1]-a3[i])
    y_d = abs(b3[i+1]-b3[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    trex_cal_7.append(dist)


with open('tracking_7.txt','r') as f:
    x2 = [column[6] for column in csv.reader(f,delimiter='\t')]

with open('tracking_7.txt','r') as f:
    y2 = [column[7] for column in csv.reader(f,delimiter='\t')]

with open('tracking_7.txt','r') as f:
    u2 = [column[22] for column in csv.reader(f,delimiter='\t')]

fas_7=[]
a4=[]
b4=[]

for j in range(len(u2)):
    if(u2[j]=='5'):
        a4.append((float(x2[j])*0.05))
        b4.append((float(y2[j])*0.05))

for i in range(len(a4)-1):
    x_d = abs(a4[i+1]-a4[i])
    y_d = abs(b4[i+1]-b4[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    fas_7.append(dist)


path3 = r"C:\Users\Vasanth\OneDrive\Desktop\12_0.csv"

df3 = pd.read_csv(path3)

a5=list(df3.x)
b5=list(df3.y)
trex_12=list(df3.velo)

trex_cal_12=[]

for i in range(len(a5)-1):
    x_d = abs(a5[i+1]-a5[i])
    y_d = abs(b5[i+1]-b5[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    trex_cal_12.append(dist)


with open('tracking_12.txt','r') as f:
    x3 = [column[6] for column in csv.reader(f,delimiter='\t')]

with open('tracking_12.txt','r') as f:
    y3 = [column[7] for column in csv.reader(f,delimiter='\t')]

with open('tracking_12.txt','r') as f:
    u3 = [column[22] for column in csv.reader(f,delimiter='\t')]

fas_12=[]
a6=[]
b6=[]

for j in range(len(u3)):
    if(u3[j]=='5'):
        a6.append((float(x3[j])*0.05))
        b6.append((float(y3[j])*0.05))

for i in range(len(a6)-1):
    x_d = abs(a6[i+1]-a6[i])
    y_d = abs(b6[i+1]-b6[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    fas_12.append(dist)

def sum1(mat):
    a = 0
    count = 0
    for i in range(len(mat)):
        if(mat[i]<1000000):
            a = a+mat[i]
            count = count + 1
    return (a/count)

v6_1 = (sum(fas_6))/(len(fas_6))
v6_2 = sum1(trex_cal_6)
v6_3 = sum1(trex_6)*0.05

v7_1 = (sum(fas_7))/(len(fas_7))
v7_2 = sum1(trex_cal_7)
v7_3 = sum1(trex_7)*0.05

v12_1 = (sum(fas_12))/(len(fas_12))
v12_2 = sum1(trex_cal_12)
v12_3 = sum1(trex_12)*0.05

barWidth = 0.25

fig = plt.subplots(figsize = (12,8))

FastTrack = [v6_1,v7_1,v12_1]
Trex_calc = [v6_2,v7_2,v12_2]
Trex_velo = [v6_3,v7_3,v12_3]

br1 = np.arange(len(FastTrack))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, FastTrack, color = 'r', width = barWidth, edgecolor = 'white', label = 'FastTrack')
plt.bar(br2, Trex_calc, color = 'g', width = barWidth, edgecolor = 'white', label = 'Trex_Calculated')
plt.bar(br3, Trex_velo, color = 'b', width = barWidth, edgecolor = 'white', label = 'Trex')

plt.xlabel('Trials', fontweight = 'bold', fontsize = 15)
plt.ylabel('Avg. Velocity', fontweight = 'bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(FastTrack))], ['Trial 6', 'Trial 7', 'Trial 12'])

plt.legend()
plt.show()

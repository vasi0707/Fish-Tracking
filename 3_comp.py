import csv
with open('tracking_vasanth.txt','r') as f:
    x_v = [column[6] for column in csv.reader(f,delimiter='\t')]

with open('tracking_vasanth.txt','r') as f:
    y_v = [column[7] for column in csv.reader(f,delimiter='\t')]

with open('tracking_vasanth.txt','r') as f:
    u_v = [column[22] for column in csv.reader(f,delimiter='\t')]

import pandas as pd
import math
import matplotlib.pyplot as plt

v_v=[]
a_v=[]
b_v=[]

for j in range(len(u_v)):
    if(u_v[j]=='5'):
        a_v.append((float(x_v[j])*0.05))
        b_v.append((float(y_v[j])*0.05))

for i in range(len(a_v)-1):
    x_d = abs(a_v[i+1]-a_v[i])
    y_d = abs(b_v[i+1]-b_v[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    v_v.append(dist)


with open('tracking_kaustab.txt','r') as f:
    x_k = [column[6] for column in csv.reader(f,delimiter='\t')]

with open('tracking_kaustab.txt','r') as f:
    y_k = [column[7] for column in csv.reader(f,delimiter='\t')]

with open('tracking_kaustab.txt','r') as f:
    u_k = [column[22] for column in csv.reader(f,delimiter='\t')]

v_k=[]
a_k=[]
b_k=[]

for j in range(len(u_k)):
    if(u_k[j]=='5'):
        a_k.append((float(x_k[j])*0.05))
        b_k.append((float(y_k[j])*0.05))

for i in range(len(a_k)-1):
    x_d = abs(a_k[i+1]-a_k[i])
    y_d = abs(b_k[i+1]-b_k[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    v_k.append(dist)

with open('tracking_sangeetha.txt','r') as f:
    x_s = [column[6] for column in csv.reader(f,delimiter='\t')]

with open('tracking_sangeetha.txt','r') as f:
    y_s = [column[7] for column in csv.reader(f,delimiter='\t')]

with open('tracking_sangeetha.txt','r') as f:
    u_s = [column[22] for column in csv.reader(f,delimiter='\t')]

v_s=[]
a_s=[]
b_s=[]

for j in range(len(u_s)):
    if(u_s[j]=='5'):
        a_s.append((float(x_s[j])*0.05))
        b_s.append((float(y_s[j])*0.05))

for i in range(len(a_s)-1):
    x_d = abs(a_s[i+1]-a_s[i])
    y_d = abs(b_s[i+1]-b_s[i])
    dist = math.sqrt((x_d*x_d)+(y_d*y_d))
    v_s.append(dist)

def vvv(m,p):
    new = 0
    for i in range(p,p+10):
        new = new + m[i]
    return (new/10)

avg = []
avg1 = []
avg2 = []

for i in range(0,len(v_v)-10,10):
    avg.append(vvv(v_v,i))

for i in range(0,len(v_k)-10,10):
    avg1.append(vvv(v_k,i))

for i in range(0,len(v_s)-10,10):
    avg2.append(vvv(v_s,i))


p = list(range(0,len(avg)))
p1 = list(range(0,len(avg1)))
p2 = list(range(0,len(avg2)))
plt.plot(p,avg,label = "Vasanth")
plt.plot(p1,avg1,label = "Kaustubh")
plt.plot(p2,avg2,label = "Sangeetha")
plt.legend()
plt.xlabel('Frames')
plt.ylabel('Velocity')
plt.title('FastTrack Comparison')
plt.show()

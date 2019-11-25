import random
import matplotlib.pyplot as plt
import math

date=[]
time=[]
d1=[]
d2=[]
rpm=[]
flag=0
f = open('testfile.txt')
line = f.readline()
while line:
    lol=line.split('T')
    if lol[0]=="20191120":
        flag=1
    if flag==1:
        date.append(int(lol[0]))
        lol=lol[1].split()
        time.append(int(lol[0]))
        lol=lol[1].split('(')
        lol=lol[1].split(',')
        d1.append(int(lol[0]))
        rpm.append(int(lol[2]))
        lol=lol[1].split(')')
        d2.append(int(lol[0]))
    line = f.readline()
f.close()

#Plotting distances
print(date,time,d1,d2,rpm)
plt.plot(d2,'-bo')
plt.xlabel('time') 
plt.ylabel('Distance 2') 
plt.savefig('./distance2.png')
plt.clf()

plt.plot(d1,'-go')
plt.xlabel('time') 
plt.ylabel('Distance 1') 
plt.savefig('./distance1.png')
plt.clf()

plt.plot(rpm,'-yo')
plt.xlabel('time') 
plt.ylabel('RPM') 
plt.savefig('./rpm_o.png')
plt.clf()

#Daily traffic
curdate=-1
count=0
sum=0
traffic=[]
index=0
indices=[]

for i in range(len(d1)):
    print(date[i])
    print(i)
    if(curdate==date[i]):
        sum+=d1[i]+d2[i]
        count+=1
    else:
        print(i)
        if(count>0):
            sum/=count
            traffic.append(sum)
            indices.append(index)
            count=0
            sum=0
            index+=1
        curdate=date[i]
        sum+=d1[i]+d2[i]
        count+=1

if(count>0):
    sum/=count
    traffic.append(sum)
    indices.append(index)

# print(traffic,indices)
plt.bar(indices,traffic, width=0.3,color = ['brown']) 
plt.xlabel('Day') 
plt.ylabel('Traffic') 
plt.savefig('./daily.png')
plt.clf()

#Daily traffic
curdate=20191120
count=[0]*24
sum=0
traffic=[0]*24
indices=[]

for i in range(len(d1)):
    if curdate==date[i]:
        tm=int(time[i]/10000)
        count[tm]+=1
        traffic[tm]+=d1[i]+d2[i]

for i in range(24):
    if count[i]>0:
        traffic[i]=traffic[i]/count[i]
    else: 
        traffic[i]=0
    indices.append(i)

print(traffic)
print(indices)
plt.bar(indices,traffic,color = ['orange']) 
plt.xlabel('Hour') 
plt.ylabel('Traffic') 
plt.savefig('./hourly.png')
plt.clf()
# plt.show()
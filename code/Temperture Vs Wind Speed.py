import matplotlib.pylab as plt
import numpy as np
import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

x15, y15 = np.genfromtxt(dir+'/source/Weather_2015.csv',delimiter=',',
                         usecols=[1,7],unpack=True)
filter15 = np.logical_and(x15 >= 0, y15 >= -100)
print('Analysis of Weather 2015 Data Completed')


x16, y16 = np.genfromtxt(dir+'/source/Weather_2016.csv',delimiter=',',
                         usecols=[1,7],unpack=True)
filter16 = np.logical_and(x16 >= 0, y16 >= -100)
print('Analysis of Weather 2016 Data Completed')

x17, y17 = np.genfromtxt(dir+'/source/Weather_2017.csv',delimiter=',',
                         usecols=[1,7],unpack=True)
filter17 = np.logical_and(x17 >= 0, y17 >= -100)
print('Analysis of Weather 2017 Data Completed')

x = np.concatenate((x15[filter15],x16[filter16],x17[filter17]))
y = np.concatenate((y15[filter15],y16[filter16],y17[filter17]))


plt.plot(x15[filter15],y15[filter15],'k,')
plt.xlabel('Temperture (Degrees)')
plt.ylabel('Wind Speed (kph)')
plt.title('2015 Temperture Vs Wind Speed Graph')
plt.savefig(dir+'/results/2015 Temperture Vs Wind Speed.png')

plt.figure()
plt.plot(x16[filter16],y16[filter16],'k,')
plt.xlabel('Temperture (Degrees)')
plt.ylabel('Wind Speed (kph)')
plt.title('2016 Temperture Vs Wind Speed Graph')
plt.savefig(dir+'/results/2016 Temperture Vs Wind Speed.png')


plt.figure()
plt.plot(x17[filter17],y17[filter17],'k,')
plt.xlabel('Temperture (Degrees)')
plt.ylabel('Wind Speed (kph)')
plt.title('2017 Temperture Vs Wind Speed Graph')
plt.savefig(dir+'/results/2017 Temperture Vs Wind Speed.png')


plt.figure()
plt.hexbin(x,y,bins='log')
plt.xlabel('Temperture (Degrees)')
plt.ylabel('Wind Speed (kph)')
plt.title('All Temperture Vs Wind Speed Graph')
plt.savefig(dir+'/results/All Temperture Vs Winds Speed.png')
plt.show()

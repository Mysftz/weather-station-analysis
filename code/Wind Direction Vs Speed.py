import matplotlib.pylab as plt
import numpy as np
import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

#plotonx = int(input('Type column ID')
x15, y15 = np.genfromtxt(dir+'/source/Weather_2015.csv',delimiter=',',usecols=[10,7],unpack=True)
#x15 = getColumn("Weather_2015.csv",0) 
#y15 = getColumn("Weather_2015.csv",2)
print('Weather 2015 Data Completed')
print('33.3% Completed')

filter15 = np.logical_and(x15 >= 0, y15 >= -1000)

x16, y16 = np.genfromtxt(dir+'/source/Weather_2016.csv',delimiter=',',usecols=[10,7],unpack=True)
#x16 = getColumn("Weather_2016.csv",0) 
#y16 = getColumn("Weather_2016.csv",2)
print('Weather 2016 Data Completed')
print('66.6% Completed')

filter16 = np.logical_and(x16 >= 0, y16 >= -1000)

x17, y17 = np.genfromtxt(dir+'/source/Weather_2017.csv',delimiter=',',usecols=[10,7],unpack=True)
#x17 = getColumn("Weather_2017.csv",0) 
#y17 = getColumn("Weather_2017.csv",2)
print('Weather 2017 Data Completed')
print('99.9% Completed')

filter17 = np.logical_and(x17 >= 0, y17 >= -1000)

plt.plot(x15[filter15],y15[filter15],'k,')
plt.xlabel('Wind Direction (Degrees)')
plt.ylabel('Wind Speed (kph)')
plt.title('2015 Wind Direction Vs Speed Graph')
plt.savefig(dir+'/results/2015 Wind Direction Vs Speed.png')

plt.figure()
plt.plot(x16[filter16],y16[filter16],'k,')
plt.xlabel('Wind Direction (Degrees)')
plt.ylabel('Wind Speed (kph)')
plt.title('2016 Wind Direction Vs Speed Graph')
plt.savefig(dir+'/results/2016 Wind Direction Vs Speed.png')

plt.figure()
plt.plot(x17[filter17],y17[filter17],'k,')
plt.xlabel('Wind Direction (Degrees)')
plt.ylabel('Wind Speed (kph)')
plt.title('2017 Wind Direction Vs Speed Graph')
plt.savefig(dir+'/results/2017 Wind Direction Vs Speed.png')

plt.show()

x = np.concatenate((x15[filter15],x16[filter16],x17[filter17]))

y = np.concatenate((y15[filter15],y16[filter16],y17[filter17]))

plt.figure()
plt.hexbin(x,y,bins='log')
plt.xlabel('Wind Direction (Degrees)')
plt.ylabel('Wind Speed (kph)')
plt.title('All Wind Direction Vs Speed Graph')
plt.savefig(dir+'/results/All Wind Direction Vs Speed.png')

plt.show()

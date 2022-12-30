# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: YOUR NAME
# Section: YOUR SECTION NUMBER
# Assignment: THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date: DAY MONTH YEAR
#
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
#initializes all lsit variables we will use
dates = []
maxtemp = []
mintemp = []
precipitation = []
averagetemp = []
windspeed = []
#were gonna utilize DictReader to easily read and sort the data of the WeaterDataCLL file
#Old code from previous lab to collect weather data
with open("WeatherDataCLL.csv","r") as weatherdata: 
    weatherline = csv.DictReader(weatherdata,delimiter = ",")
    for line in weatherline:
        #fills in only Dates
        dates.append(line['Date'])
        #Fills in only max temps
        maxtemp.append(int(line["Maximum Temperature (F)"]))
        #fills in only min temp
        mintemp.append(int(line["Minimum Temperature (F)"]))
        #fills in the precipittion
        precipitation.append(float(line["Precipitation (in)"]))
        #fills in average temps
        averagetemp.append(int(line["Average Temperature (F)"]))
        #fills in wind speed
        windspeed.append(float(line["Average Daily Wind Speed (mph)"]))
#plots first graph
temppts = np.array([maxtemp])#makes max temp and array
tempx = np.arange(0,len(dates))#makes our x values for our graph an array based on length of the data
mintempx = np.array([mintemp])
windpts = np.array([windspeed])#makes our avg wind speed an array
windx = np.arange(0,len(dates))#creates x values as an array for our wind y points based on the length of the data
fig,ax = plt.subplots()
ax2 = ax.twinx()
plt.figure()
#plots the graph
for i in range(len(temppts)):
    a, = ax.plot(tempx,temppts[i],'r', label = "Max Temp, F")
    b, = ax2.plot(windx,windpts[i],'b', label = "Avg Wind Spped, mph")
#sets up our legend
ax.legend(handles = [a,b], loc = "upper left")
#sets up our axes
ax2.set_ylabel("Wind speeds")
ax.set_ylabel("Max temp")
ax.set_xlabel("Dates")
ax.set_title("Maximum temperature and Average wind speed")
plt.show()

#plots our 2nd graph
for i in range(len(temppts)):
   plt.hist(windpts[i],bins = 29, color = 'g')#creates a histogram based on avg wind speed
#sets up the axes
plt.xlabel("Average Wind Speed, mph")
plt.ylabel("Number of Days")
plt.title("Histogram of average wind sppeds")
plt.show()

#plots 3rd graph
for i in range(len(windpts)):
#creates a scatter plot baased on the wind y made from our minimal temperature as an x
    plt.scatter(mintempx,windpts[i], linewidth = 0.05, color = 'k')
#sets up the axes
plt.xlabel("AMinimum temperature, F")
plt.ylabel("Average wind speeds")
plt.title("Average wind speed vs. Mininum temperature")

plt.show()

#creates a bunch of list 2 store each months data
jc = []
fc = []
mc = []
ac = []
mac=[]
julc=[]
juc=[]
auc=[]
sc=[]
oc=[]
nc=[]
dc =[]
months = [jc,fc,mc,ac,mac,julc,juc,auc,sc,oc,nc,dc]
maxtemp = [None]
mintemp = [None]
fig,by = plt.subplots()

plt.figure()
#loops through our data and sorts them into their correct month based on the first index of the list 'dates'
for i in range(len(dates)):
    if dates[i][0] == '1' and dates[i][1] == '/':
        jc.append(averagetemp[i])
    elif dates[i][0] == '2' and dates[i][1] == '/':
        fc.append( averagetemp[i])
    elif dates[i][0] == '3' and dates[i][1] == '/':
        mc.append( averagetemp[i])
    elif dates[i][0] == '4' and dates[i][1] == '/':
       ac.append( averagetemp[i])
    elif dates[i][0] == '5' and dates[i][1] == '/':
        mac.append(averagetemp[i])
    elif dates[i][0] == '6' and dates[i][1] == '/':
        julc.append( averagetemp[i])
    elif dates[i][0] == '7' and dates[i][1] == '/':
        juc.append( averagetemp[i])
    elif dates[i][0] == '8' and dates[i][1] == '/':
       auc.append( averagetemp[i])
    elif dates[i][0] == '9' and dates[i][1] == '/':
       sc.append( averagetemp[i])
    elif dates[i][0:2] == '10':
        oc.append(averagetemp[i])
    elif dates[i][0:2] == '11':
       nc.append(averagetemp[i])
    elif dates[i][0:2] == '12':
        dc.append(averagetemp[i])
#adjust our axes of the bar graph
by = fig.add_axes([0,0,1,1])
#loops through our month list(length = 12) and plots each month as an average
for i in range(len(months)):
    by.bar(i+1,sum(months[i])/len(months[i]), color = 'y')
#wer now create 2 more list that will find the max and mins of each months temperature
for i in range(12):
    maxtemp.append(max(months[i]))
    mintemp.append(min(months[i]))
#we plot the max and min temperature as a line graph
a, = by.plot(maxtemp,color = 'r', linewidth = "1",label = "Maximum Temp, F")
b, = by.plot(mintemp, color = 'b', linewidth = "1", label = "Minimum Temp, F")
by.legend(handles = [a,b])
plt.show()


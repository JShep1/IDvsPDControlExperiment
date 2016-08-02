import os,sys
import pylab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

############################
# TODO: set values here 
# see figure 1 in homework for definition of variables
set_point = 0.0 
rise_time = 0.02
peak_time = 0.01
overshoot = 0.02
settling_time = 0.1

# Error bands are at y = (1 +/- delta)
error_band_delta = 0.02

# offset for text
eps = .05
############################

# check proper number of arguments given
if len(sys.argv) < 2:
  print 'syntax: plotActvDes.py <joint name>'
  sys.exit(0)  

# setup font
font =  {'family' : 'sans-serif',
         'color'  : 'black',
         'weight' : 'normal',
         'size'   : 16,
        }

# step size (constant value)
DT05 = 0.05
DT1 = 0.1
DT01 = 0.01
DT001 = 0.001

# load data
y1 = pylab.loadtxt(sys.argv[1] + "_desired001.txt")
y2 = pylab.loadtxt(sys.argv[1] + "_state001.txt")
y3 = pylab.loadtxt(sys.argv[1] + "_state01.txt")
y4 = pylab.loadtxt(sys.argv[1] + "_state05.txt")
y5 = pylab.loadtxt(sys.argv[1] + "_state1.txt")

t001 = np.linspace(0,y1.size*DT001,y1.size)
t01 = np.linspace(0,y3.size*DT01,y3.size)
t1 = np.linspace(0,y5.size*DT1,y5.size)
t05 = np.linspace(0,y4.size*DT05,y4.size)


for i in range(0,y2.size):
	y2[i]=y2[i]*y2[i]

for i in range(0,y3.size):
	y3[i]=y3[i]*y3[i]

for i in range(0,y4.size):
	y4[i]=y4[i]*y4[i]

for i in range(0,y5.size):
	y5[i]=y5[i]*y5[i]




# setup the figure
fig = plt.figure()

# plot data
plt.plot(t001,y1,'k' ,label='Des')
plt.plot(t001,y2,'r' ,label='Act-0.001')
plt.plot(t01,y3,'b' ,label='Act-0.01')
plt.plot(t05,y4,'g' ,label='Act-0.05')
plt.plot(t1,y5,'y' ,label='Act-0.10')

# set limits
axPlot = plt.subplot(111)
axPlot.set_xlim(.5, 5)

# add titles, labels, and legend
plt.title('Squared Velocity Error', fontdict=font)
plt.xlabel('Time', fontdict=font)
plt.ylabel('Error', fontdict=font)
plt.legend(loc=4, shadow=True)

# annotate rise time (interval)
#plt.axhspan(set_point-error_band_delta,set_point+error_band_delta, facecolor='0.5', alpha=0.25)
#plt.axhline(y=set_point-error_band_delta, color='k',linestyle='--')
#plt.axvspan(0.0,rise_time,facecolor='0.5', alpha=0.25)
#plt.axvline(x=rise_time, color='k',linestyle='--')
#plt.annotate('rise time', xy=(rise_time-.5, set_point-eps))

# annotate peak_time
#plt.axvline(x=peak_time, color='k',linestyle='--')
#plt.annotate('peak time', xy=(peak_time+.1, set_point-2*eps))

# annotate overshoot
#plt.axhline(y=overshoot, xmin=0, xmax=peak_time,color='k',linestyle='--')
#plt.annotate('overshoot', xy=(peak_time, overshoot+eps))

# annotate settling time
#plt.axvline(x=settling_time,color='k',linestyle='--')
#plt.annotate('settling time', xy=(settling_time, set_point+eps))

# draw error band
#plt.axhspan(set_point-error_band_delta,set_point+error_band_delta, facecolor='0.5', alpha=0.25)
#plt.axhline(y=set_point-error_band_delta, color='k',linestyle='--')
#plt.axhline(y=set_point+error_band_delta, color='k',linestyle='--')
#plt.plot([0, y1[:,0].size*DT], [-0.5, -0.5], '--', lw=1.0)
#plt.plot([0, y1[:,0].size*DT], [-1.5, -1.5], '--', lw=1.0)
#plt.annotate('error band', xy=(10.1, set_point))

# show the plot
#plt.show()

# save the plot
plt.savefig(sys.argv[1] + 'error.png')


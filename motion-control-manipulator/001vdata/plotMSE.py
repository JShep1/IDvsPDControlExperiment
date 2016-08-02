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
elbowdesired = pylab.loadtxt("elbow_joint_desired001.txt")
shoulderliftdesired = pylab.loadtxt("shoulder_lift_joint_desired001.txt")
shoulderpandesired = pylab.loadtxt("shoulder_pan_joint_desired001.txt")
wrist1desired = pylab.loadtxt("wrist_1_joint_desired001.txt")
wrist2desired = pylab.loadtxt("wrist_2_joint_desired001.txt")
wrist3desired = pylab.loadtxt("wrist_3_joint_desired001.txt")
lfingerdesired = pylab.loadtxt("l_finger_actuator_desired001.txt")
rfingerdesired = pylab.loadtxt("r_finger_actuator_desired001.txt")

elbow001 = pylab.loadtxt("elbow_joint_state001.txt")
shoulderlift001 = pylab.loadtxt("shoulder_lift_joint_state001.txt")
shoulderpan001 = pylab.loadtxt("shoulder_pan_joint_state001.txt")
wrist1001 = pylab.loadtxt("wrist_1_joint_state001.txt")
wrist2001 = pylab.loadtxt("wrist_2_joint_state001.txt")
wrist3001 = pylab.loadtxt("wrist_3_joint_state001.txt")
lfinger001 = pylab.loadtxt("l_finger_actuator_state001.txt")
rfinger001 = pylab.loadtxt("r_finger_actuator_state001.txt")

elbow01 = pylab.loadtxt("elbow_joint_state01.txt")
shoulderlift01 = pylab.loadtxt("shoulder_lift_joint_state01.txt")
shoulderpan01 = pylab.loadtxt("shoulder_pan_joint_state01.txt")
wrist101 = pylab.loadtxt("wrist_1_joint_state01.txt")
wrist201 = pylab.loadtxt("wrist_2_joint_state01.txt")
wrist301 = pylab.loadtxt("wrist_3_joint_state01.txt")
lfinger01 = pylab.loadtxt("l_finger_actuator_state01.txt")
rfinger01 = pylab.loadtxt("r_finger_actuator_state01.txt")


elbow05 = pylab.loadtxt("elbow_joint_state05.txt")
shoulderlift05 = pylab.loadtxt("shoulder_lift_joint_state05.txt")
shoulderpan05 = pylab.loadtxt("shoulder_pan_joint_state05.txt")
wrist105 = pylab.loadtxt("wrist_1_joint_state05.txt")
wrist205 = pylab.loadtxt("wrist_2_joint_state05.txt")
wrist305 = pylab.loadtxt("wrist_3_joint_state05.txt")
lfinger05 = pylab.loadtxt("l_finger_actuator_state05.txt")
rfinger05 = pylab.loadtxt("r_finger_actuator_state05.txt")

elbow1 = pylab.loadtxt("elbow_joint_state1.txt")
shoulderlift1 = pylab.loadtxt("shoulder_lift_joint_state1.txt")
shoulderpan1 = pylab.loadtxt("shoulder_pan_joint_state1.txt")
wrist11 = pylab.loadtxt("wrist_1_joint_state1.txt")
wrist21 = pylab.loadtxt("wrist_2_joint_state1.txt")
wrist31 = pylab.loadtxt("wrist_3_joint_state1.txt")
lfinger1 = pylab.loadtxt("l_finger_actuator_state1.txt")
rfinger1 = pylab.loadtxt("r_finger_actuator_state1.txt")


t001 = np.linspace(0,elbowdesired.size*DT001,elbowdesired.size)
t01 = np.linspace(0,elbow01.size*DT01,elbow01.size)
t1 = np.linspace(0,elbow1.size*DT1,elbow1.size)
t05 = np.linspace(0,elbow05.size*DT05,wlbow05.size)

total_error001 = [];
total_error01 = [];
total_error1 = [];
total_error05 = [];

for i in range(0,elbow001.size):
	total_error001[i] = elbow001[i] * elbow001[i]
	total_error001[i] = total_error001[i] + shoulderlift001[i] * shoulderlift001[i]
	total_error001[i] = total_error001[i] + shoulderpan001[i] * shoulderpan001[i]
	total_error001[i] = total_error001[i] + wrist1001[i] * wrist1001[i]
	total_error001[i] = total_error001[i] + wrist2001[i] * wrist2001[i]
	total_error001[i] = total_error001[i] + wrist3001[i] * wrist3001[i]
	total_error001[i] = total_error001[i] + lfinger001[i] * lfinger001[i]
	total_error001[i] = total_error001[i] + rfinger001[i] * rfinger001[i]
	total_error001[i] = total_error001[i] / 8.0


for i in range(0,elbow01.size):
	total_error01[i] = elbow01[i] * elbow01[i]
	total_error01[i] = total_error01[i] + shoulderlift01[i] * shoulderlift01[i]
	total_error01[i] = total_error01[i] + shoulderpan01[i] * shoulderpan01[i]
	total_error01[i] = total_error01[i] + wrist101[i] * wrist101[i]
	total_error01[i] = total_error01[i] + wrist201[i] * wrist201[i]
	total_error01[i] = total_error01[i] + wrist301[i] * wrist301[i]
	total_error01[i] = total_error01[i] + lfinger01[i] * lfinger01[i]
	total_error01[i] = total_error01[i] + rfinger01[i] * rfinger01[i]
	total_error01[i] = total_error01[i] / 8.0

for i in range(0,elbow05.size):
	total_error05[i] = elbow05[i] * elbow05[i]
	total_error05[i] = total_error05[i] + shoulderlift05[i] * shoulderlift05[i]
	total_error05[i] = total_error05[i] + shoulderpan05[i] * shoulderpan05[i]
	total_error05[i] = total_error05[i] + wrist105[i] * wrist105[i]
	total_error05[i] = total_error05[i] + wrist205[i] * wrist205[i]
	total_error05[i] = total_error05[i] + wrist305[i] * wrist305[i]
	total_error05[i] = total_error05[i] + lfinger05[i] * lfinger05[i]
	total_error05[i] = total_error05[i] + rfinger05[i] * rfinger05[i]
	total_error05[i] = total_error05[i] / 8.0

for i in range(0,elbow1.size):
	total_error1[i] = elbow1[i] * elbow1[i]
	total_error1[i] = total_error1[i] + shoulderlift1[i] * shoulderlift1[i]
	total_error1[i] = total_error1[i] + shoulderpan1[i] * shoulderpan1[i]
	total_error1[i] = total_error1[i] + wrist11[i] * wrist11[i]
	total_error1[i] = total_error1[i] + wrist21[i] * wrist21[i]
	total_error1[i] = total_error1[i] + wrist31[i] * wrist31[i]
	total_error1[i] = total_error1[i] + lfinger1[i] * lfinger1[i]
	total_error1[i] = total_error1[i] + rfinger1[i] * rfinger1[i]
	total_error1[i] = total_error1[i] / 8.0



# setup the figure
fig = plt.figure()

# plot data
plt.plot(t001,total_error001,'r' ,label='0.001')
plt.plot(t01,total_error01,'b' ,label='0.01')
plt.plot(t05,total_error05,'g' ,label='0.05')
plt.plot(t1,total_error1,'y' ,label='0.10')

# set limits
axPlot = plt.subplot(111)
axPlot.set_xlim(.5, 5)

# add titles, labels, and legend
plt.title('Mean Squared Error for ID Controller on Quadruped', fontdict=font)
plt.xlabel('Time', fontdict=font)
plt.ylabel('Error', fontdict=font)
plt.legend(loc=4, shadow=True)
plt.yscale('log');
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
plt.savefig('MSE.png')


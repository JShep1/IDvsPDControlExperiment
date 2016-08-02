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
if len(sys.argv) < 1:
  print 'syntax: plotMSE.py'
  sys.exit(0)  

# setup font
font =  {'family' : 'sans-serif',
         'color'  : 'black',
         'weight' : 'normal',
         'size'   : 16,
        }
legendfont =  {'family' : 'sans-serif',
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

elbowPD = pylab.loadtxt("elbow_joint_statePID.txt")
shoulderliftPD = pylab.loadtxt("shoulder_lift_joint_statePID.txt")
shoulderpanPD = pylab.loadtxt("shoulder_pan_joint_statePID.txt")
wrist1PD = pylab.loadtxt("wrist_1_joint_statePID.txt")
wrist2PD = pylab.loadtxt("wrist_2_joint_statePID.txt")
wrist3PD = pylab.loadtxt("wrist_3_joint_statePID.txt")
lfingerPD = pylab.loadtxt("l_finger_actuator_statePID.txt")
rfingerPD = pylab.loadtxt("r_finger_actuator_statePID.txt")

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


t001 = np.linspace(-0.6,elbowdesired.size*DT001,elbowdesired.size)
t01 = np.linspace(-0.6,elbow01.size*DT01,elbow01.size)
t1 = np.linspace(-0.6,elbow1.size*DT1,elbow1.size)
t05 = np.linspace(-0.6,elbow05.size*DT05,elbow05.size)

total_error001 = [None] * elbow001.size;
total_errorPD = [None] * elbow001.size;
total_error01 = [None] * elbow01.size;
total_error1 = [None] * elbow1.size;
total_error05 = [None] * elbow05.size;

for i in range(0,elbow001.size):
	if i > 500:	
		total_error001[i] = abs(elbow001[i])
		total_error001[i] = total_error001[i] + abs(shoulderlift001[i])
		total_error001[i] = total_error001[i] + abs(shoulderpan001[i])
		total_error001[i] = total_error001[i] + abs(wrist1001[i])
		total_error001[i] = total_error001[i] + abs(wrist2001[i])
		total_error001[i] = total_error001[i] + abs(wrist3001[i])
		total_error001[i] = total_error001[i] + abs(lfinger001[i])
		total_error001[i] = total_error001[i] + abs(rfinger001[i])
		total_error001[i] = total_error001[i] / 8.0
		
		total_errorPD[i] = abs(elbowPD[i])
		total_errorPD[i] = total_errorPD[i] + abs(shoulderliftPD[i])
		total_errorPD[i] = total_errorPD[i] + abs(shoulderpanPD[i])
		total_errorPD[i] = total_errorPD[i] + abs(wrist1PD[i])
		total_errorPD[i] = total_errorPD[i] + abs(wrist2PD[i])
		total_errorPD[i] = total_errorPD[i] + abs(wrist3PD[i])
		total_errorPD[i] = total_errorPD[i] + abs(lfingerPD[i])
		total_errorPD[i] = total_errorPD[i] + abs(rfingerPD[i])
		total_errorPD[i] = total_errorPD[i] / 8.0


for i in range(0,elbow01.size):
	if i > 50:
		total_error01[i] = abs(elbow01[i])
		total_error01[i] = total_error01[i] + abs(shoulderlift01[i])
		total_error01[i] = total_error01[i] + abs(shoulderpan01[i])
		total_error01[i] = total_error01[i] + abs(wrist101[i])
		total_error01[i] = total_error01[i] + abs(wrist201[i])
		total_error01[i] = total_error01[i] + abs(wrist301[i])
		total_error01[i] = total_error01[i] + abs(lfinger01[i])
		total_error01[i] = total_error01[i] + abs(rfinger01[i])
		total_error01[i] = total_error01[i] / 8.0

for i in range(0,elbow05.size):
	if i >= 10:
		total_error05[i] = abs(elbow05[i])
		total_error05[i] = total_error05[i] + abs(shoulderlift05[i])
		total_error05[i] = total_error05[i] + abs(shoulderpan05[i])
		total_error05[i] = total_error05[i] + abs(wrist105[i])
		total_error05[i] = total_error05[i] + abs(wrist205[i])
		total_error05[i] = total_error05[i] + abs(wrist305[i])
		total_error05[i] = total_error05[i] + abs(lfinger05[i])
		total_error05[i] = total_error05[i] + abs(rfinger05[i])
		total_error05[i] = total_error05[i] / 8.0

for i in range(0,elbow1.size):
	if i >= 5:
		total_error1[i] = abs(elbow1[i])
		total_error1[i] = total_error1[i] + abs(shoulderlift1[i])
		total_error1[i] = total_error1[i] + abs(shoulderpan1[i])
		total_error1[i] = total_error1[i] + abs(wrist11[i])
		total_error1[i] = total_error1[i] + abs(wrist21[i])
		total_error1[i] = total_error1[i] + abs(wrist31[i])
		total_error1[i] = total_error1[i] + abs(lfinger1[i])
		total_error1[i] = total_error1[i] + abs(rfinger1[i])
		total_error1[i] = total_error1[i] / 8.0

print '%f %f %f %f %f' % (max(total_errorPD),max(total_error001),max(total_error01),max(total_error05),max(total_error1))

# setup the figure
fig = plt.figure()

# plot data
plt.plot(t001,total_errorPD,'c' ,label='PID - 0.001')
plt.plot(t001,total_error001,'r' ,linestyle='-.',label='0.001')
plt.plot(t01,total_error01,'b' ,linestyle='--',label='0.01')
plt.plot(t05,total_error05,'g' ,marker='.',label='0.05')
plt.plot(t1,total_error1,'y' ,marker='o',label='0.10')

# set limits
axPlot = plt.subplot(111)
axPlot.set_xlim(0, 5)


# add titles, labels, and legend
plt.title('Mean Error for ID Controller on UR10', fontdict=font)
plt.xlabel('Time', fontdict=font)
plt.ylabel('Error', fontdict=font)
plt.legend(loc=3, shadow=True,fontsize='10')


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


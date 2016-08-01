#!/bin/bash

python plot_PD_PID.py elbow_joint
python plot_PD_PID.py shoulder_pan_joint
python plot_PD_PID.py shoulder_lift_joint
python plot_PD_PID.py wrist_1_joint
python plot_PD_PID.py wrist_2_joint
python plot_PD_PID.py wrist_3_joint
python plot_PD_PID.py l_finger_actuator
python plot_PD_PID.py r_finger_actuator

rm fixed*
rm world*

rm data/*
mv *05.txt /data/
rm *PID.txt 

rm plots/*
mv *.png /plots/


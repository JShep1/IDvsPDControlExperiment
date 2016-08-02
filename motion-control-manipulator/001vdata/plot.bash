#!/bin/bash

cp plotActvDes.py actvsdes/
cd actvsdes

python plotActvDes.py elbow_joint
python plotActvDes.py shoulder_lift_joint
python plotActvDes.py shoulder_pan_joint
python plotActvDes.py wrist_1_joint
python plotActvDes.py wrist_2_joint
python plotActvDes.py wrist_3_joint
python plotActvDes.py l_finger_actuator
python plotActvDes.py r_finger_actuator
mv *.png ../plots/actvsdes/

cd ..
cp plotError.py error/
cd error/

python plotError.py elbow_joint
python plotError.py shoulder_lift_joint
python plotError.py shoulder_pan_joint
python plotError.py wrist_1_joint
python plotError.py wrist_2_joint
python plotError.py wrist_3_joint
python plotError.py l_finger_actuator
python plotError.py r_finger_actuator
mv *.png ../plots/error/



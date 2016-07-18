#!/bin/bash

rm wrist1/*.py
rm wrist2/*.py
rm wrist3/*.py
rm elbow/*.py
rm shoulderlift/*.py
rm shoulderpan/*.py
rm lfinger/*.py
rm rfinger/*.py

cp plotGearJoints.py elbow/
cp plotGearJoints.py shoulderlift/
cp plotGearJoints.py shoulderpan/
cp plotGearJoints.py wrist1/
cp plotGearJoints.py wrist2/
cp plotGearJoints.py wrist3/
cp plotGearJoints.py lfinger/
cp plotGearJoints.py rfinger/

cp plotThreeSeconds.py elbow/
cp plotThreeSeconds.py shoulderlift/
cp plotThreeSeconds.py shoulderpan/
cp plotThreeSeconds.py wrist1/
cp plotThreeSeconds.py wrist2/
cp plotThreeSeconds.py wrist3/
cp plotThreeSeconds.py lfinger/
cp plotThreeSeconds.py rfinger/

cd elbow/
python plotGearJoints.py elbow
cp elbow_error.png ..
python plotThreeSeconds.py elbow
cp elbow_error3.png ..
cd ..

cd shoulderlift/
python plotGearJoints.py shoulderlift
cp shoulderlift_error.png ..
python plotThreeSeconds.py shoulderlift
cp shoulderlift_error3.png ..
cd ..

cd shoulderpan/
python plotGearJoints.py shoulderpan
cp shoulderpan_error.png ..
python plotThreeSeconds.py shoulderpan
cp shoulderpan_error3.png ..
cd ..

cd wrist1/
python plotGearJoints.py wrist_1
cp wrist_1_error.png ..
python plotThreeSeconds.py wrist_1
cp wrist_1_error3.png ..
cd ..

cd wrist2/
python plotGearJoints.py wrist_2
cp wrist_2_error.png ..
python plotThreeSeconds.py wrist_2
cp wrist_2_error3.png ..
cd ..

cd wrist3/
python plotGearJoints.py wrist_3
cp wrist_3_error.png ..
python plotThreeSeconds.py wrist_3
cp wrist_3_error3.png ..
cd ..

cd lfinger/
python plotGearJoints.py l_finger
cp l_finger_error.png ..
python plotThreeSeconds.py l_finger
cp l_finger_error3.png ..
cd ..

cd rfinger/
python plotGearJoints.py r_finger
cp r_finger_error.png ..
python plotThreeSeconds.py r_finger
cp r_finger_error3.png ..
cd ..

rm allplots/*.png
mv *.png allplots/




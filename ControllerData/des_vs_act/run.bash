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
python plotThreeSeconds.py elbow
cp elbow_actvsdes.png ..
cp elbow_actvsdes3.png ..
cd ..

cd shoulderlift/
python plotGearJoints.py shoulderlift
python plotThreeSeconds.py shoulderlift
cp shoulderlift_actvsdes3.png ..
cp shoulderlift_actvsdes.png ..
cd ..

cd shoulderpan/
python plotGearJoints.py shoulderpan
python plotThreeSeconds.py shoulderpan
cp shoulderpan_actvsdes3.png ..
cp shoulderpan_actvsdes.png ..
cd ..

cd wrist1/
python plotGearJoints.py wrist_1
python plotThreeSeconds.py wrist_1
cp wrist_1_actvsdes3.png ..
cp wrist_1_actvsdes.png ..
cd ..

cd wrist2/
python plotGearJoints.py wrist_2
python plotThreeSeconds.py wrist_2
cp wrist_2_actvsdes3.png ..
cp wrist_2_actvsdes.png ..
cd ..

cd wrist3/
python plotGearJoints.py wrist_3
python plotThreeSeconds.py wrist_3
cp wrist_3_actvsdes3.png ..
cp wrist_3_actvsdes.png ..
cd ..


cd lfinger/
python plotGearJoints.py l_finger
python plotThreeSeconds.py l_finger
cp l_finger_actvsdes3.png ..
cp l_finger_actvsdes.png ..
cd ..

cd rfinger/
python plotGearJoints.py r_finger
python plotThreeSeconds.py r_finger
cp r_finger_actvsdes3.png ..
cp r_finger_actvsdes.png ..
cd ..

rm allplots/*.png
mv *.png allplots/




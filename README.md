# Robust, Multilevel Algorithm for Thoracic Vertebra Bone Measurements in Conventional Chest CT: Gender and Ethnicity Analysis Using the Multi-Ethnic Study of Atherosclerosis

### Purpose:
To develop and validate an automated, multilevel, multiplanar approach for thoracic vertebral bone measurements using conventional chest CT and investigate the pattern of measurements according to sex/gender and race/ethnicity using the Multi-Ethnic Study of Atherosclerosis (MESA) cohort.

### Methods:
A multicenter (n=6), prospective cohort (MESA exam 5, n=3,083 participants) underwent noncontrast chest CT with (n=296) and without (n=2,787) phantom. T1-T10 vertebrae were recursively selected in axial (planes (n=30,150, one for each vertebral level) and sagittal (n=6,030, upper and lower thoracic spine). A custom instance segmentation algorithm was developed. The internal validation set (n=360 participants, Northwestern University) was trained and tested and applied to an independent, external validation set (n=240 participants, University of Minnesota). We extracted pixel intensity (Hounsfield Units (HU)) and 2D surface area (mm2).

### Results:
The internal and external validation sets differed (P<0.001) according to race, HU, vertebral bone mineral density (vBMD), and surface area. Dice score for the internal (0.94 [0.94-0.93], 0.90 [0.91-0.89], 0.90 [0.91-0.89]) and external (0.93 [0.94-0.92], 0.87 [0.88-0.85], 0.85 [0.86-0.84]) validation set were reported for axial, T1-T5 sagittal, and T6-T10 sagittal, respectively. AI-derived HU were correlated with manual vBMD measurements from T1-T10 (R2=0.77, P<0.001). Black/African American participants had 34% (P<0.001) less variability in HU between T1-T10 compared with white/Caucasians. The surface area of vertebrae significantly increased from T1 (201 mm2) to T10 (903 mm2) in all races.

### Conclusions:
Our automated, multilevel algorithm can opportunistically determine the pattern of BMD and shape measurements in thoracic vertebrae from any conventional chest CT, revealing distinct distribution according to age, race, and gender.


## Manual (green) versus Infered (orange) traces
![alt text](https://github.com/qahathaway/vBMD/blob/main/Inference_vBMD.jpg)

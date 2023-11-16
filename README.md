# Robust, Multilevel Algorithm for Thoracic Vertebra Bone Measurements in Conventional Chest CT: Gender and Ethnicity Analysis Using the Multi-Ethnic Study of Atherosclerosis

## Training weights and COCO weights
##### Please contact qahathaway if you need the training weights or the pre-trained COCO weights, as storage on GitHub is difficult to maintain

##### Mask R-CNN pretrained COCO weigths link: https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5

### Purpose:
To develop and validate an automated, multilevel, multiplanar approach for thoracic vertebral bone measurements using conventional chest CT and investigate the pattern of measurements according to sex/gender and race/ethnicity using the Multi-Ethnic Study of Atherosclerosis (MESA) cohort.

### Methods:
A multicenter (n=6), prospective cohort (MESA exam 5, n=3,083 participants) underwent noncontrast chest CT with (n=296) and without (n=2,787) phantom. T1-T10 vertebrae were recursively selected in axial (planes (n=30,150, one for each vertebral level) and sagittal (n=6,030, upper and lower thoracic spine). A custom instance segmentation algorithm was developed. The internal validation set (n=360 participants, Northwestern University) was trained and tested and applied to an independent, external validation set (n=240 participants, University of Minnesota). We extracted pixel intensity (Hounsfield Units (HU)) and 2D surface area (mm2).

### Results:
The internal and external validation sets differed (P<0.001) according to race, HU, vertebral bone mineral density (vBMD), and surface area. Dice score for the internal (0.94 [0.94-0.93], 0.90 [0.91-0.89], 0.90 [0.91-0.89]) and external (0.93 [0.94-0.92], 0.87 [0.88-0.85], 0.85 [0.86-0.84]) validation set were reported for axial, T1-T5 sagittal, and T6-T10 sagittal, respectively. AI-derived HU were correlated with manual vBMD measurements from T1-T10 (R2=0.77, P<0.001). Black/African American participants had 34% (P<0.001) less variability in HU between T1-T10 compared with white/Caucasians. The surface area of vertebrae significantly increased from T1 (201 mm2) to T10 (903 mm2) in all races.

### Conclusions:
Our automated, multilevel algorithm can opportunistically determine the pattern of BMD and shape measurements in thoracic vertebrae from any conventional chest CT, revealing distinct distribution according to age, race, and gender.

## Overview of Study Design and Algorithm Development
![alt text](https://github.com/qahathaway/vBMD/blob/main/Overview.png)
Figure: Methodological Overview. (A) Non-contrast chest CT DICOM images from 3,015 participants were collected. The primary axial images were selected and converted to PNG. Using the primary axial images, a 3D volume was constructed to extract sagittal images. (B) Using pixel thresholding, the frames in the axial and sagittal planes were recursively selected to correspond to the middle of the vertebral body. Manual traces for the internal (n=360) and external (n=240) validation sets were performed using LabelMe. A custom instance segmentation, ROI inference pipeline was developed using PixelLib and Mask R-CNN. (C) The study included 3,015 participants, 600 of which had manual measurements. The Dice and intersection over union (IoU) score were calculated for the 600 participants with manual measurements (n=360 internal validation, n=240 external validation). The number of manual measurements included 6,000 for axial and 1,200 for sagittal. The number of images that AI-based inference was applied to included 30,150 axial and 6,030 sagittal.


## Example of AI-Driven ROI Inference for Axial and Sagittal
![alt text](https://github.com/qahathaway/vBMD/blob/main/Inference.png)
Figure: Example of Manual and Inferred Regions-of-Interest (ROIs) in the External Validation Set. (A) Representative axial frames from T1-T10 with the inferred ROIs (multicolored) superimposed over the manual traces (white). (B) Representative sagittal upper T1-T5 (left) and lower T6-T10 (right) with the inferred ROIs (multicolored) superimposed over the manual traces (white). (C) An example of a single vertebrae that has corresponding manual and AI-inferred ROIs.

### Code is made freely available for academic research and teaching. The code within this repository cannot be freely used for commercial applications.

# A Deep Learning Model for Three-Dimensional Determination of Whole Thoracic Vertebral Bone Mineral Density from Non-Contrast Chest CT: the Multi-Ethnic Study of Atherosclerosis

## TotalSegmentator 2.0 for 3D Segmentation
#### This code was adapted from https://github.com/wasserth/TotalSegmentator with modifcations as detailed within this repository.
#### Please cite the manuscript by Wasserthal et al. at: https://pubs.rsna.org/doi/10.1148/ryai.230024 or https://pmc.ncbi.nlm.nih.gov/articles/PMC10546353/


## Training weights and COCO weights for 2D Segmentation
#### Please contact qahathaway if you need the training weights or the pre-trained COCO weights, as storage on GitHub is difficult to maintain
#### Mask R-CNN pretrained COCO weigths link: https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5


### Key Results:
1.	In a secondary analysis of a multicenter cohort (Multiethnic Study of Atherosclerosis (MESA) Exam-5 and -6) of 1304 participants, a 3D deep learning (DL) model applied to phantomless, non-contrast chest CT images measured whole thoracic vertebral bone mineral density (BMD), with Dice scores of 0.93 [95% CI: 0.92-0.95] for the axial plane and 0.91 [95% CI: 0.88-0.93] for the sagittal plane, compared to manual segmentation (n=594).
2.	CT-derived 3D vertebral BMD integrated with all features outperformed the Fracture Risk Assessment Tool with no BMD (FRAXnb) alone when predicting incident vertebral fractures (VFx) (AUC: 0.82 [95% CI: 0.72-0.93] versus 0.66 [95% CI: 0.49-0.79], P=.03).
3.	DL-derived 2D models provided higher measurement uncertainty for 2D axial (average standard deviation, 65 mg/cm3, P<.001) and 2D sagittal (59 mg/cm3, P<.001) imaged planes compared to 3D BMD measurements (41 mg/cm3).

### Summary Statement:
A multilevel, three-dimensional, deep learning segmentation algorithm applied to non-contrast chest CT images delineated distinct bone mineral density patterns from whole thoracic vertebrae and provided incremental value in predicting vertebral fractures.

### Background:
Recent work has investigated how deep learning (DL) algorithms applied to CT using two-dimensional (2D) segmentation (sagittal or axial planes) can calculate bone mineral density (BMD) and predict osteoporosis-related outcomes.

### Purpose:
To determine whether TotalSegmentator, a nnU-net algorithm, can measure three-dimensional (3D) vertebral body BMD throughout consistently imaged thoracic levels (T1-T10) in any conventional, non-contrast chest CT examinations.

### Materials and Methods:
This study is a secondary analysis of a multicenter (n=6) prospective cohort (Multiethnic Study of Atherosclerosis (MESA). Participants underwent non-contrast chest CT with (n=296) and without (n=2660) phantom. In 594 participants, manual segmentation for T1-T10 vertebrae in axial and sagittal planes was performed. TotalSegmentator provided 3D vertebral body segmentation of T1-T10 levels with further post-processing to remove cortical bone. 2D axial and sagittal DL-derived algorithms were developed and compared with 3D model performance. Dice and intersection-over-union scores were calculated. Vertebral BMD-derived data, integrated with the Fracture Risk Assessment Tool with no BMD (FRAXnb), was used to predict incident vertebral fractures (VFx) in participants from the follow-up MESA Exam-6 (n=1304).

### Results:
This study included 2956 participants (52% female, aged 69 ± 9 years) with longitudinal data obtained approximately 6.2 years later in a subset of 1304 participants. DL-derived 3D segmentations were correlated with manual axial (Dice: 0.93 [0.91-0.96]) and sagittal (Dice: 0.91 [0.87-0.94]) segmentations, respectively. DL-derived 2D-axial and -sagittal BMD measurements had higher uncertainty compared to DL-derived 3D BMD measurements (average standard deviation, 2D-axial: 65 mg/cm3, 2D-sagittal: 59 mg/cm3 versus 3D: 41 mg/cm3, both P<.001). 3D vertebral BMD with FRAXnb demonstrated better performance in predicting incident VFx (AUC: 0.82) compared to FRAXnb alone (AUC 0.66, P=.03).

### Conclusion:
A multilevel DL algorithm for measuring 3D whole thoracic vertebral BMD using conventional chest CT determined distinct BMD patterns from whole thoracic vertebrae and provided incremental value in predicting vertebral fractures.

#### ClinicalTrials.gov: NCT00005487


## Overview of Study Design and 3D Algorithm Development
![alt text](https://github.com/qahathaway/vBMD/blob/main/Overview.jpg)
#### 3D Segmentation Overview.
(A) Non-contrast chest CT DICOM images from 2956 participants were collected. The primary axial images were selected and converted to a NIFTI volume for 3D segmentation using the TotalSegmentator algorithm. (B) Using the TotalSegmentator algorithm, 3D volumes of the T1-T10 vertebral bodies for each participant were collected. The extracted 3D volume of the vertebral body was further modified to remove cortical bone. (C) In 594 participants with manual segmentation (using LabelMe) of axial and sagittal frames, Dice score and Intersection over Union (IoU) were calculated for the 3D segmentation. The diagram, containing the grey circles, illustrates how overlapping manual and automated segmentation is used to generate the Dice and IoU scores. (D) An example of T7-T10 vertebral bodies illustrating a T8-T9 wedge grade 3 fracture. To the right is an AUC curve depicting the performance of clinical and deep learning-derived variables to predict incident vertebral fractures. Lines are colored by feature, displayed in the legend in the bottom right of the plot.


## Example of AI-Driven ROI Inference for Axial and Sagittal
![alt text](https://github.com/qahathaway/vBMD/blob/main/Inference.jpg)
#### 2D Axial and Sagittal Segmentation Overview.
Representative non-contrast chest CT DICOM images for (A) axial and (B) sagittal segmentation illustrating manual labeling (white ROI) overlayed with inferred ROI (colored for contrast) using the 2D DL-derived algorithm. (C) A custom instance segmentation, ROI inference pipeline was developed using PixelLib and Mask R-CNN. Representative non-contrast chest CT images show T10 examined by each step of the 2D DL-derived algorithm. In the box, the ROI alignment and deep learning process are illustrated, which results in a final segmentation (far right), where the inferred ROI is displayed in purple.




### Code is made freely available for academic research and teaching. The code within this repository cannot be freely used for commercial applications.

# Jupyter Notebook code for semi-automated and automated vertebral bone mineral denisty assessement

## Steps
A) Convert DICOM to PNG
B) Select original, primary axial images
C) Select T1-T10 in indivdual PNGs in the axial view and an upper and lower PNG for sagittal
D) Manually trace the ROI for 600 patients
E) Train (60%) and hold-out testing (40%) for the 600 patients using MASK R-CNN and Pixellib
F) Infer based on the developed model
G) Calculate Dice Score and Intersection over union

### Pixel Intensities used for Frame Selection
![alt text](https://github.com/qahathaway/vBMD/blob/main/Jupyter-Notebook/Pixel_Intensities_vBMD.jpg)

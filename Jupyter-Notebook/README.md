# Jupyter Notebook code for semi-automated and automated vertebral bone mineral denisty assessement

## Steps
##### A) Convert DICOM to PNG
##### B) Select original, primary axial images
##### C) Select T1-T10 PNGs in the axial (n=10 images per participant) and sagittal (n=2 images per participant)
#####   C.2) Individual frames are required for axial, whereas an upper (i.e., T1-T5) and lower (T6-T10) sagittal image was acquired
##### D) Manually trace the ROI for 600 patients (n=6,000 axial, n=1,200 sagittal)
##### E) Internal validaiton (n=360) and independent, external validation (n=240) set using MASK R-CNN and Pixellib
##### F) Infer based on the developed AI-model
##### G) Calculate Dice Score and Intersection over union
##### H) Use PyRadiomics to extract pixel level and shape information

### Pixel Intensities used for Frame Selection in Sagittal
![alt text](https://github.com/qahathaway/vBMD/blob/main/Jupyter-Notebook/Threshold_Sagittal.png)
Figure: Selection of Sagittal Frames (T1-T10) using Pixel Thresholding. (A) Process for selecting the mid portion of the spine, shown in a participant without scoliosis (Cobb angle < 10o). Histogram depicting the pixel values across the spinal column reveal three peaks. The middle peak (#2) is associated with the spinous process and the mid-vertebral level. (B) Process for selecting the mid portion of the spine used in the current study, shown in a participant with scoliosis (Cobb angle ≥ 10o). Images were cropped to include the T1-T5 (i.e., upper sagittal spine) and T6-T10 (i.e., lower sagittal spine) to account for scoliosis and spine curvature. Histogram depicting the pixel values across the spinal column reveal three peaks. The middle peak is associated with the spinous process and the mid-vertebral level.


### Pixel Intensities used for Frame Selection in Axial
![alt text](https://github.com/qahathaway/vBMD/blob/main/Jupyter-Notebook/Threshold_Axial.png)
Figure: Selection of Axial Frames using Pixel Thresholding. (A) Sagittal plane depicting the T1-T10 vertebrae of interest. (B) Histogram depicting the pixel values from T4-T7. The troughs correspond to the middle of the vertebral body whereas the peaks represent the transition of cortical bone on the superior and inferior aspect of the vertebrae.

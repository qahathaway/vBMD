### DL-Derived 3D Vertebral Body Segmentation

#### Step-1-NIFTI.py
Convert DICOM files into a single NIFTI file

#### Step-2-Whole-Vertebrae.sh
Use the task "vertebrae_body" to segment all of the vertebae on the chest CT

#### Step-3-Individual-Vertebrae.sh
Use the task "roi_subset" to indvidually segment out only the vertebral bodies of T1-T10.

#### Step-4-Remove-Cortical-Bone.py
Use spatial information from the "vertebrae_body" and "roi_subset" of T1-T10 to create individual masks of T1-T10 while also removing cortical bone.

#### Overview of Methods
The original algorithm, TotalSegmentator v2 (1), has been recently developed using the nnU-net framework (2) on eight different clinical sites and 16 different scanners. Both 1.5- and 3.0-mm isotropic resolution CT scans were trained through batches of iterative annotation. Data augmentation was applied, and 1.5 mm slices were trained for 4,000 epochs, whereas 3.0 mm slices were trained for 8,000 epochs. The algorithm is capable of volumetric segmentation of 117 anatomic structures from a wide variety of CT acquisitions, demonstrating its generalizability (1). The volumetrically segmented structures include vertebral bodies and paraspinal muscles with DICE coefficients of 0.94 on internal testing and 0.93 on external testing for all anatomical regions measured. Using Python 3.9.19, DICOM images with the primary axial sequence were selected and converted to NIFTI format using nibabel (v.5.2.1) and pydicom (v.2.4.4). Using TotalSegmentator (v2.1.0) (1) and the nnU-net architecture (2), 3D segmentation of the vertebral body for T1-T10 was accomplished, with distinct modifications.

These modifications included processing the 3D segmentation into 3D numpy arrays (v.1.26.4) in Python (i.e., 1) vertebral body with the vertebral arch designated by location and 2) all vertebral body measurements (not including the vertebral arch), which were extracted from TotalSegmentator); these two outputs were combined to designate T1-T10 locations, and the vertebral body data overlaid for each defined level (i.e., T1-T10 vertebral body data labeled by location). We further modified and optimized the TotalSegmentator algorithm by removing any cortical bone using the previously established attenuation threshold of > 700 Hounsfield units from the mask volume (3).

1. Wasserthal J, Breit HC, Meyer MT, Pradella M, Hinck D, Sauter AW, Heye T, Boll DT, Cyriac J, Yang S, Bach M, Segeroth M. TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images. Radiol Artif Intell 2023;5(5):e230024. doi: 10.1148/ryai.230024
2. Isensee F, Jaeger PF, Kohl SAA, Petersen J, Maier-Hein KH. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nat Methods 2021;18(2):203-211. doi: 10.1038/s41592-020-01008-z
3. Lim Fat D, Kennedy J, Galvin R, O'Brien F, Mc Grath F, Mullett H. The Hounsfield value for cortical bone geometry in the proximal humerus--an in vitro study. Skeletal Radiol 2012;41(5):557-568. doi: 10.1007/s00256-011-1255-7

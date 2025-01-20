#!/bin/bash -l
#SBATCH -J Individual_Vertebrae

module load anaconda
conda activate TotalSeg

for FILE in /path/to/NIFTI/directory/*.nii;
do filename=$(basename "$FILE");
filename="${filename%.*}";
TotalSegmentator -i $FILE -o /path/to/output/segmentations/$filename -ta total --roi_subset vertebrae_T1 vertebrae_T2 vertebrae_T3 vertebrae_T4 vertebrae_T5 vertebrae_T6 vertebrae_T7 vertebrae_T8 vertebrae_T9 vertebrae_T10;
done

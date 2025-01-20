#!/bin/bash -l
#SBATCH -J Whole_Vertebrae

module load anaconda
conda activate TotalSeg

for FILE in /path/to/NIFTI/directory/*.nii;
do filename=$(basename "$FILE");
filename="${filename%.*}";
TotalSegmentator -i $FILE -o /path/to/output/segmentations/$filename -ta vertebrae_body;
done

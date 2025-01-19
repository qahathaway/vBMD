#!/bin/bash -l
#SBATCH -J TotalSeg_T1T10
#SBATCH --time=72:0:0
#SBATCH -N 1
#SBATCH --ntasks-per-node=12
#SBATCH --mem-per-cpu=4GB
#SBATCH --quiet


module load anaconda
conda activate TotalSeg

for FILE in /home/sdemehr1/scr16_sdemehr1/MESA_Exam5_NIFTI/*.nii;
do filename=$(basename "$FILE");
filename="${filename%.*}";
TotalSegmentator -i $FILE -o /home/sdemehr1/data_sdemehr1/TotalSegmentator/Segmentations3/$filename -ta total --roi_subset vertebrae_T1 vertebrae_T2 vertebrae_T3 vertebrae_T4 vertebrae_T5 vertebrae_T6 vertebrae_T7 vertebrae_T8 vertebrae_T9 vertebrae_T10;
done

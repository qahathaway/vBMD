### Load Essential Packages ###
import pydicom
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import csv
import cv2
import os
from os import listdir
from os.path import isfile, join
import dicom2nifti # to convert DICOM files to the NIftI format
import nibabel as nib # nibabel to handle nifti files
from pathlib import Path # pathlib for easy path handling

folder = '/path/to/main/DICOM/repository'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
sortedfolder = sorted(sub_folders)

for q in sortedfolder:
    files = []
    
    try:
        # Create NIFTI files from DICOM for All Patients in Directory #
        for filename in sorted(glob.glob('/path/to/main/DICOM/repository/' + q + '/*')):
            files.append(pydicom.dcmread(filename, force=True))

        try:
            dicom2nifti.convert_dicom.dicom_array_to_nifti(files, '/path/to/main/output/NIFIT/directory/'+ q)
        except:
            pass

    except TypeError:
        pass

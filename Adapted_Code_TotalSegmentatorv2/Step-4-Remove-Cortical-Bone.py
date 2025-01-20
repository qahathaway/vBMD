#Import necessary libraries
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import os
import csv

import SimpleITK as sitk
import six
import radiomics
from radiomics import featureextractor

dataDir = '/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Radiomics'
radiomicsCSV = os.path.join(dataDir, 'RadiomicsVert3-Exam6.csv')
params = os.path.join(dataDir, "Params.yaml")
headers = None

for scanFilePath in sorted(glob.glob("/home/sdemehr1/data_sdemehr1/MESA_Exam6_NIFTI/MESA3*.nii")):
    for scanFilePath2 in sorted(glob.glob("/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Segmentations/MESA3*/*.nii.gz")):
        if scanFilePath[46:57] == scanFilePath2[66:77]:
            for scanFilePath3 in sorted(glob.glob("/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Segmentations3/MESA3*/*.nii.gz"), key=lambda name: (name[67:78], int(os.path.basename(name)[11:-7]))):
                if scanFilePath2[66:77] == scanFilePath3[67:78]:
                    path, filenames = os.path.split(scanFilePath3)
                    path2 = os.path.basename(path)

                    #Load the scan and extract data using nibabel 
                    scan = nib.load(scanFilePath)
                    scanArray = scan.get_fdata()
                    scan2 = nib.load(scanFilePath2)
                    scanArray2 = scan2.get_fdata()
                    scanArray2[scanArray2 >= 1] = 1

                    try:

                        if filenames[10:-7] == 'T1':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T1 = cv2.add(scanArray2, scanArray3)
                            T1[T1 == 1] = 0
                            T1[T1 == 2] = 255
                            T1_img = nib.Nifti1Image(T1, scan2.affine)
                            nib.save(T1_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T1_Mask.nii.gz")
                            T1FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T1_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT1 = extractor.execute(scanFilePath, T1FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT1.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT1.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT1.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT1.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        elif filenames[10:-7] == 'T2':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T2 = cv2.add(scanArray2, scanArray3)
                            T2[T2 == 1] = 0
                            T2[T2 == 2] = 255
                            T2_img = nib.Nifti1Image(T2, scan2.affine)
                            nib.save(T2_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T2_Mask.nii.gz")
                            T2FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T2_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT2 = extractor.execute(scanFilePath, T2FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT2.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT2.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT2.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT2.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)        

                        elif filenames[10:-7] == 'T3':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T3 = cv2.add(scanArray2, scanArray3)
                            T3[T3 == 1] = 0
                            T3[T3 == 2] = 255
                            T3_img = nib.Nifti1Image(T3, scan2.affine)
                            nib.save(T3_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T3_Mask.nii.gz")
                            T3FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T3_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT3 = extractor.execute(scanFilePath, T3FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT3.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT3.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT3.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT3.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        elif filenames[10:-7] == 'T4':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T4 = cv2.add(scanArray2, scanArray3)
                            T4[T4 == 1] = 0
                            T4[T4 == 2] = 255
                            T4_img = nib.Nifti1Image(T4, scan2.affine)
                            nib.save(T4_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T4_Mask.nii.gz")
                            T4FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T4_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT4 = extractor.execute(scanFilePath, T4FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT4.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT4.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT4.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT4.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        elif filenames[10:-7] == 'T5':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T5 = cv2.add(scanArray2, scanArray3)
                            T5[T5 == 1] = 0
                            T5[T5 == 2] = 255
                            T5_img = nib.Nifti1Image(T5, scan2.affine)
                            nib.save(T5_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T5_Mask.nii.gz")
                            T5FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T5_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT5 = extractor.execute(scanFilePath, T5FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT5.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT5.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT5.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT5.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        elif filenames[10:-7] == 'T6':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T6 = cv2.add(scanArray2, scanArray3)
                            T6[T6 == 1] = 0
                            T6[T6 == 2] = 255
                            T6_img = nib.Nifti1Image(T6, scan2.affine)
                            nib.save(T6_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T6_Mask.nii.gz")
                            T6FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T6_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT6 = extractor.execute(scanFilePath, T6FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT6.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT6.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT6.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT6.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        elif filenames[10:-7] == 'T7':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T7 = cv2.add(scanArray2, scanArray3)
                            T7[T7 == 1] = 0
                            T7[T7 == 2] = 255
                            T7_img = nib.Nifti1Image(T7, scan2.affine)
                            nib.save(T7_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T7_Mask.nii.gz")
                            T7FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T7_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT7 = extractor.execute(scanFilePath, T7FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT7.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT7.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT7.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT7.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        elif filenames[10:-7] == 'T8':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T8 = cv2.add(scanArray2, scanArray3)
                            T8[T8 == 1] = 0
                            T8[T8 == 2] = 255
                            T8_img = nib.Nifti1Image(T8, scan2.affine)
                            nib.save(T8_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T8_Mask.nii.gz")
                            T8FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T8_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT8 = extractor.execute(scanFilePath, T8FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT8.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT8.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT8.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT8.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        elif filenames[10:-7] == 'T9':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T9 = cv2.add(scanArray2, scanArray3)
                            T9[T9 == 1] = 0
                            T9[T9 == 2] = 255
                            T9_img = nib.Nifti1Image(T9, scan2.affine)
                            nib.save(T9_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T9_Mask.nii.gz")
                            T9FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T9_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT9 = extractor.execute(scanFilePath, T9FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT9.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT9.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT9.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT9.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        elif filenames[10:-7] == 'T10':
                            scan3 = nib.load(scanFilePath3)
                            scanArray3 = scan3.get_fdata()
                            scanArray3[scanArray3 >= 1] = 1
                            T10 = cv2.add(scanArray2, scanArray3)
                            T10[T10 == 1] = 0
                            T10[T10 == 2] = 255
                            T10_img = nib.Nifti1Image(T10, scan2.affine)
                            nib.save(T10_img, "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T10_Mask.nii.gz")
                            T10FilePath = "/home/sdemehr1/data_sdemehr1/TotalSegmentator_Exam6/Mask_Vert/" + path2 + "_T10_Mask.nii.gz"
                            extractor = featureextractor.RadiomicsFeatureExtractor(params)
                            resultT10 = extractor.execute(scanFilePath, T10FilePath, label=255)
                            with open(radiomicsCSV, 'a') as outputFile:
                                writer = csv.writer(outputFile, lineterminator='\n')
                                if headers is None:
                                    headers = list(resultT10.keys())
                                    headers.insert(0, 'Slice')
                                    headers.insert(0, 'Name')
                                    writer.writerow(headers)
                                types1 = [type(k) for k in resultT10.values()]
                                string_list = [str(element) for element in types1]
                                row = []
                                m = 0
                                for i in string_list:
                                    if i == "<class 'numpy.ndarray'>":
                                        row.append(float(list(resultT10.values())[m]))
                                        m+=1
                                    else:
                                        row.append(list(resultT10.values())[m])
                                        m+=1
                                row.insert(0, filenames[10:-7])
                                row.insert(0, path2)
                                writer.writerow(row)

                        else:
                            continue

                    except TypeError:
                        pass

                else:
                    continue

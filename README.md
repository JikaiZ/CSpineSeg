# CSpineSeg
This repository includes essential code scripts to curate the Duke Cervical Spine MRI Dataset.

## Code Files
- dicom_nifti_dcm2niix.py: This script converts a series of DICOM files to one NIfTI file using “dcm2niix” toolkit. Users need to specify the input folder path that contains the original DICOM
files, the output folder path, and a pandas dataframe that records basic information of the DICOM files.
- nnUNet_Setup.py: This script organizes the input NIfTI files for nnU-Net pipeline into a separate folder. Users need to specify the location of the input NIfTI files, and the development (training + validation) plus the test set for training/validating a nnU-Net model. Other customizable configurations include the dataset id, task name, and folders that save training/testing/un-annotated images.
- nnUNet_env_set.sh: This script includes command lines that implements nnU-Net, including preprocessing, training of 2d and 3d_fullres models, and inference using 2d, 3d_fullres and ensembled outputs of both

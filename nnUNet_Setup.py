import os
import pandas as pd
import shutil

from batchgenerators.utilities.file_and_folder_operations import *
from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json
import json


if __name__ == '__main__':
	# separate the training, validation and test data based on user's need
	TRAIN_df = pd.read_csv("<PATH_TO_TRAIN_METADATA_CSV>")
	VAL_df = pd.read_csv("<PATH_TO_VAL_METADATA_CSV>")
	TEST_df = pd.read_csv("<PATH_TO_TEST_METADATA_CSV>")
	# nnUNet cross validation 
	full_df = pd.concat([TRAIN_df, VAL_df])
	# nifti file path
    data_dir = "<PATH_TO_NIFTI_DATA>"
    # destination file path
    dest_dir = "<PATH_TO_NNUNET_DEST>" 

    # raw_brats_data_dir = '../../data/BraTs'
    # convert_brats_data_dir = './BraTs_convert/'

    task_id = 108
    task_name = "CSpineSeg"

    data_path = "Dataset%03.0d_%s" % (task_id, task_name)

    # setting up nnU-Net folders
    imagestr = os.path.join(dest_dir, data_path, "imagesTr")
    labelstr = os.path.join(dest_dir, data_path, "labelsTr")
    
    maybe_mkdir_p(imagestr)
    maybe_mkdir_p(labelstr)

    mri_case_ids = full_df['MRI_CASE_ID'].values
    mask_case_ids = full_df['MASK_CASE_ID'].values
    N_train = len(mri_case_ids)
    
    for idx, _mri_id in enumerate(mri_case_ids):
        print(f"Processing {_mri_id}")
        # pid, eid = _mri_id.split(".")[0].split("_")[1], _mri_id.split(".")[0].split("_")[2]
        new_fname = "cspine_%d_0000" % (idx)
        shutil.copyfile(join(data_dir, _mri_id + ".nii.gz"), join(imagestr, new_fname + ".nii.gz"))
    for idx, _mask_id in enumerate(mask_case_ids):
        print(f"Processing {_mask_id}")
        new_fname = "cspine_%d" % (idx)
        seg_example = nib.load(join(data_dir, _mask_id + ".nii.gz"))
        print(np.sum(seg_example.get_fdata() == 1))
        shutil.copyfile(join(data_dir, _mask_id + ".nii.gz"), join(labelstr, new_fname + ".nii.gz"))

    # Test set not for training        
    imagests = os.path.join(dest_dir, data_path, "imagesTs")
    labelsts = os.path.join(dest_dir, data_path, "labelsTs")
    maybe_mkdir_p(imagests)
    maybe_mkdir_p(labelsts)
        
    mri_case_ids = TEST_df['MRI_CASE_ID'].values
    mask_case_ids = TEST_df['MASK_CASE_ID'].values
    
    for idx, _mri_id in enumerate(mri_case_ids):
        print(f"Processing {_mri_id}")
        # pid, eid = _mri_id.split(".")[0].split("_")[1], _mri_id.split(".")[0].split("_")[2]
        new_fname = "cspine_%d_0000" % (idx)
        shutil.copyfile(join(data_dir, _mri_id + ".nii.gz"), join(imagests, new_fname + ".nii.gz"))
    for idx, _mask_id in enumerate(mask_case_ids):
        print(f"Processing {_mask_id}")
        new_fname = "cspine_%d" % (idx)
        shutil.copyfile(join(data_dir, _mask_id + ".nii.gz"), join(labelsts, new_fname + ".nii.gz"))


    generate_dataset_json(os.path.join(dest_dir, data_path), 
        channel_names={'0': 'T2'},
        labels={'background':0, 'vertebrae':1, 'inter-vetebral disc':2}, 
        dataset_name="CSpineSeg",
        num_training_cases=N_train,
        file_ending='.nii.gz')